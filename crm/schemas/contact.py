from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema) 
from .address import AddressSchema

class HTTPError(BaseModel):
    detail: str


#Contact
class ContactBase(BaseModel):
    
    salutation: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    first_name:  Optional[str] = None
    middle_name: Optional[str] = None
    last_name:  Optional[str] = None
    date_of_birth: Optional[date]
    personal_email: Optional[str] = None
    primary_official_email: Optional[str] = None
    secondary_official_email: Optional[str] = None
    primary_mobile_number:  Optional[str] = None
    secondary_mobile_number: Optional[str] = None
    home_phone_number: Optional[str] = None
    primary_office_phone_number: Optional[str] = None
    secondary_office_phone_number: Optional[str] = None

    department: Optional[str] = None
    language: Optional[str] = None
    do_not_call: Optional[str] = None
    website_url: Optional[str] = None
    linked_in_url: Optional[str] = None
    facebook_url: Optional[str] = None
    twitter_username: Optional[str] = None
    country: Optional[str] = None
    is_active: Optional[bool] = False
    creator_id:  Optional[UUID] = None
   
    address_ids: Optional[ List[UUID]] = []
    staff_ids: Optional[ List[UUID]] = []
    lead_ids: Optional[ List[UUID]] = []
    #meeting_action_ids : Optional[ List[UUID]] = []
    
      
# Properties to receive via API on creation
class ContactCreate(ContactBase): 
     
    salutation: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    first_name:  Optional[str] = None
    middle_name: Optional[str] = None
    last_name:  Optional[str] = None
    date_of_birth: Optional[date]
    personal_email: Optional[str] = None
    primary_official_email: Optional[str] = None
    secondary_official_email: Optional[str] = None
    primary_mobile_number:  Optional[str] = None
    secondary_mobile_number: Optional[str] = None
    home_phone_number: Optional[str] = None
    primary_office_phone_number: Optional[str] = None
    secondary_office_phone_number: Optional[str] = None
    do_not_call: Optional[bool] = False
    
   
            
# Properties to receive via API on update
class ContactUpdate(ContactBase):
   pass


class ContactInDBBase(ContactBase):
    id: Optional[UUID] = None
    creator_id: Optional[UUID] = None
    #updator_id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ContactSchema(ContactInDBBase):
    
    created_by: Optional[StaffSchema] = None
    updated_by: Optional[StaffSchema]  = None

    addresses: Optional[AddressSchema] = None
    staffs: Optional[List[StaffSchema]] = []

    #meeting_actions : Optional[ List[MeetingActionSchema]] = []

   
    