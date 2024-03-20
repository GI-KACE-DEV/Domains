from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Trial(APIBase): #hearing
    case_id = Column(UUID, ForeignKey("cases.id"))      
    court = Column(UUID, ForeignKey("courts.id"))
    judge = Column(String(1200), nullable=True)
    notes = Column(Text, nullable=True)#court notes
    remarks = Column(Text, nullable=True)
    date = Column(DateTime)
    next_hearing_date = Column(DateTime,nullable=True)

    def __str__(self):
        return f"self.notes"


class HearingRemarks:
    pass