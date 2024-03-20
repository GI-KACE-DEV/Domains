from typing import List
from sqlalchemy import (Column, String, DateTime, Text,Boolean,Integer, Date, 
                            Table, ForeignKey )
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
from .expected_visitor import (ExpectedVisitor, VisitStatus)
from .utils import OfficeArea, VisitCategory
from app.domains.officemanager.models.visitor import Visitor

class VisitEntry(APIBase):
    
    #salutation = Column(String(20), nullable = True)
    #first_name = Column(String(500), nullable=False)
    #last_name = Column(String(500), nullable=True)
    #email = Column(String(100), nullable=True)
    #visitor_phone_number = Column(String(50), nullable=True)
    #place_from = Column(String(500), nullable=True)
    #company = Column(String(500), nullable=True)
    #company_contact_name = Column(String(100), nullable=True)
    #company_primary_phone = Column(String(100))
    #company_secondary_phone = Column(String(100), nullable=True)
    
    purpose_of_visit = Column(Text)
    person_to_see_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    office_area_id = Column(UUID, ForeignKey("office_areas.id"), nullable=False)
    visitor_id =  Column(UUID, ForeignKey("visitors.id"), nullable=True) 
    visit_category_id =  Column(UUID, ForeignKey("visit_categories.id"), nullable=True)
    place_from = Column(String(500), nullable=True)
    visitor_tag_code = Column(String(20), nullable=False)
    visit_date = Column(Date)
    time_in = Column(DateTime, nullable=True)
    time_out = Column(DateTime, nullable=True)
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    
    created_by = relationship("Staff", 
                              back_populates="visit_entries_created",
                              foreign_keys="VisitEntry.creator_id")
    
    updated_by = relationship( "Staff", 
                              back_populates="visit_entries_updated",
                              foreign_keys="VisitEntry.updator_id")    
      
    person_to_see = relationship("Staff", back_populates="received_visits",
                              foreign_keys="VisitEntry.person_to_see_id")    
    
    
    visitor = relationship("Visitor", back_populates="visit_entries",)    
    office_area = relationship("OfficeArea", back_populates="visit_entries")    
    visit_category = relationship("VisitCategory", back_populates="visit_entries")    


    def __str_(self):
        return f"{self.first_name} {self.last_name}"