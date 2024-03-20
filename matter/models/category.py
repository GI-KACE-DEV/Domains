from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class Category(APIBase):
    name = Column(String(250))
    description = Column(String(200))
    
    matters = relationship("Matter", secondary="matters_categories", 
                                  	back_populates='categories')

    def __str__(self):
        return self.name
