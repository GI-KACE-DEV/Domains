from typing import Optional, List
from pydantic import UUID4, BaseModel


# Shared properties
class PermissionBase(BaseModel):
    title: Optional[str] = None 
    desription: Optional[str] = None  


# Properties to receive via API on creation
class PermissionCreate(PermissionBase):
    title: str


# Properties to receive via API on update
class PermissionUpdate(PermissionBase):
    pass


class PermissionInDBBase(PermissionBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class PermissionSchema(PermissionInDBBase):
    pass