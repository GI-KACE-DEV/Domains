from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
from sqlalchemy import (Column, String, Text, )
from .utils import COUNTRIES
import time


def document_path(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" % ("docs", hash_, filename)


class Attachment(APIBase):

    attachment = Column(String(1500), nullable=False)
    # staff_id = Column(UUID, ForeignKey("staffs.id"))
    file_name = Column(String(1001), nullable=True, default="")
    file_path = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    # staff
    # staff = relationship("Staff", back_populates="attachments")

    # leads
    leads = relationship("Lead", secondary="leads_attachments",
                         back_populates="attachments")
    # accounts
    # accounts =  relationship("Account", secondary="accounts_attachments",
    #                          back_populates="attachments")

    # clients
    # clients = relationship("Client")

    def file_type(self):
        pass

    def get_file_type_display(self):
        pass
        # if self.attachment:
        #    return self.file_type()[1]
        # return None
