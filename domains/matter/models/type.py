from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Type(APIBase):
    name = Column(String(250))
    description = Column(String(250))
    matters = relationship("Matter", secondary="matters_types", 
                                  	back_populates="types")
    def __str__(self):
        return self.name

