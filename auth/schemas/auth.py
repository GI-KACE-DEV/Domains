from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
#from  hr.staff.schemas import StaffSchema
from .user import UserSchema, UserBase

class Auth(UserBase):
    password: str


class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: UserSchema

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: Optional[str]
    refresh_token: Optional[str]


class RevokedTokenSchema(BaseModel):
    id: UUID4
    jti: str

    class Config:
        orm_mode = True
    

class EmailSchema(BaseModel):
    email: EmailStr


class Notice(EmailSchema):
    message_subject: str
    message_body:str