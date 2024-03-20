from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class EntryState(APIBase):
    state = Column(String(20))
    description = Column(String(5000), nullable=True)

    def __str__(self):
        return self.state
