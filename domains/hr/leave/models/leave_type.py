from sqlalchemy import  Column, Integer, String, Date, Boolean, func, extract, ForeignKey
from sqlalchemy.orm import  relationship
from datetime import date, timedelta
#from app.db.base import Base
from app.db.base_class import APIBase, UUID


class LeaveType(APIBase):
    
    #__tablename__ = "leave_types"
    name = Column(String, unique=True)
    allocated_days = Column(Integer, nullable=True, default=0)

