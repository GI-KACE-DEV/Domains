from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Court(APIBase):
    name = Column(String(250))
    location = Column(String(500))
    district_id = Column(UUID, ForeignKey("districts.id"))
    email = Column(String(250), nullable=True)
    phone = Column(String(20), nullable=True)

    district = relationship("District", back_populates="courts")
    
    matters = relationship("Matter", secondary="matters_courts", 
                                  	back_populates="courts")
    
    cases = relationship("Case", secondary="cases_courts", 
                                  	back_populates="courts")
    
    def __str__(self):
        
        return self.name

