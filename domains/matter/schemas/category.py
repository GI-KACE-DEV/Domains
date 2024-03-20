from pydantic import BaseModel, UUID4
from typing import Optional, List

from app.domains.matter.schemas.matter import MatterSchema


# Shared properties
class CategoryBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    
# Properties to receive via API on creation
class CategoryCreate(CategoryBase):
    name: str
  

# Properties to receive via API on update
class CategoryUpdate(CategoryBase):
    pass

class CategoryInDBBase(CategoryBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class CategorySchema(CategoryInDBBase):

    matters = Optional[List[MatterSchema]]

# Additional properties stored in DB
class CategoryInDB(CategoryInDBBase):
    pass