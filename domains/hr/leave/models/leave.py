'''
class Staff(models.Model):
	

	def get_name(self):
		"""Return the employe member's name."""
		return f"{self.first_name} {self.last_name}"

	def _current_year(self):
		"""Get the current year."""
		return datetime.today().year

	def get_approved_leave_days(self, year: Optional[int] = None):
		"""Get approved leave days in the current year."""
		return get_taken_leave_days(
			staff=self,
			status=Leave.APPROVED,
			leave_type=Leave.REGULAR,
			start_year=year or self._current_year,
			end_year=year or self._current_year,
		)

	def get_approved_sick_days(self, year: Optional[int] = None):
		"""Get approved leave days in the current year."""
		return get_taken_leave_days(
			staff=self,
			status=Leave.APPROVED,
			leave_type=Leave.SICK,
			start_year=year or self._current_year,
			end_year=year or self._current_year,
		)

	def get_available_leave_days(self, year: Optional[int] = None):
		"""Get available leave days."""
		try:
			# pylint: disable=no-member
			leave_record = AnnualLeave.objects.get(
				leave_type=Leave.REGULAR, staff=self, year=year or self._current_year
			)
		except AnnualLeave.DoesNotExist:
			return Decimal(0)
		else:
			return leave_record.get_available_leave_days()

	def get_available_sick_days(self, year: Optional[int] = None):
		"""Get available sick days."""
		try:
			# pylint: disable=no-member
			leave_record = AnnualLeave.objects.get(
				leave_type=Leave.SICK, staff=self, year=year or self._current_year
			)
		except AnnualLeave.DoesNotExist:
			return Decimal(0)
		else:
			return leave_record.get_available_leave_days()

	def str(self):
		"""Unicode representation of class object."""
		return self.get_name()  # pylint: disable=no-member


#leave start

YEAR_CHOICES = (
	(str(i), i) for i in range(2000, 2023)
)

class StaffRequest(models.Model):
	Staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
	start = models.DateTimeField(null=True, blank=True)
	end = models.DateTimeField(null=True, blank=True)
	review_reason = models.TextField()
	review_status = models.CharField(max_length=250, default='pending')

	class Meta:
		abstract = True
		db_table = 'Staffs'


class Leave(StaffRequest):
	SICK = "1"
	REGULAR = "2"
	MATERNITY = "3"
	APPROVED = "4"

	TYPE_CHOICES = (
		(SICK, _("Sick Leave")),
		(REGULAR, _("Regular Leave")),
		(MATERNITY, _("Regular Leave")),
	)

	leave_type = models.CharField(max_length=10)

	def str(self):
		# pylint: disable=no-member
		return _(f"{self.Staff.get_name()}: {self.start} to {self.end}")

	def get_duration(self):
		"""Get duration."""
		return self.end - self.start

	def duration(self):
		"""Get duration as a property."""
		return self.get_duration()

	def day_count(self):
		"""
		Get the number of leave days as a property.

		This takes into account holidays and weekend policy.
		"""
		return get_real_leave_duration(leave_obj=self)


class OverTime(StaffRequest):
	date = models.DateTimeField(default=datetime.utcnow())
	start = models.DateTimeField(null=True, blank=True)
	end = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = "over_times"

	def str(self):
		"""Unicode representation of class object."""
		name = self.Staff.get_name()  # pylint: disable=no-member
		return _(f"{name}: {self.date} from {self.start} to {self.end}")  # unresolved reference "_"

	def get_duration(self):
		"""Get duration."""
		start = datetime.combine(self.date, self.start.time())
		end = datetime.combine(self.date, self.end.time())
		return end - start

	def duration(self):
		"""Get duration as a property."""
		return self.get_duration()


	class AnnualLeave(TimeStampedModel, models.Model):
		"""
		Model to keep track of staff Staff annual leave.

		This model is meant to be populated once a year
		Each staff member can only have one record per leave_type per year
		"""

		# YEAR_CHOICES = [(r, r) for r in range(2017, datetime.today().year + 10)]

		year = models.PositiveIntegerField(
			_("Year"), choices=YEAR_CHOICES, default=2017, db_index=True
		)
		staff = models.ForeignKey(
			Staff, verbose_name=_("Staff Member"), on_delete=models.CASCADE
		)
		leave_type = models.CharField(
			_("Type"), max_length=1, choices=Leave.TYPE_CHOICES, db_index=True
		)
		allowed_days = models.DecimalField(
			_("Allowed Leave days"),
			default=21,
			blank=True,
			decimal_places=1,
			max_digits=12,
			validators=[MinValueValidator(Decimal('0.1'))],
			help_text=_("Number of leave days allowed in a year."),
		)
		carried_over_days = models.DecimalField(
			_("Carried Over Leave days"),
			default=0,
		blank=True,
		decimal_places=1,
		max_digits=12,
		validators=[MinValueValidator(Decimal('0.1'))],
		help_text=_("Number of leave days carried over into this year."),
	)

	class Meta:  # pylint: disable=too-few-public-methods
		"""Meta options for AnnualLeave."""
		db_table = "_annual_leaves"
		verbose_name = _("Annual Leave")
		verbose_name_plural = _("Annual Leave")
		ordering = ["-year", "leave_type", "staff"]
		unique_together = (("year", "staff", "leave_type"),)

	def str(self):
		"""Unicode representation of class object."""
		# pylint: disable=no-member
		return _(
			f"{self.year}: {self.staff.get_name()} " f"{self.get_leave_type_display()}"
		)

	def get_cumulative_leave_taken(self):
		"""
		Get the cumulative leave taken.
		Returns a timedelta
		"""
		return get_taken_leave_days(
			staffprofile=self.staff,
			status=Leave.APPROVED,
			leave_type=self.leave_type,
			start_year=self.year,
			end_year=self.year,
		)

	def get_available_leave_days(self, month: int = 12):
		"""Get the remaining leave days."""
		if month <= 0:
			month = 1
		elif month > 12:
			month = 12

		# the max allowed days per year
		allowed = self.allowed_days

		# the days earned per month
		per_month = Decimal(allowed / 12)

		# the days earned so far, given the month
		earned = Decimal(month) * per_month

		# the days taken
		taken = self.get_cumulative_leave_taken()

		# the starting balance
		starting_balance = self.carried_over_days

		return Decimal(earned + starting_balance - taken)


class FreeDay(models.Model):
	"""Model definition for FreeDay."""

	name = models.CharField(_("Name"), max_length=255)
	date = models.DateField(_("Date"), unique=True)

	class Meta:
		"""Meta definition for FreeDay."""

		ordering = ["-date"]
		verbose_name = _("Free Day")
		verbose_name_plural = _("Free Days")

	def str(self):
		"""Unicode representation of class object."""
		return f"{self.date.year} - {self.name}"

	@staticmethod
	def get_days(start: object, end: object):
		"""Yield the days between two datetime objects."""
		current_tz = timezone.get_current_timezone()
		local_start = current_tz.normalize(start)
		local_end = current_tz.normalize(end)
		span = local_end.date() - local_start.date()
		for i in range(span.days + 1):
			yield local_start.date() + timedelta(days=i)

	@staticmethod
	def get_real_leave_duration(leave_obj: Leave) -> Decimal:
		"""
		Get the real leave duration.

		Takes into account public holidays, weekends and weekend policy
		"""
		count = Decimal(0)
		free_days = FreeDay.objects.filter(
			date__gte=leave_obj.start.date(), date__lte=leave_obj.end.date()
		).values_list("date", flat=True)
		days = get_days(start=leave_obj.start, end=leave_obj.end)
		for day in days:
			if day not in free_days:
				day_value = settings.SSHR_DAY_LEAVE_VALUES[day.isoweekday()]  # unresolved call "settings"
				count = count + Decimal(day_value)
		return count

	@staticmethod
	def get_taken_leave_days(
			staffprofile: object, status: str, leave_type: str, start_year: int, end_year: int
	):
		"""
		Calculate the number of leave days actually taken.
		Takes into account weekends and weekend policy
		"""
		count = Decimal(0)
		free_days = FreeDay.objects.filter(
			date__year__gte=start_year, date__year__lte=end_year
		).values_list("date", flat=True)
		queryset = Leave.objects.filter(
			staff=staffprofile, review_status=status, leave_type=leave_type
		).filter(Q(start__year__gte=start_year) | Q(end__year__lte=end_year))
		for leave_obj in queryset:
			days = get_days(start=leave_obj.start, end=leave_obj.end)
			for day in days:
				if start_year <= day.year <= end_year and day not in free_days:
					day_value = settings.SSHR_DAY_LEAVE_VALUES[day.isoweekday()]  # unresolved call "settings"
					count = count + Decimal(day_value)
		return count
art_year) | Q(end__year__lte=end_year))
		for leave_obj in queryset:
			days = get_days(start=leave_obj.start, end=leave_obj.end)
			for day in days:
				if start_year <= day.year <= end_year and day not in free_days:
					day_value = settings.SSHR_DAY_LEAVE_VALUES[day.isoweekday()]  # unresolved call "settings"
					count = count + Decimal(day_value)
		return count



from datetime import datetime, date

from pydantic import BaseModel, validator


class OddDate(BaseModel):
    birthdate: date

    @validator("birthdate", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()


if __name__ == "__main__":
    odd_date = OddDate(birthdate="12/04/1992")
    print(odd_date.json()) #{"birthdate": "1992-04-12"}
    
    
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer(), primary_key=True)
    manager_id = Column(Integer(), ForeignKey('employees.id'))
    name = Column(String(255), nullable=False)
    manager = relationship("Employee", backref=backref('reports'),
    		remote_side=[id])
'''

from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, func, extract
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date, timedelta
from sqlalchemy import (Column, Integer, String, ForeignKey, Numeric, Date,
                        Boolean, Float, DateTime, Text)
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
import datetime

from typing import List, Any
from sqlalchemy.orm import backref
from .leave_type import LeaveType
# from app.domains.hr.staff.models import Staff


from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, func, extract
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date, timedelta
from app.db.base_class import APIBase, UUID
from app.domains.hr.leave.models.leave_type import LeaveType


class Leave(APIBase):

    staff_id = Column(UUID, ForeignKey("staffs.id"))
    leave_type_id = Column(UUID, ForeignKey("leave_types.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    # is_approved = Column(Boolean, default=False)
    status = Column(String)  # pending, declined /approved
    staff = relationship("Staff", back_populates="leaves")
    leave_type = relationship("LeaveType")
