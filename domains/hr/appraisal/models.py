from sqlalchemy import (Column, Integer, String, ForeignKey, Numeric, Date,
                        	Boolean,Float, DateTime, Text)
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
import datetime

from typing import List,Any
from sqlalchemy.orm import backref


class ReviewPeriod(APIBase):
    
	title = Column(String(250) )
	description = Column(Text, nullable=True)
	start_date = Column(Date)
	end_date = Column(Date)
	year = Column(Integer)
 
	def __str__(self):
		return self.title

	def get_reviews_by_year(self, year: int) -> List[Any]:
		pass
	

class FirmTarget(APIBase):
	title = Column(String(250))
	description = Column(Text)
	success_indicator = Column(Text, nullable=True)
	minimum_rating = Column(Float, nullable=True, default=0.0)
	maximum_rating = Column(Float, nullable=True, default=0.0)
	start_date = Column(Date, nullable=True)
	end_date = Column(Date, nullable=True)
 
	year = Column(Integer, nullable=True)
	review_period_id = Column(UUID, ForeignKey("review_periods.id"))
	review_period = relationship("ReviewPeriod", backref="firm_targets")

	def __str__(self) -> str:
		return self.title


class DepartmentTarget(APIBase):
    
	title = Column(String(250))
	description = Column(Text, nullable=True)
	success_indicator = Column(Text, nullable=True)
	start_date = Column(Date, nullable=True)
	end_date = Column(Date, nullable=True)
	minimum_rating = Column(Float, nullable=False, default=0.0)
	maximum_rating = Column(Float, nullable=False, default=0.0)

	review_period_id = Column(UUID, ForeignKey("review_periods.id"), nullable=True)
	firm_target_id = Column(UUID, ForeignKey("firm_targets.id"), nullable=True)
	
	review_period = relationship("ReviewPeriod", backref="department_targets")
	firm_target = relationship("FirmTarget", backref="department_targets")


class StaffTarget(APIBase):
    
	title = Column(String(250))
	description = Column(Text, nullable=True)
	department_target_id = Column(UUID, ForeignKey("department_targets.id"))
	success_indicator = Column(Text, nullable=False)
	staff_id = Column(UUID, ForeignKey("staffs.id"))     
	supervisor_id = Column(UUID, ForeignKey("staffs.id")) 
	employee_remarks = Column(Text, nullable=True)
	supervisor_remarks = Column(Text, nullable=True)
	status = Column(String(20)) #opened/ finalized/reviewed/ appraised
	minimum_rating = Column(Float,  default=0.0)
	maximum_rating = Column(Float, default=4.0)
	#start_date = Column(Date, nullable=True)
	#end_date = Column(Date, nullable=True)
	
	department_target = relationship("DepartmentTarget", backref="staff_targets")
	staff = relationship("Staff", backref="staff_targets",
                         foreign_keys="StaffTarget.staff_id")
	supervisor = relationship("Staff", backref="supervisee_targets",
                               foreign_keys="StaffTarget.supervisor_id")
							   
	def __str__(self):
		return self.title

    
class DepartmentAppraisal(APIBase):
    
    quality_score = Column(Float, default=0.0)
    efficiency_score = Column(Float, default=0.0)
    timeliness_score = Column(Float, default=0.0)
    accuracy_score = Column(Float, default=0.0)
    evaluator_remarks = Column(Text, nullable=True)
    department_remarks = Column(Text, nullable=True) 	 	
    date_recorded = Column(Date)
    rating_status_id =Column(String(50)) 
    
    evaluator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    review_period_id = Column(UUID, ForeignKey("review_periods.id"), nullable=True)
    department_target_id = Column(UUID, ForeignKey("department_targets.id"), nullable=True)
    
    evaluator = relationship("Staff", backref="department_appraisals")
    review_period = relationship("ReviewPeriod", backref="department_appraisals")
    department_target = relationship("DepartmentTarget", backref="department_appraisals")


class StaffAppraisal(APIBase):
	
	quality_score = Column(Float, default=0.0)
	efficiency_score = Column(Float, default=0.0)
	timeliness_score = Column(Float, default=0.0)
	accuracy_score = Column(Float, default=0.0)
	staff_remarks = Column(Text, nullable=True)
	evaluator_remarks = Column(Text , nullable=True)
	review_year =  Column(Integer)
	status = Column(String(25)) #draft , final ,review, appraised
	staff_id = Column(UUID, ForeignKey("staffs.id") )
	staff_target_id = Column(UUID, ForeignKey("staff_targets.id") )
	evaluator_id = Column(UUID, ForeignKey("staffs.id") )
	review_period_id = Column(UUID, ForeignKey("review_periods.id"))
 
	staff = relationship("Staff", backref="appraisals",
                      foreign_keys="StaffAppraisal.staff_id")
 
	evaluator = relationship("Staff", backref="reviewed_appraisals",
                      foreign_keys="StaffAppraisal.evaluator_id")
 
