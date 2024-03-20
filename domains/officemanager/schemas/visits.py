from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import StaffSchema

class HTTPError(BaseModel):
    detail: str
from app.domains.officemanager.models.dispatch import Incoming, Outgoing
from app.crud.base import CRUDBase
from app.domains.officemanager.schemas.dispatches import  (
    IncomingCreate, IncomingUpdate,
    OutgoingCreate, OutgoingUpdate
)


class HTTPError(BaseModel):
    detail: str


class CRUDIncoming(CRUDBase[Incoming, IncomingCreate, IncomingUpdate]):
    pass
    

incoming_actions = CRUDIncoming(Incoming)
    

class CRUDOutgoing(CRUDBase[Outgoing, OutgoingCreate, OutgoingUpdate]):
    pass
    

outgoing_actions = CRUDOutgoing(Outgoing)
    


# ********Visit Status *****************
# Shared properties
class VisitStatusBase(BaseModel):
    status: Optional[str] = None
    description: Optional[str]
    

# Properties to receive via API on creation
class VisitStatusCreate(VisitStatusBase):
    status:  str


# Properties to receive via API on update
class VisitStatusUpdate(VisitStatusBase):
   pass


class VisitStatusInDBBase(VisitStatusBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class VisitStatusSchema(VisitStatusInDBBase):
    #visit_entries: Optional[ List[VisitEntrySchema] ]
    pass


# ********Visit Category *****************
# Shared properties
class VisitCategoryBase(BaseModel):
    category: Optional[str] = None
    description: Optional[date]
    

# Properties to receive via API on creation
class VisitCategoryCreate(VisitCategoryBase):
    category:  str


# Properties to receive via API on update
class VisitCategoryUpdate(VisitCategoryBase):
   pass


class VisitCategoryInDBBase(VisitCategoryBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class VisitCategorySchema(VisitCategoryInDBBase):
    pass
    #expected_visitors: Optional[ List[ExpectedVisitorsEntrySchema]] = None
    #visit_entries: Optional[ List[ReviewPeriodSchema]]


# ******** Office Area *****************
# Shared properties

class OfficeAreaBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str]
    

# Properties to receive via API on creation
class OfficeAreaCreate(OfficeAreaBase):
    name:  str


# Properties to receive via API on update
class OfficeAreaUpdate(OfficeAreaBase):
   pass


class OfficeAreaInDBBase(OfficeAreaBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class OfficeAreaSchema(OfficeAreaInDBBase):    
    pass

    
# ******** Expected Visitor *****************
# Shared properties
class ExpectedVisitorBase(BaseModel):
    
    visitor_name: Optional[str] = None
    visitor_email: Optional[str] = None
    visitor_phone: Optional[str] = None
    visit_purpose: Optional[str] = None
    visit_date: Optional[datetime] = None

    person_to_see_id: Optional[UUID4] = None
    visit_category_id: Optional[UUID4] = None
    office_area_id: Optional[UUID4] = None
    visit_status_id: Optional[UUID4] = None
    
    

# Properties to receive via API on creation
class ExpectedVisitorCreate(ExpectedVisitorBase):
    pass

# Properties to receive via API on update
class ExpectedVisitorUpdate(ExpectedVisitorBase):
   pass


class ExpectedVisitorInDBBase(ExpectedVisitorBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ExpectedVisitorSchema(ExpectedVisitorInDBBase):
    visit_category: Optional[VisitCategorySchema]    
    status: Optional[VisitStatusSchema]
    #person_to_see: Optional[StaffSchema]    





# ******** Visit Entry *****************

# Shared properties
class VisitEntryBase(BaseModel):

    #salutation: Optional[str] = None
    #first_name: Optional[str] = None
    #last_name: Optional[str] = None
    #email: Optional[str] = None
    #phone: Optional[str] = None

    visitor_id: Optional[UUID4] = None
    purpose_of_visit:Optional[str] = None
    place_from: Optional[str] = None
    visit_category_id: Optional[UUID4] = None
   # person_to_see_id: Optional[UUID4] = None
    office_area_id: Optional[UUID4] = None
    visitor_tag_code: Optional[UUID4] = None
    time_in: Optional[datetime] = None
    time_out: Optional[datetime] = None


# Properties to receive via API on creation
class VisitEntryCreate(VisitEntryBase):

    visitor_id: Optional[UUID4] = None
    purpose_of_visit:Optional[str] = None
    #place_from: Optional[str] = None
    visit_category_id: Optional[UUID4] = None
    person_to_see_id: Optional[UUID4] = None
    office_area_id: Optional[UUID4] = None
    visitor_tag_code: Optional[str] = None
    time_in: Optional[datetime] = None
    time_out: Optional[datetime] = None


# Properties to receive via API on update
class VisitEntryUpdate(VisitEntryBase):
   pass


class VisitEntryInDBBase(VisitEntryBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class VisitEntrySchema(VisitEntryInDBBase):
    pass

    #visitor: Optional[VisitorSchema] = None


# ******** Visitor ****************

# Shared properties
class VisitorBase(BaseModel):

    salutation: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    

# Properties to receive via API on creation
class VisitorCreate(VisitorBase):

    first_name:str
    last_name: str
   
 
# Properties to receive via API on update
class VisitorUpdate(VisitorBase):
   pass


class VisitorInDBBase(VisitEntryBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class VisitorSchema(VisitorInDBBase):
    visit_entries: Optional[VisitEntrySchema]
    
