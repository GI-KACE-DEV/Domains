from app.db.base_class import APIBase
from sqlalchemy import (Column, String, Text, )
from sqlalchemy.orm import relationship
from .utils import COUNTRIES 


class PracticeArea(APIBase):
    
    title  = Column(String(50) , nullable=True)
    description = Column(Text , nullable=True)
     
     
    staffs = relationship("Staff", secondary="staffs_practice_areas", 
                          	back_populates='practice_areas')
    
    leads = relationship("Lead", secondary="leads_practice_areas", 
                                  	back_populates='practice_areas')
    
    consultations =  relationship("Consultation", secondary="consultations_practice_areas", 
                                  back_populates="practice_areas")

   
    
   # accounts = relationship("Account", secondary="accounts_practice_areas", 
   #                               	back_populates='practice_areas')
   
    
    def __str__(self):
      return self.title

