from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class TaskCode(APIBase):
    name = Column(String(150))
    description = Column(String, nullable=True)
    code = Column(String, unique=True, index=True)

    def __str__(self):
        return f"{self.name} {self.code}"
                                                                                  