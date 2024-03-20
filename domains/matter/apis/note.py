from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Note(APIBase):
    
    matter_id = Column(UUID, ForeignKey("matters.id"))
    title = Column(String(500),null=True)
    body = Column(Text)
    date  = Column(Date)
    authour_id = Column(UUID, ForeignKey("staffs.id"))
    
    matter = relationship("Matter",  back_populates="notes")

    
    def __str__(self):
        return f"{self.title}"