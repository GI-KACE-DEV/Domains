from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Expense(APIBase):
    
    description = Column(String(20))
    matter_id = Column(UUID, ForeignKey("matters.id"))
    expense_code_id = Column(UUID, ForeignKey("expense_codes.id"))
    phase_code_id = Column(UUID, ForeignKey("phase_codes.id"), nullable=True)
    amount = Column(Numeric, default=0.0)
    date = Column(Date)
    responsible = Column(UUID, ForeignKey("staffs.id"))

    phase_code = relationship("PhaseCode",  back_populates="expenses")
    matter = relationship("Matter",  back_populates="expenses")


    def _str__(self):
        return self.description
