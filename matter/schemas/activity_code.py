from pydantic import BaseModel, UUID4
from typing import Optional, List
from datetime import date, datetime

class HTTPError(BaseModel):
    detail: str


#ActivityCode
class ActivityCodeBase(BaseModel):
    
    name: Optional[str]  = None
    description: Optional[str] = None 
    code:Optional[str] = None


# Properties to receive via API on creation
class ActivityCodeCreate(ActivityCodeBase): 
    name: str  
    description: str 
    code: str 
    
    
# Properties to receive via API on update
class ActivituUpdate(ActivityCodeBase):
   pass


class ActivityCodeInDBBase(ActivityCodeBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ActivityCodeSchema(ActivityCodeInDBBase):

    pass
    
   