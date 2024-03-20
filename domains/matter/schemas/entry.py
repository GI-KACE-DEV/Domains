from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date

from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.matter.schemas import MatterSchema



#Entry
class EntryBase(BaseModel):
    
    matter_id: Optional[UUID4] = None 
    title: Optional[UUID4] = None
    description: Optional[str] = None
    activity_code_id:  Optional[UUID4] = None 
    activity_code_id:  Optional[UUID4] = None 
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    date: Optional[datetime.date] = None


# Properties to receive via API on creation
class EntryCreate(EntryBase): 
    matter_id: UUID4 | None
    activity_code_id:  Optional[str] = None 
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    
    
# Properties to receive via API on update
class EntryUpdate(EntryBase):
   pass


class EntryInDBBase(EntryBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class EntrySchema(EntryInDBBase):
    
    matters: List[Optional[MatterSchema]] = []
    
   