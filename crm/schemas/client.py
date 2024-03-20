from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel
#from uuid import UUID
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import (SectorSchema, StaffSchema, 
        PracticeAreaSchema
    ) 

from app.domains.crm.schemas.contact import ContactSchema
from app.domains.common.schemas.action import ActionSchema
from app.domains.common.schemas.comment import CommentSchema
from app.domains.common.schemas.attachment import AttachmentSchema
from app.domains.common.schemas.tag import TagSchema


class HTTPError(BaseModel):
    detail: str


#Client
class ClientBase(BaseModel):
    
    client_type: Optional[str] = None # individual or corporate
    client_registration_number: Optional[str] = None 
    client_name: Optional[str] = None
    name_of_authourized_representative: Optional[str] = None
    mailing_address: Optional[str] = None
    occupation: Optional[str] = None    # individual
    principal_business_activity: Optional[str] = None
    names_of_directors_or_partners: Optional[str] = None
    name_of_employer: Optional[str] = None# individual
    registered_office: Optional[str] = None  # corporate
    residential_address: Optional[str] = None
    tin_number: Optional[str] = None
    business_phone_number: Optional[str] = None
    cellphone_number: Optional[str] = None
    corporate_email: Optional[str] = None
    personal_email: Optional[str] = None
    opposing_party_name: Optional[str] = None
    opposing_party_lawyer: Optional[str] = None
    status : Optional[str] = None

   
# Properties to receive via API on creation
class ClientCreate(ClientBase):
    client_type: Optional[str] # individual or corporate
    client_name: str
    mailing_address: str
    cellphone_number: str


# Properties to receive via API on update
class ClientUpdate(ClientBase):
   pass


class ClientInDBBase(ClientBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ClientSchema(ClientInDBBase):

    #matter
    #case
    #actions
    #meetings
    #tasks
    #visits
    #appointments
    #support
    #invoices
    #payments
    #attachments: Optional[AttachmentSchema] = []
    
    contacts: Optional[ContactSchema] = []
    
    relationship_managers: List[StaffSchema] = []
    
    sectors: Optional[List[UUID4]] = []

    practice_areas: Optional[List[UUID4]] = []
    
    actions: Optional[List[ActionSchema]] = []


    #crm
    #front office
    #appointments: Optional[List[AppointmentSchema]]
    #visit_ : 


    #matters
    #matters: Optional[List[MatterSchema]] = []
