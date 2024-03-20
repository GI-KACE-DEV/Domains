from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class District(APIBase):   
    region_id = Column(UUID, ForeignKey("regions.id"))
    name = Column(String(50))
    code = Column(String(5), nullable=True)
    
    courts = relationship("Court", back_populates="district")


    def __str__(self):
        return f"{self.name}"
