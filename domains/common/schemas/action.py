from typing import Any, Dict, List, Optional, Union
from uuid import UUID
import datetime
from pydantic import BaseModel
from datetime import  datetime

from  app.domains.common.schemas.reminder import ReminderSchema
from app.domains.hr.staff.schemas import StaffSchema
from app.domains.hr.staff.schemas import TeamSchema


class HTTPError(BaseModel):
    detail: str


#status
class StatusBase(BaseModel):
   status: Optional[str] 
   description: Optional[str]
   
   
# Properties to receive via API on creation
class StatusCreate(StatusBase):
   status: str
   description: Optional[str]
   

# Properties to receive via API on update
class StatusUpdate(StatusBase):
   pass


class StatusInDBBase(StatusBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class StatusSchema(StatusInDBBase):
    status: str
    description: int 

# Additional properties stored in DB
class StatusInDB(StatusInDBBase):
    pass



# Shared properties
class ActionBase(BaseModel):
    
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    start_date_time: Optional[datetime] = None
    close_date_time: Optional[datetime] = None
    duration: Optional[int] = None
    is_active:  Optional[bool] = True    
    status_id: Optional[UUID] = None
    assigned_users_ids: List[UUID] = []
   
   
    
# Properties to receive via API on creation
class ActionCreate(ActionBase):
    name: str
    start_date_time: datetime
    
    
# Properties to receive via API on update
class ActionUpdate(ActionBase):
    #name: Optional[str] = None
    #start_date_time: Optional[datetime] = False
    pass


class ActionInDBBase(ActionBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ActionSchema(ActionInDBBase):
   
    reminders:  List[ReminderSchema]  = []
    staff_attendees: List[StaffSchema]  = []
    contacts:  List[StaffSchema] = []
    teams:  List[TeamSchema] = []
    assigned_users:  List[StaffSchema] = []
    #tags:  List[TagSchema] = []


class ActionSchemaRelatedIds(ActionInDBBase):
    
    team_ids: Optional[List[UUID]] = []
    contacts: Optional[List[UUID]] = []
    reminders: Optional[List[UUID]] = [] 
    staff_attendees: Optional[List[UUID]] = []
    assigned_users: Optional[List[UUID]] = []
    team_ids: Optional[List[UUID]] = []
    

# Additional properties stored in DB
class ActionInDB(ActionInDBBase):
  
    pass