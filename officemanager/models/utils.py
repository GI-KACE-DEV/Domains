from typing import List
from sqlalchemy import (Column, String, Text,Boolean,Integer, Date,Table, ForeignKey )
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
from app.db.base_class import Base
from app.domains.common.models.document import Document


class OfficeArea(APIBase):

    name = Column(String(250), unique=True)
    code = Column(String(20), unique=True, nullable=True, default=None)
    description = Column(Text, nullable=True)

    def __str(self):
        return f'{self.name}/{self.code}'

    visit_entries = relationship("VisitEntry", back_populates="office_area")
    expected_visitors = relationship("ExpectedVisitor", back_populates="office_area")


class VisitCategory(APIBase):
    category = Column(String(25))
    description = Column(Text, nullable=True)

    def __str__(self):
        return self.category

    visit_entries = relationship("VisitEntry", back_populates="visit_category")
    expected_visitors = relationship("ExpectedVisitor", back_populates="visit_category")
