from sqlalchemy import (Column, String)
from sqlalchemy.orm import relationship
from app.db.base_class import UUID, APIBase


class Tag(APIBase):
    name = Column(String(50))

    def __str__(self):
        return f"{self.name}"

    # leads
    leads = relationship("Lead", secondary="leads_tags", back_populates="tags")

    # consultations

    # clients

    # briefs

    # litigation

    # transactions
