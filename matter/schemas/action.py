from pydantic import BaseModel, UUID4
from typing import Optional, List
from datetime import date, datetime


class HTTPError(BaseModel):
    detail: str


# Shared properties
class ActionBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    date: Optional[str] = None
    status: Optional[str] = None  #draft, assigned , in progress , cancelled , complted


# Properties to receive via API on creation
class ActionCreate(ActionBase):
    title: Optional[str] 
    description: Optional[str] 
    notes: Optional[str] 
    date: Optional[date] = None
    action_type: Optional[str] = None


# Properties to receive via API on update
class ActionUpdate(ActionBase):
   assigned_to: Optional[List[UUID4] ] = []
   status: Optional[str] = None  #draft, assigned , in progress , cancelled , completed


class ActionInDBBase(ActionBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ActionSchema(ActionInDBBase):

    assigned_to:Optional[List[UUID4]] = []

# Additional properties stored in DB
class ActionInDB(ActionInDBBase):
    pass