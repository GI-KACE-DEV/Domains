from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
#from uuid import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema) 
from .country import CountrySchema

class HTTPError(BaseModel):
    detail: str


#Address
class AddressBase(BaseModel):
      
    code: Optional[str] = None
    country: Optional[str] = None
   
      
# Properties to receive via API on creation
class AddressCreate(AddressBase):  
     
    address_line: str
    street: str
    city: str
    region_state: str
    country_id: UUID4
      
                               
# Properties to receive via API on update
class AddressUpdate(AddressBase):
   pass


class AddressInDBBase(AddressBase):
    
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None
    country_id: UUID4

    class Config:
        orm_mode = True


class AddressSchema(AddressInDBBase):
    pass


'''

class AddressSchema(AddressInDBBase):
    
    created_by: Optional[StaffSchema] 
    updated_by: Optional[StaffSchema] 
    country =  Optional[CountrySchema]
    


   
    
'''