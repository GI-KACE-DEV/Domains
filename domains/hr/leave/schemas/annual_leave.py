from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import StaffSchema
from app.domains.hr.leave.schemas.leave_type import LeaveTypeSchema

class HTTPError(BaseModel):
    detail: str


# Shared properties
class AnnualLeaveBase(BaseModel):

    staff_id: Optional[UUID4] = None
    leave_type_id: Optional[UUID4] = None 
    allocated_days: Optional[int] = 0
    allocation_date: Optional[date] = None
    

# Properties to receive via API on creation
class AnnualLeaveCreate(AnnualLeaveBase):
    
    staff_id: Optional[UUID4] 
    leave_type_id: Optional[UUID4] 
    allocated_days: Optional[int] 
    allocation_date: Optional[date]
    

# Properties to receive via API on update
class AnnualLeaveUpdate(AnnualLeaveBase):
    pass
    

class AnnualLeaveInDBBase(AnnualLeaveBase):
    
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True

# Additional properties to return via API
class AnnualLeaveSchema(AnnualLeaveInDBBase):
    
    leave_type: Optional[LeaveTypeSchema]
    staff: Optional[StaffSchema] 

