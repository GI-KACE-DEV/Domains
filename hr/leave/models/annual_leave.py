
from sqlalchemy import  Column, Integer, String, Date, Boolean, func, extract, ForeignKey
from sqlalchemy.orm import  relationship
from datetime import date, timedelta
from app.db.base_class import APIBase, UUID, Base

#from app.domains.hr.staff.models import Staff
from app.domains.hr.leave.models.leave_type import LeaveType


class AnnualLeave(APIBase):

    staff_id = Column(UUID, ForeignKey("staffs.id"))
    leave_type_id = Column(UUID, ForeignKey("leave_types.id"))
    allocated_days = Column(Integer)
    allocation_date = Column(Date)
    staff = relationship("Staff", back_populates="annual_leaves")
    leave_type = relationship("LeaveType")
