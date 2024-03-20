from app.db.base_class import APIBase
from sqlalchemy import (Column, String, Text, )
from sqlalchemy.orm import relationship
from .utils import COUNTRIES
# from app.domains.hr.staff.models import Staff


class Sector(APIBase):

    title = Column(String(50), nullable=True)
    description = Column(Text)

    staffs = relationship(
        "Staff", secondary="staff_sectors", back_populates='sectors')
    leads = relationship("Lead", secondary="leads_sectors",
                         back_populates="sectors")
    consultations = relationship(
        "Consultation", secondary="consultations_sectors", back_populates="sectors")

    # client =  relationship("Account", secondary="accounts_sectors", back_populates="sectors")
    # breifs

    def __str__(self):
        return self.title
