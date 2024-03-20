from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class PhaseCode(APIBase):
    name = Column(String(150))
    description = Column(String, nullable=True)
    code = Column(String, unique=True, index=True)
    
    expenses = relationship("Expense",  back_populates="phase_code")

    
    def __str__(self):
        return "{self.name} {self.code}"
