from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID


class File(APIBase):

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    path = Column(String)
    folder_id = Column(UUID, ForeignKey("folders.id"))

    folder = relationship("Folder", back_populates="files")

    def __str__(self):
        pass