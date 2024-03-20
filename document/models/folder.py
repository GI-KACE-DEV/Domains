from fastapi import UploadFile, File,  HTTPException
from sqlalchemy import  Column,  String, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
import os


from app.crud.base import APIBase, UUID


# Create a model for the Folder
class Folder(APIBase):

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    version = Column(UUID)
    path = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    parent_folder_id = Column(UUID, ForeignKey("folders.id"), nullable=True)

    children = relationship("Folder", back_populates="parent_folder")
    parent_folder = relationship("Folder", remote_side=[id])


    def __str__(self):
        return self.name
