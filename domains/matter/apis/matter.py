from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,
                            Table, Numeric)
from sqlalchemy.orm import relationship

from app.db.base import APIBase,  Base, UUID

import datetime

'''
class Chamber(APIBase):
    name = Column(String)
    description
    primary_phone = Column(String)
    secondary_phone = Column(String)
    primary_email = Column(String)
    secondary_email)
    website
    linkedin
    location
    address
        line_one
        line_two
        street
        city/province/region
        post_code



#matter_sectors
#matter_pratice_areas
#matter_type
#matter_categories
#matter_opposing_party_lawyers
#matter_opposing_party

#matter_actions
#matter_documents
#matter_comments
#matter_tags
#matter_notes

#matter_staffs
#matter_team
#matter_associates
#matter_supervising_partners


#case_courts
#case_notes
#case_documents
#case_associates???
#case_supervising_partners

'''

matters_practice_areas = Table(
    'matters_practice_areas', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('practice_area_id', UUID, ForeignKey('practice_areas.id'))
)


matters_sectors = Table(
    'matters_sectors', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('sector_id', UUID, ForeignKey('sectors.id'))
)


matters_staffs = Table(
    'matters_staffs', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('staff_id', UUID, ForeignKey('staffs.id'))
)


matters_categories = Table(
    'matters_categories', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('category_id', UUID, ForeignKey('categories.id'))
)


matters_types = Table(
    'matters_types', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('types_id', UUID, ForeignKey('types.id'))
)


cases_courts = Table(
    'cases_courts', Base.metadata,
    Column('case_id', UUID, ForeignKey('cases.id')),
    Column('court_id', UUID, ForeignKey('courts.id'))
)


matters_courts = Table(
    'matters_courts', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('court_id', UUID, ForeignKey('courts.id'))
)


matters_opposing_party_lawyers = Table(
    'matters_opposing_party_lawyers', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('opposing_party_lawyer_id', UUID, 
            ForeignKey('opposing_party_lawyers.id'))
)



matters_opposing_partie = Table(
    'matters_opposing_party_lawyers', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('opposing_party_lawyer_id', UUID, 
            ForeignKey('opposing_parties.id'))
)


matters_documents = Table(
    'matters_documents', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('document_id', UUID, ForeignKey('documents.id'))
)


matters_actions = Table(
    'matters_actions', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('action_id', UUID, ForeignKey('actions.id'))
)


matters_assocciates = Table(
    'matters_associates', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('staff_id', UUID, ForeignKey('staffs.id'))
)


matters_supervising_partners = Table(
    'matters_supervising_partners', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('staff_id', UUID, ForeignKey('staffs.id'))
)




'''
matters_comments = Table(
    'matters_comments', Base.metadata,
    Column('matter_id', UUID, ForeignKey('matters.id')),
    Column('comment_id', UUID, ForeignKey('comments.id'))
)


class Sector(APIBase):
    name = Column(String(250))
    description = Column(String(250))

     
    matters = relationship("Matter", secondary="matters_sectors", 
                            back_populates='sectors')
   
    def __str__(self):
        return self.name


class PracticeArea(APIBase):
    name = Column(String(250))
    description = Column(String(200))
    
    #matter
    matters = relationship("Matter", secondary="matters_practice_areas", 
                                  	back_populates='practice_areas')

    def __str__(self):
        return f"{self.name}"


class Staff(APIBase):
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), unique=True)
    phone_number = Column(String(25))
    designation = Column(String(25))

    def __str__(self):
        return "{self.first_name} {self.last_name}"
    
    #client  
    clients_created = relationship("Client", 
                                  back_populates="created_by",
                                  foreign_keys="Client.updator_id")
    
    clients_updated = relationship("Client", 
                                  back_populates="updated_by",
                                  foreign_keys="Client.creator_id")
    
    client_registrations_created = relationship("ClientRegistration", 
                                  back_populates="created_by",
                                  foreign_keys="ClientRegistration.updator_id")
    
    client_registrations_updated = relationship("ClientRegistration", 
                                  back_populates="updated_by",
                                  foreign_keys="ClientRegistration.updator_id")
    
    #matter
    matter_tasks_assigned_to = relationship("MatterTask", 
                                  back_populates="assignee",
                                  foreign_keys="MatterTask.assignee_id")
    
    matter_tasks_assigned_by = relationship("MatterTask", 
                                  back_populates="assigner",
                                  foreign_keys="MatterTask.assigner_id")
    
    matter_tasks_created = relationship("MatterTask", 
                                        back_populates="created_by",
                                        foreign_keys="MatterTask.creator_id")
    
    matter_tasks_updated = relationship("MatterTask", 
                                  back_populates="updated_by",
                                  foreign_keys="MatterTask.updator_id")
    
    matter_tasks_created = relationship("MatterTask", back_populates="created_by",
                              foreign_keys="MatterTask.creator_id")
    
    matters_updated = relationship("Matter", 
                                  back_populates="updated_by",
                                  foreign_keys="Matter.creator_id")
    
    matters_created = relationship("Matter", 
                                  back_populates="created_by",
                                  foreign_keys="Matter.updator_id")
    
    
    matters_supervising = relationship("Matter", 
                                secondary="matters_supervising_partners",
                                back_populates="supervising_partners"
                            )   
    
    matters_assigned = relationship("Matter", 
                            secondary="matters_associates",
                            back_populates="associates"
                        )   
    
    
    matters = relationship("Matter", 
                            secondary="matters_associates",
                            back_populates="associates"
                        )   
    
    actions_assigned = relationship("Action", secondary="action_staffs", 
                            back_populates="assigned_to")
    
    
    actions_assigned_by = relationship("Action", 
                                back_populates="assigned_by",
                                foreign_keys="Action.assigned_by_id"       
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
    status = Column(String(10), nullable=False, default="draft")
    registration_date = Column(DateTime)

    
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    
    created_by = relationship("Staff", 
                              back_populates="client_registrations_created",
                              foreign_keys="ClientRegistration.creator_id")
    
    updated_by = relationship("Staff", 
                              back_populates="client_registrations_updated",
                              foreign_keys="ClientRegistration.updator_id")    
      
    def __str__(self):
        return self.client_name



class Client(APIBase):

    client_type = Column(String(12))  # individual or corporate
    client_registration_number = Column(String(20), unique=True)
    client_name = Column(String(250))
    name_of_authourized_representative = Column(String(250))
    mailing_address = Column(String(5000))
    occupation = Column(String(150), nullable=True)  # individual
    principal_business_activity = Column(String(5000), nullable=True)  # corporate
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
    status = Column(String(10), nullable=False, default="draft")
    
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    #matters
    matters = relationship("Matter", back_populates="client")
        
    #staffs
    created_by = relationship("Staff", back_populates="clients_created",
                              foreign_keys="Client.creator_id")
    
    updated_by = relationship("Staff", back_populates="clients_updated",
                              foreign_keys="Client.updator_id")   


    def __str__(self):
        return self.name
        
        
'''

class Matter(APIBase):
    reference_number = Column(String(30), unique=True, index=True)
    brief = Column(Text)
    client_id = Column(UUID, ForeignKey("clients.id"))
    authourized_representative = Column(String(500))
    authourized_representative_email = Column(String(100), nullable=True)
    authourized_representative_phone = Column(String(100), nullable=True)
    #nature_of_engagement 
    date_of_engagement = Column(Date)
    status = Column(String(25), default="pending")
    assistance_required_from_partners = Column(Text, nullable=True)
    special_observations_remarks = Column(Text,nullable=True)
    fee = Column(Numeric, nullable=True, default=0)
    
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    
    #client
    client = relationship("Client", back_populates="matters")
    
    #staffs
    created_by = relationship("Staff", back_populates="matters_created",
                              foreign_keys="Matter.creator_id")
    
    updated_by = relationship("Staff", back_populates="matters_updated",
                              foreign_keys="Matter.updator_id")   

    staffs = relationship("Staff", secondary="matters_staffs", 
                            back_populates="matters")
    
    supervising_partners = relationship("Staff", 
                                secondary="matters_supervising_partners",
                                back_populates="matters_supervising",
                            )   
    
    associates = relationship("Staff", 
                                secondary="matters_associates",
                                back_populates="matters_assigned",
                            )   
         
    #sectors
    sectors = relationship("Sector", secondary="matters_sectors", 
                            back_populates="matters")
    #practice_areas
    practice_areas = relationship("PracticeArea", secondary="matters_practice_areas", 
                        	back_populates="matters")
    #categories
    categories = relationship("Category", secondary="matters_categories", 
                        	back_populates="matters")
    #types
    types = relationship("Type", secondary="matters_types", 
                        	back_populates="matters")

    #opposing parties
    #opposing party
    opposing_party_lawyers = relationship("OpposingPartyLawyer", 
                back_populates="matter",
                secondary="matters_opposing_party_lawyers"
            )

    opposing_parties = relationship("OpposingParty", back_populates="matter")
    

    #expenses
    expenses = relationship("Expense",  back_populates="matter")
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #notes
    notes = relationship("Note",  back_populates="matter")

    #entries
    entries = relationship("Entry",  back_populates="matter")

    #actions 
    actions = relationship("Action", 
                            secondary="matters_actions", 
                        	back_populates="matters")


    #actions 
    matter_tasks = relationship("MatterTask", back_populates="matter")


    #court cases
    courts = relationship("Court", secondary="matters_courts", 
                                  	back_populates="matters")
    
    cases = relationship("Case",  back_populates="matter")
    
    
    def __str__(self):
        return self.reference_number

