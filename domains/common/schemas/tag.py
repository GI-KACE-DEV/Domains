from typing import Any, Dict, List, Optional, Union
from uuid import UUID
import datetime
from pydantic import BaseModel
from datetime import  datetime
#import app.domains.crm.schemas.lead



class TagBase(BaseModel):
    name: Optional[str] = None


# Properties to receive via API on creation
class TagCreate(TagBase):
    name: str


# Properties to receive via API on update
class TagUpdate(TagBase):
   pass


class TagInDBBase(TagBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class TagSchema(TagInDBBase):
    name: str
    #leads = List[lead.LeadSchema] = []

