from sqlalchemy import (Column, String, DateTime, Boolean)
from datetime import datetime
from app.db.base_class import APIBase, UUID


class Message(APIBase):

    MESSAGE_STATUSES = (("sent", "sent"), ("draft", "draft"))

    from_email = Column(String(200))
    to_email = Column(String(200))
    subject = Column(String(200))
    message = Column(String(200))
    send_time = Column(DateTime, default=datetime.now)
    status = Column(String(20), default="sent")
    important = Column(Boolean, default=False)

    def __str__(self):
        return self.subject
