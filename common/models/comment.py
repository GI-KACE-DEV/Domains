from sqlalchemy import (
    Column, Integer, Date, DateTime, ForeignKey, Text, String
)
from sqlalchemy.orm import relationship

from app.db.base_class import APIBase, UUID


class CommentFile(APIBase):

    comment_id = Column(UUID, ForeignKey("comments.id"), nullable=False)
    file_name = Column(String(2000))

    comment = relationship("Comment", back_populates="files")

    def __str(self):
        return self.file_name


class Comment(APIBase):

    comment = Column(Text)
    commented_on = Column(DateTime, nullable=False)
    staff_id = Column(UUID, ForeignKey("staffs.id"))

    # staff
    commented_by = relationship("Staff", back_populates="comments")

    # action

    # lead
    leads = relationship("Lead", secondary="leads_comments",
                         back_populates="comments")

    # registration
    files = relationship("CommentFile", back_populates="comment")

    def __str__(self):
        return self.comment
