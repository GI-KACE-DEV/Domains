from sqlalchemy import (Column, DateTime, Boolean,String)
from app.db.base_class import APIBase


class Email(APIBase):

    from_email = Column(String , nullable=False)
    to_email =Column(String(250))
    subject = Column(String(200))
    message = Column(String(200))
    file = Column(String(1200), nullable=True,default="")
    send_time = Column(DateTime, )
    status = Column(max_length=200, default="sent") #draft, sent ,
    important = Column(Boolean, default=True)


    def __str__(self):
        return self.subject
