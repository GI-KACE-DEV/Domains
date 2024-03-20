from sqlalchemy import (Column, Integer, String, ForeignKey, Numeric, Date, Table,
                        Boolean, DateTime, Text, UniqueConstraint)
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.orm import backref, relationship

from app.db.base_class import APIBase, UUID, Base
from app.domains.common.models.practice_area import PracticeArea
from app.domains.common.models.sector import Sector

'''
from app.domains.common.models.utils import (
    COUNTRIES,
    LEAD_SOURCE,
    LEAD_STATUS,
    return_complete_address,
    INDCHOICES,
)'''

# from app.domains.crm.models.contact import Contact
from app.domains.common.models.contact import Contact

from app.domains.common.models.sector import Sector
from app.domains.common.models.tag import Tag
from app.domains.common.models.practice_area import PracticeArea
from app.domains.common.models.generics import (
    HasAction,
    HasComment,
    HasAttachement,
    HasDocument,
)


leads_tags = Table(
    'leads_tags', Base.metadata,
    Column('lead_id', UUID, ForeignKey('leads.id')),
    Column('tag_id', UUID, ForeignKey('tags.id'))
)

leads_staffs = Table(
    'leads_staffs', Base.metadata,
    Column('lead_id', UUID, ForeignKey('leads.id')),
    Column('staffs_id', UUID, ForeignKey('staffs.id'))
)

# leads_teams = Table(
#    'leads_teams', Base.metadata,
#    Column('lead_id', UUID, ForeignKey('leads.id')),
#    Column('team_id', UUID, ForeignKey('teams.id'))
# )


leads_sectors = Table(
    'leads_sectors', Base.metadata,
    Column('lead_id', UUID, ForeignKey('leads.id')),
    Column('sector_id', UUID, ForeignKey('sectors.id'))
)


leads_practice_areas = Table(
    'leads_practice_areas', Base.metadata,
    Column('lead_id', UUID, ForeignKey('leads.id')),
    Column('practice_areas_id', UUID, ForeignKey('practice_areas.id'))
)


leads_contacts = Table(
    'leads_contacts', Base.metadata,
    Column('lead_id', UUID, ForeignKey('leads.id')),
    Column('contact_id', UUID, ForeignKey('contacts.id'))
)


leads_attachments = Table(
    'leads_attachments', Base.metadata,
    Column('lead_id', UUID, ForeignKey('leads.id')),
    Column('attachment_id', UUID, ForeignKey('attachments.id'))
)


leads_comments = Table(
    'leads_comments', Base.metadata,
    Column('lead_id', UUID, ForeignKey('leads.id')),
    Column('comment_id', UUID, ForeignKey('comments.id'))
)


leads_actions = Table(
    'leads_actions', Base.metadata,
    Column('lead_id', UUID, ForeignKey('leads.id')),
    Column('action_id', UUID, ForeignKey('actions.id'))
)


class LeadStatus(APIBase):
    status = Column(String(255))
    description = Column(Text, nullable=True)

    def __str__(self):
        return self.status


class LeadSource(APIBase):

    source = Column(String(255))
    description = Column(Text, nullable=True)

    def _str__(self):
        return self.source


# class Lead(HasComment, HasAttachement, HasAction, APIBase):

class Lead(APIBase):

    description = Column(Text)
    salutation = Column(String(255), nullable=True)
    first_name = Column(String(255))
    last_name = Column(String(255), nullable=True)
    primary_email = Column(String(255), nullable=True)
    secondary_email = Column(String(255), nullable=True)
    primary_cellphone = Column(String(25), nullable=True)
    secondary_cellphone = Column(String(25), nullable=True)
    # source_id = Column(UUID, ForeignKey("lead_sources.id"), nullable=True)
    source = Column(String, nullable=True)
    address_line = Column(String(500), nullable=True)
    street = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    state_region = Column(String(255), nullable=True)
    postcode = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    website = Column(String(255), nullable=True)
    status = Column(String(25), nullable=True)
    is_active = Column(Boolean, default=False)

    estimated_value = Column(Numeric(10, 2), nullable=True, default=0.0)
    probability = Column(Numeric, nullable=True, default=0.0)

    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    close_date = Column(Date, nullable=True)

    created_by = relationship("Staff", back_populates="leads_created",
                              foreign_keys="Lead.creator_id")

    updated_by = relationship("Staff", back_populates="leads_updated",
                              foreign_keys="Lead.updator_id")

    sectors = relationship(
        "Sector", secondary="leads_sectors", back_populates="leads")

    practice_areas = relationship("PracticeArea", secondary="leads_practice_areas",
                                  back_populates="leads")

    contacts = relationship("Contact", secondary="leads_contacts",
                            back_populates="leads")

    assigned_to = relationship("Staff", secondary="leads_staffs",
                               back_populates="assigned_leads")

    attachments = relationship("Attachment", secondary="leads_attachments",
                               back_populates="leads")

    comments = relationship(
        "Comment", secondary="leads_comments", back_populates="leads")

    tags = relationship("Tag", secondary="leads_tags", back_populates="leads")
    actions = relationship("Action", secondary="leads_actions",
                           back_populates="leads")

    def __str__(self):
        return self.title

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_team_staff(self):
        team_staffs = [
            staff for team in self.teams for staffs in team for staff in staffs
        ]
        return team_staffs

    @property
    def get_team_and_assigned_staffs(self):
        assigned_staffs = self.assigned_to
        staffs = self.get_team_staff + assigned_staffs
        return staffs

    @property
    def get_assigned_staffs_not_in_teams(self):
        staffs = set(self.get_team_staff) - set(self.assigned_to)
        return staffs

    def convert(self):
        # change status to converted
        # creat account out of it if accoun does not exists
        pass

    # def save(self, *args, **kwargs):
    #     super(Lead, self).save(*args, **kwargs)
    #     queryset = Lead.objects.all().exclude(status='converted').select_related('created_by'
    #         ).prefetch_related('tags', 'assigned_to',)
    #     open_leads = queryset.exclude(status='closed')
    #     close_leads = queryset.filter(status='closed')
    #     cache.set('admin_leads_open_queryset', open_leads, 60*60)
    #     cache.set('admin_leads_close_queryset', close_leads, 60*60)
