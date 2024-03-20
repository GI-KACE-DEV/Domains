from typing import Any, Dict, List, Optional, Union
from uuid import UUID
import datetime
from pydantic import BaseModel
#from datetime import  datetime
#from  app.domains.hr.staff.schemas import StaffSchema


class HTTPError(BaseModel):
    detail: str


# Shared properties
class DocumentBase(BaseModel):
    
    title: Optional[str] = None
    description: Optional[str] = None
    document_file: Optional[str] = None
    
   
      
# Properties to receive via API on creation
class DocumentCreate(DocumentBase):
    
    title: str
    description: str
    document_file: UUID
    
    
# Properties to receive via API on update
class DocumentUpdate(DocumentBase):
   
    pass


class DocumentInDBBase(DocumentBase):
    id: Optional[UUID] = None
    document_file: str
    title: str

    class Config:
        orm_mode = True



        
# Additional properties stored in DB
class DocumentInDB(DocumentInDBBase):
    pass

# Additional properties to return via API
class DocumentSchema(DocumentInDBBase):
   pass 
   