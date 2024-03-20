from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime

class Notification(APIBase):
    title = Column(String)
    content = Column(Text)
    status = Column(String(10))
    
    def __str__(self):
        return self.title