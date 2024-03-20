from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import StaffSchema


class HTTPError(BaseModel):
    detail: str


# Shared properties
class LeaveTypeBase(BaseModel):
    name: Optional[str] = None
    allocated_days: Optional[int] = 0 


# Properties to receive via API on creation
class LeaveTypeCreate(LeaveTypeBase):
    name: str


# Properties to receive via API on update
class LeaveTypeUpdate(LeaveTypeBase):
   pass


class LeaveTypeInDBBase(LeaveTypeBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class LeaveTypeSchema(LeaveTypeInDBBase):
    pass