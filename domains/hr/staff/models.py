from sqlalchemy import (Column, Integer, String, ForeignKey, Numeric, Date, DateTime, Table,
                        Boolean, DateTime, Text, UniqueConstraint)
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.orm import backref

from app.db.base_class import APIBase, UUID, Base
from app.domains.task.models.task import task_staffs  # , task_teams
from app.domains.common.models.practice_area import PracticeArea
from app.domains.common.models.contact import Contact
from app.domains.officemanager import VisitEntry
from app.domains.crm.models.client import Client
from app.domains.auth.models import User
from app.domains.hr.leave.models.annual_leave import AnnualLeave


staff_sectors = Table(
    'staff_sectors', Base.metadata,
    Column('staff_id', UUID, ForeignKey('staffs.id')),
    Column('sector_id', UUID, ForeignKey('sectors.id'))
)


stafs_tasks = Table(
    'staffs_tasks', Base.metadata,
    Column('staff_id', UUID, ForeignKey('staffs.id')),
    Column('task_id', UUID, ForeignKey('tasks.id'))
)


staffs_practice_areas = Table(
    'staffs_practice_areas', Base.metadata,
    Column('staff_id', UUID, ForeignKey('staffs.id')),
    Column('practice_areas_id', UUID, ForeignKey('practice_areas.id'))
)


staffs_contacts = Table(
    'staffs_contacts', Base.metadata,
    Column('staff_id', UUID, ForeignKey('staffs.id')),
    Column('contact_id', UUID, ForeignKey('contacts.id'))
)


class Department(APIBase):

    name = Column(String(50), unique=True, nullable=True)
    location = Column(String(50), nullable=True)

    def __str__(self):
        return f"{self.name}"


class Designation(APIBase):

    title = Column(String(250), nullable=False, unique=True)
    min_salary = Column(Numeric, nullable=True, default=0.0)
    maximum_salary = Column(Numeric, nullable=True, default=0.0)
    rate_per_case = Column(Numeric, nullable=True, default=1.0)
    rate_per_hour = Column(Numeric, nullable=True, default=1.0)
    commission_per_case = Column(Numeric, nullable=True, default=0.0)

    def __str__(self):
        return self.title


class Qualification(APIBase):

    title = Column(String(5), nullable=True)
    description = Column(Text)

    def self__(self):
        return self.title


class Staff(APIBase):

    first_name = Column(String(250))
    last_name = Column(String(250))
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    tin = Column(String(250), unique=True, nullable=True)
    ssn = Column(String(250), unique=True, nullable=True)
    nhis = Column(String(250), unique=True, nullable=True)
    national_id = Column(String(250), unique=True, nullable=True)

    official_email = Column(String(250), unique=True, nullable=True)
    personal_email = Column(String(250), unique=True)
    cellphone_1 = Column(String(20), nullable=True)
    cellphone_2 = Column(String(20), nullable=True)
    location = Column(String(250), nullable=True)
    linkedin = Column(String(50), nullable=True)
    registration_number = Column(String(50), unique=True, nullable=True)
    year_called_to_bar = Column(DateTime, nullable=True)
    leave_days = Column(Integer, default=21, nullable=False)
    sick_days = Column(Integer, default=1)
    overtime_allowed = Column(Boolean, default=False)
    salary = Column(Numeric(10, 2), nullable=True, default=0.00)
    rate_per_matter = Column(Numeric(10, 2), nullable=True)
    rate_per_matter = Column(Numeric(10, 2), nullable=True)
    commission_per_matter = Column(Numeric(10, 2), nullable=True)
    hire_date = Column(Date, nullable=True, default=None)
    end_date = Column(Date, nullable=True, default=None)
    is_active = Column(Boolean, default=False)

    # supervisor_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    designation_id = Column(UUID, ForeignKey("designations.id"), nullable=True)
    department_id = Column(UUID, ForeignKey("departments.id"), nullable=True)

    # staff
    # user = relationship("User",  uselist=False, back_populates="staff")

    # designation
    designation = relationship("Designation", backref="staff")
    department = relationship("Department", backref="staff")

    # created_contacts = relationship("Contact", back_populates="created_by")

    teams = relationship("Team", secondary="team_staffs",
                         back_populates="members")

    # CRM
    # account
    # accounts_created = relationship("Account", back_populates="created_by",
    #                                foreign_keys="Account.creator_id")

    # accounts_updated = relationship("Account", back_populates="updated_by",
    #                               foreign_keys="Account.updator_id")

    # assigned_accounts = relationship("Account", secondary="accounts_staffs",
    #                                back_populates="assigned_to")

    # Clients
    client_registrations_created = relationship(
        "ClientRegistration",
        back_populates="created_by",
        foreign_keys="ClientRegistration.creator_id")

    client_registrations_updated = relationship(
        "ClientRegistration",
        back_populates="updated_by",
        foreign_keys="ClientRegistration.updator_id")

    clients_created = relationship("Client", back_populates="created_by",
                                   foreign_keys="Client.creator_id")

    clients_updated = relationship("Client", back_populates="created_by",
                                   foreign_keys="Client.updator_id")

    assigned_clients = relationship("Client", secondary="clients_staffs",
                                    back_populates="relationship_managers")

    # leads
    leads_created = relationship("Lead", back_populates="created_by",
                                 foreign_keys="Lead.creator_id")

    leads_updated = relationship("Lead", back_populates="updated_by",
                                 foreign_keys="Lead.updator_id")

    assigned_leads = relationship("Lead", secondary="leads_staffs",
                                  back_populates="assigned_to")

    # consultation
    assigned_consultations = relationship("Consultation", secondary="consultations_staffs",
                                          back_populates="assigned_to")

    consultations_led = relationship("Consultation", back_populates="lead_counsel",
                                     foreign_keys="Consultation.lead_counsel_id")

    consultations_created = relationship("Consultation", back_populates="created_by",
                                         foreign_keys="Consultation.creator_id")

    consultations_updated = relationship("Consultation", back_populates="updated_by",
                                         foreign_keys="Consultation.updator_id")

    # common
    sectors = relationship("Sector", secondary="staff_sectors",
                           back_populates="staffs")

    # action

    assigned_actions = relationship("Action", secondary="action_staffs",
                                    back_populates="assigned_staffs")

    actions_created = relationship("Action", back_populates="created_by",
                                   foreign_keys="Action.creator_id")

    actions_updated = relationship("Action", back_populates="updated_by",
                                   foreign_keys="Action.updator_id")

    # activities
    action_activities = relationship("ActionActivity", back_populates="staff")

    # practice area
    practice_areas = relationship("PracticeArea", secondary="staffs_practice_areas",
                                  back_populates="staffs")
    # comments
    comments = relationship("Comment", back_populates="commented_by")

    # attachments
    # attachments = relationship("Attachment", back_populates="staff")

    # crm_tasks
    assigned_crm_tasks = relationship("Task", secondary="staffs_tasks",
                                      back_populates="staffs")

    # contacts
    contacts = relationship("Contact", secondary="staffs_contacts",
                            back_populates="staffs")

    # Office Manager
    # visit entries
    visit_entries_created = relationship("VisitEntry", back_populates="created_by",
                                         foreign_keys="VisitEntry.creator_id")

    visit_entries_updated = relationship("VisitEntry", back_populates="updated_by",
                                         foreign_keys="VisitEntry.updator_id")

    received_visits = relationship("VisitEntry", back_populates="person_to_see",
                                   foreign_keys="VisitEntry.person_to_see_id")

    # expected visitors
    expected_visitors_created = relationship("ExpectedVisitor", back_populates="created_by",
                                             foreign_keys="ExpectedVisitor.creator_id")

    expected_visitors_updated = relationship("ExpectedVisitor", back_populates="updated_by",
                                             foreign_keys="ExpectedVisitor.updator_id")

    expected_visitors = relationship("ExpectedVisitor", back_populates="person_to_see",
                                     foreign_keys="ExpectedVisitor.person_to_see_id")

    # incoming documents
    incoming_documents_created = relationship("Incoming", back_populates="created_by",
                                              foreign_keys="Incoming.creator_id")

    incoming_documents_updated = relationship("Incoming",
                                              back_populates="updated_by",
                                              foreign_keys="Incoming.updator_id")

    deliveries_received = relationship("Incoming",
                                       back_populates="received_by",
                                       foreign_keys="Incoming.delivered_to_id")

    incoming_documents = relationship("Incoming",
                                      back_populates="addressed_to",
                                      foreign_keys="Incoming.to_whom_id")

    # visitors
    visitors_created = relationship("Visitor", back_populates="created_by",
                                    foreign_keys="Visitor.creator_id")

    visitors_updated = relationship("Visitor", back_populates="updated_by",
                                    foreign_keys="Visitor.updator_id")

    # outgoing documents
    outgoing_documents_created = relationship("Outgoing", back_populates="created_by",
                                              foreign_keys="Outgoing.creator_id")

    outgoing_documents_updated = relationship("Outgoing", back_populates="updated_by",
                                              foreign_keys="Outgoing.updator_id")

    typed_outgoing_documents = relationship("Outgoing", back_populates="typist",
                                            foreign_keys="Outgoing.typist_id")

    authourized_outgoing_documents = relationship("Outgoing", back_populates="partner",
                                                  foreign_keys="Outgoing.partner_id")

    associates_outgoing_documents = relationship("Outgoing", secondary="associates_outgoings",
                                                 back_populates="associates")

    # leave
    annual_leaves = relationship("AnnualLeave", back_populates="staff")
    leaves = relationship("Leave", back_populates="staff")

    def get_name(self):
        """Return the employe member's name."""
        return f"{self.first_name} {self.last_name}"

    def _current_year(self):
        """Get the current year."""
        return datetime.today().year

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
