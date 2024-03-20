from typing import Optional, List
from pydantic import UUID4, BaseModel
from .permission import PermissionSchema

# Shared properties
class RoleBase(BaseModel):
    title: Optional[str] = None 
    description: Optional[str] = None  
    default: Optional[bool] = False


# Properties to receive via API on creation
class RoleCreate(RoleBase):
    title: str


# Properties to receive via API on update
class RoleUpdate(RoleBase):
    pass


class RoleInDBBase(RoleBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class RoleSchema(RoleInDBBase):
    permissions: Optional[ List[PermissionSchema]] = []
