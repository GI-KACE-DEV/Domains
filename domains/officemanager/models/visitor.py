from typing import List
from sqlalchemy import (Column, String, DateTime, Text,Boolean,Integer, Date, 
                            Table, ForeignKey )
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
from .expected_visitor import (ExpectedVisitor, VisitStatus)
from .utils import OfficeArea, VisitCategory


class Visitor(APIBase):
    
    salutation = Column(String(20), nullable = True)
    first_name = Column(String(500), nullable=False)
    last_name = Column(String(500), nullable=True)
    email = Column(String(100), nullable=True)
    phone = Column(String(25), nullable=True)

    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    
    
    created_by = relationship("Staff", 
                              back_populates="visitors_created",
                              foreign_keys="Visitor.creator_id")
    
    updated_by = relationship( "Staff", 
                                back_populates="visitors_updated",
                              foreign_keys="Visitor.updator_id")    
      
    visit_entries = relationship("VisitEntry", back_populates="visitor")    


    def __str_(self):
        return f"{self.first_name} {self.last_name}"