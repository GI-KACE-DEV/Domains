from pydantic import BaseModel , EmailStr
from typing import Optional, List
from pydantic import UUID4
from .role import RoleSchema
from .permission import PermissionSchema
from app.domains.hr.staff.schemas import StaffSchema

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None 
    staff_id: Optional[UUID4] = None        
    status: Optional[bool] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str
    staff_id: UUID4


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserSchema(UserInDBBase):

    #related objects
    roles: Optional[List[RoleSchema]]
    permissions: Optional[ List[PermissionSchema]]
    staff: StaffSchema

