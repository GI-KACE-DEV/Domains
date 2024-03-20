from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import StaffSchema
from app.domains.hr.leave.schemas.leave_type import LeaveTypeSchema


class HTTPError(BaseModel):
    detail: str


# Shared properties
class LeaveBase(BaseModel):

    staff_id: Optional[UUID4] = None 
    leave_type_id: Optional[UUID4] = None 
    start_date: Optional[date]  = None
    end_date: Optional[date] = None
    is_approved: Optional[bool] = False
    status: Optional[str] = "pending"
    

# Properties to receive via API on creation
class LeaveCreate(LeaveBase):
    staff_id: UUID4
    leave_type_id: UUID4
    start_date: date
    end_date: date
   

# Properties to receive via API on update
class LeaveUpdate(LeaveBase):
   pass


class LeaveInDBBase(LeaveBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class LeaveSchema(LeaveInDBBase):
    
    leave_type: LeaveTypeSchema
    staff: StaffSchema