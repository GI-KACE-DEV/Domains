from pydantic import BaseModel, UUID4
from typing import Optional, List


# Shared properties
class DocumentBase(BaseModel):
    
    title: Optional[str] = None 
    description: Optional[str] = None
    reference_number: Optional[str] = None 
    version: Optional[str] = None
    path: Optional[str] = None
    


# Properties to receive via API on creation
class DocumentCreate(DocumentBase):
    title: str
    description: str

# Properties to receive via API on update
class DocumentUpdate(DocumentBase):
    pass

class DocumentInDBBase(DocumentBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class DocumentSchema(DocumentInDBBase):
    pass

# Additional properties stored in DB
class DocumentInDB(DocumentInDBBase):
    pass




