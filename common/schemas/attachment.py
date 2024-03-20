from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema) 

class HTTPError(BaseModel):
    detail: str


#Attachment
class AttachmentBase(BaseModel):
    attachment: Optional[str] = None
    file_name: Optional[str] 
    description: Optional[str] = None
    staff_id: Optional[UUID4] = None
            
      
# Properties to receive via API on creation
class AttachmentCreate(AttachmentBase):  
           
    file_name: str
    staff_id: Optional[UUID4] = None
    

                               
# Properties to receive via API on update
class AttachmentUpdate(AttachmentBase):
   pass


class AttachmentInDBBase(AttachmentBase):
    id: Optional[UUID4] = None
    staff_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class AttachmentSchema(AttachmentInDBBase):
    staff: Optional[UUID4] = None 
    leads: Optional[List[UUID4]]    = []
    created_by: Optional[StaffSchema] 
    updated_by: Optional[StaffSchema] 


   
    