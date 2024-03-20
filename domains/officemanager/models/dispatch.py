from typing import List
from sqlalchemy import (Column, String, DateTime,Text,
                        Boolean,Integer, Date,Table, ForeignKey )
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
from app.db.base_class import Base
from app.domains.common.models.document import Document

associates_outgoings = Table(
    "associates_outgoings",  Base.metadata,
    Column("associate_id", UUID, ForeignKey("staffs.id"), primary_key=True),
    Column("outgoing_id", UUID, ForeignKey("outgoings.id"), primary_key=True)
)


class Incoming(APIBase):

    document_title = Column(String(2000), nullable=False)
    description = Column(Text, nullable=True, default=None)
    case_title = Column(Text, nullable=True)
    client = Column(String(1000), nullable=True)
    to_whom_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    delivered_to_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    receipt_acknowledged = Column(Boolean,nullable=False, default=False)
    sender_name = Column(String(500), nullable=True)
    courier_name = Column(String(500), nullable=True)
    courier_phone = Column(String(20), nullable=True)
    date = Column(DateTime)
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    created_by = relationship("Staff",
                              back_populates="incoming_documents_created",
                              foreign_keys="Incoming.creator_id")

    updated_by = relationship("Staff",
                              back_populates="incoming_documents_updated",
                              foreign_keys="Incoming.updator_id")

    received_by = relationship("Staff", back_populates="deliveries_received",
                               foreign_keys="Incoming.delivered_to_id")

    addressed_to = relationship("Staff",
                                 back_populates="incoming_documents",
                                 foreign_keys="Incoming.to_whom_id")
    

    def __str__(self):
        return f"{self.document_name}/{self.case_title}"


class Outgoing(APIBase):

    serial_no = Column(Integer, autoincrement=True)
    document_title = Column(String(250), nullable=False)
    typist_id = Column(UUID, ForeignKey("staffs.id"), nullable=False)
    reference_number = Column(String(24), unique=True, index=True)
    date = Column(Date, nullable=False)
    #document = Column(UUID, ForeignKey("documents.id"), nullable=True)

    # staff
    partner_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    typist_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=False)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    created_by = relationship("Staff",
                              back_populates="outgoing_documents_created",
                              foreign_keys="Outgoing.creator_id")

    updated_by = relationship("Staff",
                              back_populates="outgoing_documents_updated",
                              foreign_keys="Outgoing.updator_id")

    partner = relationship("Staff",
                           back_populates="authourized_outgoing_documents",
                           foreign_keys="Outgoing.partner_id")
    
    associates = relationship("Staff", secondary="associates_outgoings",
                              back_populates="associates_outgoing_documents")
    
    typist = relationship("Staff", back_populates="typed_outgoing_documents",
                          foreign_keys="Outgoing.typist_id")

    
    def __str__(self):
        return f"{self.filename}/{self.file_title}/{self.reference_number}"
    

    def initials(self,full_name):
        if len(full_name) == 0:
            return 
        initial = "".join([self.name[0].upper() for name in self.full_name.split(" ")])
        return initial


    def generate_initials(self, rslt: List):
        return "".join( [self.initials(item) for item in self.rslt] )


    def generate_serial(current):
        current += 1
        next_serial= f"{current:0>5.0f}"
        return next_serial


    def generate_reference_number(self,partners:List, associates:List, typist:str, current: int) -> str:
        partners = self.generate_initials(partners)
        associates = self.generate_initials(associates)
        serial = self.generate_serial(current)
        return f"{partners}/{associates}/{serial}"

