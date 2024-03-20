from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import User
from ..schemas.user import UserCreate, UserUpdate, UserSchema
from app.utils.deps import get_db


user_router = APIRouter()

#create new user
@user_router.post("/register")
async def register(d ):
    pass


#get token
@user_router.post("/token")
async def get_token(payload:UserSchema,db:Session=Depends(get_db)):
    pass

#refresh token
@user_router.post("/refresh")
async def get_token(payload:UserSchema,db:Session=Depends(get_db)):
    pass

#login
@user_router.post("/login")
async def get_token(payload:UserSchema,db:Session=Depends(get_db) ):
    pass

#logout
@user_router.post("/logout")
async def get_token(payload:UserSchema,db:Session=Depends(get_db)):
    pass


