from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Judge(APIBase):
    first_name = Column(String(250))
    last_name = Column(String(250))

    def __str__(self):
        return f"{self.first_name}  {self.other_names}"

