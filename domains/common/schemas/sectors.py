from typing import Any, Dict, List, Optional, Union
from uuid import UUID
import datetime
from pydantic import BaseModel
from datetime import  datetime


class HTTPError(BaseModel):
    detail: str


# Shared properties
class SectorBase(BaseModel):
    title: Optional[str]  
    description: Optional[str] 
     
     
          
# Properties to receive via API on creation
class SectorCreate(SectorBase):
    title: str
    
    
# Properties to receive via API on update
class SectorUpdate(SectorBase):
    
    pass


class SectorInDBBase(SectorBase):
    id: Optional[UUID] = None
    title: str
    
    class Config:
        orm_mode = True


# Additional properties to return via API
class SectorSchema(SectorInDBBase):
    pass
    

       