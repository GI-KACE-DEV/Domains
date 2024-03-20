from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4   
#from uuid import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema) 


class HTTPError(BaseModel):
    detail: str


#Country
class CountryBase(BaseModel):
      
    code: Optional[str] = None
    country: Optional[str] = None
    
   

# Properties to receive via API on creation
class CountryCreate(CountryBase):  
     
    code: Optional[str] = None
    country: Optional[str] = None
    address_ids: Optional[str] = []
      
                               
# Properties to receive via API on update
class CountryUpdate(CountryBase):
   pass


class CountryInDBBase(CountryBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None
    country_id: UUID4

    class Config:
        orm_mode = True


# Additional properties to return via API
class CountrySchema(CountryInDBBase):
    
    created_by: Optional[StaffSchema] 
    updated_by: Optional[StaffSchema] 


   
    