from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import StaffSchema

class HTTPError(BaseModel):
    detail: str

    
#<<<<<<<<<<<<<<Dispatch>>>>>>>>>>>>>********
# Incoming
#******** Incoming Entry *****************

# Shared properties
class IncomingBase(BaseModel):
        
    document_title: Optional[str] = None
    description: Optional[str] = None
    client: Optional[str] = None
    to_whom_id: Optional[UUID4] = None
    delivered_to_id:  Optional[UUID4] = None
    receipt_acknowledged: Optional[bool] = None
    sender_name: Optional[str] = None
    courier_name: Optional[str] = None
    courier_phone: Optional[str] = None
    

# Properties to receive via API on creation
class IncomingCreate(IncomingBase):
        
    document_title: Optional[str] = None
    sender_name: Optional[str] = None


# Properties to receive via API on update
class IncomingUpdate(IncomingBase):
   pass


class IncomingInDBBase(IncomingBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class IncomingSchema(IncomingInDBBase):
    #received_by: Optional[StaffSchema]
    #addressed_to = Optional[StaffSchema]
    pass


#******** Outgoing Entry *****************
# Shared properties
class OutgoingBase(BaseModel):
        
    serial_no: Optional[str]
    document_title: Optional[str]
    typist_id: Optional[UUID4]
    reference_number: Optional[str]
    date: Optional[str]
    #document: Optional[UUID4] = Column(UUID, ForeignKey("documents.id"))

    # staff
    partner_id: Optional[UUID4] 
    typist_id: Optional[UUID4] 
    creator_id: Optional[UUID4] 
    updator_id: Optional[UUID4] 


# Properties to receive via API on creation
class OutgoingCreate(OutgoingBase):
      
    serial_no: str
    document_name: str
    typist_id: UUID4
    date: datetime

    # staff
    partner_id: Optional[UUID4] 
    typist_id: Optional[UUID4] 
    creator_id: Optional[UUID4] 
    updator_id: Optional[UUID4] 

    
# Properties to receive via API on update
class OutgoingUpdate(OutgoingBase):
   pass


class OutgoingInDBBase(OutgoingBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True

# Additional properties to return via API
class OutgoingSchema(OutgoingInDBBase):
    partner: Optional[StaffSchema]
    typist: Optional[StaffSchema]
    