from typing import Any, Dict, List, Optional, Union
from datetime import datetime , date
from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.common.schemas.comment import CommentSchema
from app.domains.matter.schemas.matter import MatterSchema



# Properties to receive via API on creation
class TrialBase(BaseModel):
    case_id: Optional[UUID4] = None      
    court: Optional[UUID4] = None
    judge: Optional[str] = None
    notes = Optional[str] = None
    remarks: Optional[str] = None
    date = Optional[datetime] = NotImplementedError
    next_hearing_date: Optional[datetime] = None

#create 
class TrialCreate(TrialBase):
    name: str
    code: str


# Properties to receive via API on update
class TrialUpdate(TrialBase):
    pass


class TrialInDBBase(TrialBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class TrialSchema(TrialInDBBase):
    pass


# Additional properties stored in DB
class TrialInDB(TrialInDBBase):
    pass
