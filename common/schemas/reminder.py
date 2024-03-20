from pydantic import BaseModel, UUID4
from typing import Optional
#from app.domains.schemas.action import ActionSchema

class ReminderBase(BaseModel):
    reminder_type: Optional[str] = None
    reminder_time: Optional[int] = None


# Properties to receive via API on creation
class ReminderCreate(ReminderBase):
    reminder_type: str
    reminder: int


# Properties to receive via API on update
class ReminderUpdate(ReminderBase):
   pass


class ReminderInDBBase(ReminderBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ReminderSchema(ReminderInDBBase):
    reminder: str
    reminder_time: int 
#    actions = List[ActionSchema] = []

# Additional properties stored in DB
class ReminderInDB(ReminderInDBBase):
    pass
