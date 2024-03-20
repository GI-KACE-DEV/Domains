from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime

from matter import Matter   
from app.domains.matter.models import  action
from app.domains.matter.models import matter
    

class Case(APIBase):
    
    matter_id = Column(UUID, ForeignKey("matters.id"))
    suite_number = Column(String(500))
    title = Column(Text)
    brief = Column(Text)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    status = Column(String(20), default="pending")

    matter = relationship("Matter",  back_populates="cases")   
    courts = relationship("Court", secondary="cases_courts", 
                                  	back_populates="cases")

    def __str__(self):
        return self.title


