from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Entry(APIBase):
    
    title = Column(String(250))
    description = Column(Text, nullable=True)
    matter_id = Column(UUID, ForeignKey("matters.id"))
    phase_code_id = Column(UUID, ForeignKey("phase_codes.id"), nullable=True)
    activity_code_id = Column(UUID, ForeignKey("activity_codes.id"), nullable=True)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True) 
    date = Column(Date, nullable=True) 

    
    #matter
    matter = relationship("Matter",  back_populates="entries")

    def __str__(self):
        return self.title