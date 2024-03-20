from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Opposing(APIBase):

    opposing_type = Column(String(10)) #party /lawyer
    matter_id = Column(UUID, ForeignKey("matters.id"))
    first_name = Column(String(150))
    last_name = Column(String(150))
    description = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    phone = Column(String(40), nullable=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

  #  opposing = relationship("Matter", back_populates="opposing")
