from fastapi import APIRouter
from sqlalchemy import Session
from ..models import User
from ..schemas.user import UserCreate, UserUpdate
from app.utils.deps import get_db


user_router = APIRouter()


@user_router("/register")
def new_user(d ):
    pass


@user_router.post("/token")
def get_token(payload:Userchema,db:Session=Depends(get_db) )