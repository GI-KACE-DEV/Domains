from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base
import datetime


class Document(APIBase):
    title = Column(String)
    description = Column(String, nullable=True)
    document_url = Column(String, nullable=True)
    folder_name = Column(String, nullable=True)
    date_created = Column(DateTime,  default=datetime.datetime.utcnow)
    date_modified = Column(DateTime,  default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __str__(self):
        return self.title