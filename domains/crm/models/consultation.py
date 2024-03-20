from sqlalchemy import (
    Column, Integer, String, ForeignKey, Numeric, Date, Table,
    Boolean, DateTime, Text, UniqueConstraint
)
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID, Base
from app.domains.common.models.practice_area import PracticeArea
from app.domains.common.models.sector import Sector


consultations_staffs = Table(
    'consultations_staffs', Base.metadata,
    Column('consultation_id', UUID, ForeignKey(
        'consultations.id'), primary_key=True),
    Column('staffs_id', UUID, ForeignKey('staffs.id'), primary_key=True)
)

consultations_sectors = Table(
    'consultations_sectors', Base.metadata,
    Column('consultation_id', UUID, ForeignKey('consultations.id')),
    Column('sector_id', UUID, ForeignKey('sectors.id'))
)


consultations_practice_areas = Table(
    'consultations_practice_areas', Base.metadata,
    Column('consultation_id', UUID, ForeignKey('consultations.id')),
    Column('practice_areas_id', UUID, ForeignKey('practice_areas.id'))
)


consultations_actions = Table(
    'consultations_actions', Base.metadata,
    Column('consultation_id', UUID, ForeignKey('consultations.id')),
    Column('action_id', UUID, ForeignKey('actions.id'))
)


consultations_actions = Table(
    'consultations_contacts', Base.metadata,
    Column('consultation_id', UUID, ForeignKey('consultations.id')),
    Column('contact_id', UUID, ForeignKey('contacts.id'))
)


class ConsultationStatus(APIBase):

    status = Column(String(25))

    def __str__(self):
        return self.status


class Consultation(APIBase):

    client_id = Column(UUID, ForeignKey("clients.id"), )
    title = Column(String(250))
    brief = Column(Text, nullable=Text)
    remarks = Column(Text, nullable=True)

    # estimated_value = Column(String(500), nullable=True)
    # probability = Column(String(50), nullable=True, default=0.0)

    estimated_value = Column(Numeric, nullable=True)
    probability = Column(Numeric, nullable=True, default=0.0)
    consulting_fee = Column(Numeric, nullable=True, default=0.0)
    is_paid = Column(Boolean, default=False)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)

    lead_counsel_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    # booked,  accepted, completed, closed_onboarded, closed_discontinued
    # expired
    status = Column(String(20), default="")

    # sectors
    sectors = relationship("Sector", secondary="consultations_sectors",
                           back_populates="consultations")
    # practice_area
    practice_areas = relationship("PracticeArea", secondary="consultations_practice_areas",
                                  back_populates="consultations")

    # staff
    assigned_to = relationship("Staff", secondary="consultations_staffs",
                               back_populates="assigned_consultations")

    lead_counsel = relationship("Staff", back_populates="consultations_led",
                                foreign_keys="Consultation.lead_counsel_id")

    created_by = relationship("Staff", back_populates="consultations_created",
                              foreign_keys="Consultation.creator_id")

    updated_by = relationship("Staff", back_populates="consultations_updated",
                              foreign_keys="Consultation.updator_id")

    # contacts
    contacts = relationship("Contact", secondary="consultations_contacts",
                            back_populates="consultations")

    # client
    client = relationship("Client", back_populates="consultations")

    # action
    actions = relationship("Action", secondary="consultations_actions",
                           back_populates="consultations")

    def __str__(self):

        return f" {self.title } ({self.account} ) "
