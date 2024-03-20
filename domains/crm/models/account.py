from sqlalchemy import (Column, Integer, String, ForeignKey, Numeric, Date, Table,
                        Boolean, DateTime, Text, UniqueConstraint)
import datetime
from sqlalchemy.orm import backref, relationship

from app.db.base_class import APIBase, UUID, Base
from app.domains.common.models.practice_area import PracticeArea
from app.domains.common.models.sector import Sector

from app.domains.common.models.sector import Sector
from app.domains.common.models.tag import Tag
from app.domains.common.models.practice_area import PracticeArea

from app.domains.common.models.generics import (
    HasAction,
    HasComment,
    HasAttachement,
    HasDocument,
)

'''
accounts_tags = Table(
    'accounts_tags', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('tag_id', UUID, ForeignKey('tags.id'))
)

accounts_staffs = Table(
    'accounts_staffs', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('staffs_id', UUID, ForeignKey('staffs.id'))
)

accounts_teams = Table(
    'accounts_teams', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('team_id', UUID, ForeignKey('teams.id'))
)

accounts_sectors = Table(
    'accounts_sectors', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('sector_id', UUID, ForeignKey('sectors.id'))
)

accounts_practice_areas = Table(
    'accounts_practice_areas', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('practice_areas_id', UUID, ForeignKey('practice_areas.id'))
)

accounts_contacts = Table(
    'accounts_contacts', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('contact_id', UUID, ForeignKey('contacts.id'))
)

accounts_attachments = Table(
    'accounts_attachments', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('attachment_id', UUID, ForeignKey('attachments.id'))
)


accounts_documentss = Table(
    'accounts_documents', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('document_id', UUID, ForeignKey('documents.id'))
)

accounts_comments = Table(
    'accounts_comments', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('comment_id', UUID, ForeignKey('comments.id'))
)

accounts_actions = Table(
    'accounts_actions', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id')),
    Column('action_id', UUID, ForeignKey('actions.id'))
)


accounts_tasks = Table(
    'accounts_tasks', Base.metadata,
    Column('account_id', UUID, ForeignKey('accounts.id'),),
    Column('task_id', UUID, ForeignKey('tasks.id'))
)


class AccountStatus(APIBase):

    status = Column(String(20))
    description = Column(Text, nullable=True)

    def __str__(self):
        return self.status


class Nextofkin(APIBase):

    client_id  = Column(UUID , ForeignKey("individual_clients.id"))
    dob = Column(Date , nullable=True)
    first_name = Column(String(250))
    middle_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    relationship_to_client = Column(String(250), nullable=True)

    def __str__(self):
        return f"{self.first} {self.middle_name} {self.last_name}"


class CorporateClient(APIBase):

    #corporate infor
    client_name = Column(String(250))
    legal_representative = Column(String(250))
    principal_business_activities = Column(String(250))
    name_of_directors_partners = Column(Text)
    vat_number = Column(String(250))
    tin = Column(String(250))

    #contact info
    office_address_line1 =  Column(String(250))	
    office_address_line_2 =  Column(String(250))
    city =   Column(String(250))
    state_province_region =  Column(String(250))
    country = Column(UUID, ForeignKey("countries.id"), nullable=True)
    business_phone = Column(String(20))
    corporate_email = Column(String(20), unique=True)
    personal_email = Column(String(20),nullable=True)
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    account = relationship(
  			'Account',
  			primaryjoin="and_(Account.client_type=='corporate', \
   				foreign(Account.client_id)==CorporateClient.id)", 
    		#lazy="dynamic", 
            back_populates="corporate_client" 
    )


    def __str__(self):
        return self.client_name


class IndividualClient(APIBase):

    #personal info
    first_name = Column(String(250))
    middle_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    date_of_birth = Column(Date)
    spouse_name = Column(String(250), nullable=True)
    occupation = Column(String(250), nullable=True)
    employer = Column(String(250), nullable=True)

	#contact info
    mailing_address = Column(Text)	
    home_phone = Column(String(25), nullable=True)
    business_phone = Column(String(25), nullable=True)
    cellphone = Column(String(25), nullable=True)
    email = Column(String(250), nullable=True, unique=True)

    registration_date = Column(Date, nullable=True)
    #status_id = Column(UUID, ForeignKey("accounts_statuses.id"))   
    #creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    #updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    account = relationship(
  			'Account',
  			primaryjoin="and_(Account.client_type=='individual', \
   			    foreign(Account.client_id)==IndividualClient.id)", 
    		#lazy="dynamic",
      		back_populates="individual_client" 
       )

    @property
    def client_name(self):
        name = f"{self.first_name} {self.middle_name} {self.last_name}"
        return " ".join(name).split()


class Account(APIBase):

    name = Column(String(750))
    reference_number = Column(String(25), nullable=True)
    client_id =  Column(Integer, unique = True)
    client_type = Column(String(25))
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    corporate_client = relationship(
      'CorporateClient',
      primaryjoin="and_(Account.client_type=='corporate', foreign(Account.client_id)==CorporateClient.id)",
      uselist=False,
      back_populates = "account"
    )

    individual_client = relationship(
      'IndividualClient',
      primaryjoin="and_(Account.client_type=='individual', foreign(Account.client_id)==IndividualClient.id)",
      uselist=False,
      back_populates="account"
    )

    def parent(self):
        if self.client_type == 'corporate':
            return self.corporate_client.to_dict()
        elif self.client_type == 'individual':
            return self.individual_client.to_dict()
        else:
            return "Invalid imageable_type"

    def to_dict(self):
        return {
            "id": self.id,
            #"url": self.url,
            "client_id": self.client_id,
            "client_type": self.client_type,
            "parent": self.parent()
        }


    #staff   
    created_by = relationship("Staff", back_populates="accounts_created",
                            foreign_keys="Account.creator_id")
   
    updated_by = relationship("Staff", back_populates="accounts_updated",
                              foreign_keys="Account.updator_id")

    assigned_to = relationship("Staff", secondary="accounts_staffs",
                               back_populates="assigned_accounts")

    teams =  relationship("Team", secondary="accounts_teams", 

                          back_populates="accounts")
    #crm   
    contacts = relationship("Contact", secondary="accounts_contacts", 
                            back_populates="accounts")

    actions =  relationship("Action", secondary="accounts_actions", 
                            back_populates="accounts")

    #common  
    sectors =  relationship("Sector", secondary="accounts_sectors", 
                            back_populates="accounts")

    practice_areas =  relationship("PracticeArea", secondary="accounts_practice_areas", 
                        	back_populates="accounts")


    attachments =  relationship("Attachment", secondary="accounts_attachments",
                                back_populates="accounts")

    documents =  relationship("Document", secondary="accounts_documents",
                                back_populates="accounts")
 
    #comments =  relationship("Comment", secondary="accounts_comments", 
    #                         back_populates="accounts")

    tags =  relationship("Tag", secondary="accounts_tags",
                            back_populates="accounts")

    tasks =  relationship("Task", secondary="accounts_tasks", 
                          back_populates="accounts")
'''
