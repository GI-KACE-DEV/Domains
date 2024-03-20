from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.common.schemas.comment import CommentSchema
from app.domains.matter.schemas.phase_code import PhaseCodeSchema
from app.domains.matter.schemas.matter import MatterSchema


#Notification
class NotificationBase(BaseModel):
   
    title: Optional[str] =  None
    content: Optional[str] = None
    status = Optional[str]  = None
     
# Properties to receive via API on creation
class NotificationCreate(NotificationBase): 
    
    matter_id: UUID4
    title: str 
    body: str 
    date: date
    authour_id: UUID4  

     
# Properties to receive via API on update
class NotificationUpdate(NotificationBase):
   pass


class NotificationInDBBase(NotificationBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class NotificationSchema(NotificationInDBBase):
    
    matter: Optional[MatterSchema] = None 
