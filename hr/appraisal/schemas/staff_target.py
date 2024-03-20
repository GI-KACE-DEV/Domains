from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from .review_period import ReviewPeriodSchema
from .department_target import DepartmentTargetSchema

class HTTPError(BaseModel):
    detail: str
    
    
# Shared properties
class StaffTargetBase(BaseModel):
    
    title: Optional[str] = None
    description: Optional[str] = None
    staff_id: Optional[UUID4] = None
    department_target_id: Optional[UUID4] = None
    supervisor_id: Optional[UUID4] = None 
    success_indicator: Optional[str] = None	 
    minimum_rating: Optional[float] = 0.0
    maximum_rating: Optional[float] = 1
    #start_date: Optional[date] = None
    #end_date: Optional[date] = None
    employee_remarks: Optional[str] = None

    supervisor_remarks: Optional[str] = None
    status: Optional[str] = None #opened/ finalized/reviewed/ appraised

    

# Properties to receive via API on creation
class StaffTargetCreate(StaffTargetBase):
    title: str
    department_target_id: UUID4
    staff_id: UUID4

    
# Properties to receive via API on update
class StaffTargetUpdate(StaffTargetBase):
   pass


class StaffTargetInDBBase(StaffTargetBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class StaffTargetSchema(StaffTargetInDBBase):
   review_period: Optional[ReviewPeriodSchema]
   department_target : Optional[DepartmentTargetSchema]