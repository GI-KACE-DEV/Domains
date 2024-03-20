from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


    
class Region(APIBase):
    name = Column(String(50))
    code = Column(String(5), unique=True)

    def __str__(self):
        return f"{self.name}"
