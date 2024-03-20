from sqlalchemy import (Column, String, ForeignKey, Text )
from app.db.base_class import APIBase, UUID


class Google(APIBase):
    
    google_id = Column(String(200), nullable=False, default="")
    google_url = Column(Text, nullable=False, default="")
    verified_email = Column(String(100), default="")
    family_name = Column(String(200), default="")
    name = Column(String(200), default="")
    gender = Column(String(10), default="")
    dob = Column(String(50), default="")
    given_name = Column(String(200), default="")
    email = Column(String(200), default="", db_index=True)

    #user = models.ForeignKey(
    #    User, related_name="google_user", on_delete=models.CASCADE, null=True
    #)

    
    def __str__(self):
        return self.email