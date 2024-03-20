from typing import Any, Dict, List, Optional, Union
from uuid import UUID
import datetime
from pydantic import BaseModel
from datetime import  datetime


class HTTPError(BaseModel):
    detail: str


# Shared properties
class PracticeAreaBase(BaseModel):
    title: Optional[str]  
    description: Optional[str] 
     
     
          
# Properties to receive via API on creation
class PracticeAreaCreate(PracticeAreaBase):
    title: str
    
    
# Properties to receive via API on update
class PracticeAreaUpdate(PracticeAreaBase):
    
    pass


class PracticeAreaInDBBase(PracticeAreaBase):
    id: Optional[UUID] = None
    title: str
    
    class Config:
        orm_mode = True


# Additional properties to return via API
class PracticeAreaSchema(PracticeAreaInDBBase):
    pass
    

       