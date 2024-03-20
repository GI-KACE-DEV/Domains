from typing import List
from sqlalchemy import (Column, String, DateTime,Text,Boolean,Integer, Date,Table, ForeignKey )
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
from app.domains.common.models.document import Document
from app.domains.officemanager import VisitCategory  


class VisitStatus(APIBase):
    status = Column(String(20))
    description = Column(Text, nullable=True)
    expected_visitors = relationship("ExpectedVisitor",
                                     back_populates="status")

    #visit_entries = relationship("VisitEntry",
    #                             back_populates="status")


class ExpectedVisitor(APIBase):

    visitor_name = Column(String(250), nullable=False)
    visitor_email = Column(String(50), nullable=True)
    visitor_phone = Column(String(50), nullable=True)
    visit_purpose = Column(Text, nullable=True)
    visit_date = Column(DateTime)

    person_to_see_id = Column(UUID, ForeignKey("staffs.id"), nullable=False)
    visit_category_id = Column(UUID, ForeignKey("visit_categories.id"))
    office_area_id = Column(UUID, ForeignKey("office_areas.id"), nullable=True)
    visit_status_id = Column(UUID, ForeignKey("visit_statuses.id"))

    # staff
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    created_by = relationship(
                "Staff",
                back_populates="expected_visitors_created",
                foreign_keys="ExpectedVisitor.creator_id")

    updated_by = relationship(
                 "Staff",
                 back_populates="expected_visitors_updated",
                 foreign_keys="ExpectedVisitor.updator_id")

    person_to_see = relationship(
                    "Staff",
                    back_populates="expected_visitors",
                    foreign_keys="ExpectedVisitor.person_to_see_id")

    office_area = relationship("OfficeArea",
                               back_populates="expected_visitors")

    status = relationship("VisitStatus", back_populates="expected_visitors")
    visit_category = relationship("VisitCategory",
                                  back_populates="expected_visitors")

    def __str__(self):
        return self.visitor_name
