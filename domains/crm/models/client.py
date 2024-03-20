from sqlalchemy import (Column, Integer, String, ForeignKey, Numeric, Date, Table,
                        Boolean, DateTime, Text, UniqueConstraint)
import datetime
from sqlalchemy.orm import backref, relationship

from app.db.base_class import APIBase, UUID, Base
from app.domains.common.models.sector import Sector
from app.domains.common.models.tag import Tag
from app.domains.common.models.practice_area import PracticeArea


clients_tags = Table(
    'clients_tags', Base.metadata,
    Column('client_id', UUID, ForeignKey('clients.id'), primary_key=True),
    Column('tag_id', UUID, ForeignKey('tags.id'), primary_key=True)
)

relationship_managers = Table(
    'clients_staffs', Base.metadata,
    Column('client_id', UUID, ForeignKey('clients.id'), primary_key=True),
    Column('staffs_id', UUID, ForeignKey('staffs.id'), primary_key=True)
)


clients_contacts = Table(
    'clients_contacts', Base.metadata,
    Column('client_id', UUID, ForeignKey('clients.id'), primary_key=True),
    Column('contact_id', UUID, ForeignKey('contacts.id'), primary_key=True)
)


clients_actions = Table(
    'clients_actions', Base.metadata,
    Column('client_id', UUID, ForeignKey('clients.id')),
    Column('action_id', UUID, ForeignKey('actions.id'))
)


class ClientRegistration(APIBase):

    client_type = Column(String(12))  # individual or corporate
    client_name = Column(String(250))
    name_of_authourized_representative = Column(String(250))
    mailing_address = Column(String(5000))
    occupation = Column(String(150), nullable=True)  # individual
    principal_business_activity = Column(String(5000), nullable=True)
    names_of_directors_or_partners = Column(String)
    name_of_employer = Column(String(250), nullable=True)  # individual
    registered_office = Column(String(5000), nullable=True)  # corporate
    residential_address = Column(String(5000))  # individual
    tin_number = Column(String(40), unique=True)
    business_phone_number = Column(String(40), nullable=True)
    cellphone_number = Column(String(40), nullable=True)
    corporate_email = Column(String(100), nullable=True)
    personal_email = Column(String(100), nullable=True)
    opposing_party_name = Column(String(5000), nullable=True)
    opposing_party_lawyer = Column(String(5000), nullable=True)
    status = Column(String(10), nullable=False,
                    default="draft")  # processed/pendinig
    registration_date = Column(DateTime)

    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    created_by = relationship("Staff",
                              back_populates="client_registrations_created",
                              foreign_keys="ClientRegistration.creator_id")

    updated_by = relationship("Staff", foreign_keys="ClientRegistration.updator_id",
                              back_populates="client_registrations_updated")

    def __str__(self):
        return self.client_name


class Client(APIBase):

    client_type = Column(String(12))  # individual or corporate
    client_registration_number = Column(String(20), unique=True, nullable=True)
    client_name = Column(String(250))
    name_of_authourized_representative = Column(String(250))
    mailing_address = Column(String(5000))
    occupation = Column(String(150), nullable=True)     # individual
    principal_business_activity = Column(
        String(5000), nullable=True)  # corporate
    names_of_directors_or_partners = Column(String, nullable=True)
    name_of_employer = Column(String(250), nullable=True)   # individual
    registered_office = Column(String(5000), nullable=True)      # corporate
    residential_address = Column(String(5000))      # individual
    tin_number = Column(String(40), unique=True, nullable=True)
    business_phone_number = Column(String(40), nullable=True)
    cellphone_number = Column(String(40), nullable=True)
    corporate_email = Column(String(100), nullable=True)
    personal_email = Column(String(100), nullable=True)
    opposing_party_name = Column(String(5000), nullable=True)
    opposing_party_lawyer = Column(String(5000), nullable=True)

    # /draft/consideration /registration/active/closed
    status = Column(String(10), nullable=False, default="draft")
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    # staffs
    created_by = relationship("Staff", back_populates="clients_created",
                              foreign_keys="Client.creator_id")

    updated_by = relationship("Staff", back_populates="clients_updated",
                              foreign_keys="Client.updator_id")

    # contacts
    contacts = relationship("Contact", secondary="clients_contacts",
                            back_populates="clients")

    # relationship managers
    relationship_managers = relationship("Staff", secondary="clients_staffs",
                                         back_populates="assigned_clients")
    # leads
    # leads = relationship("Lead" ,back_populates="client")

    # consultations
    consultations = relationship("Consultation", back_populates="client")

    # matters
    # matters = relationship("Matter", back_populates="client")

    # cases
    # matters = relationship("Matter", back_populates="client")

    # actions
    actions = relationship("Action", secondary="clients_actions",
                           back_populates="clients")

    # meetings

    # crm_tasks

    # calls

    # visits

    # appointments

    # invoices

    # payments

    # complaints

    def __str__(self):
        return self.client_name
