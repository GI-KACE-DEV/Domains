from pydantic import BaseModel, UUID4
from typing import Optional, List
from app.domains.matter.schemas.matter import MatterSchema
from app.domains.matter.schemas. case import CaseSchema
#from app.domains.common.schemas.district import DistrictSchema
from app.domains.matter.schemas.district import DistrictSchema


# Shared properties
class CourtBase(BaseModel):
    
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str]  = None 
    district_id: Optional[UUID4] = None
    email: Optional[str] = None
    phone: Optional[str] = None


# Properties to receive via API on creation
class CourtCreate(CourtBase):
    name: str
    location: str

# Properties to receive via API on update
class CourtUpdate(CourtBase):
    pass

class CourtInDBBase(CourtBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class CourtSchema(CourtInDBBase):
    
    district = Optional[DistrictSchema]
    #matters = Optional[List[MatterSchema]]
    #cases = Optional[List[CaseSchema]]


# Additional properties stored in DB
class CourtInDB(CourtInDBBase):
    pass




