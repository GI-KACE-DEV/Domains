from pydantic import BaseModel, UUID4
from typing import Optional, List

#from app.domains.matter.schemas.matter import MatterSchema
from app.domains.matter.schemas.court import CourtSchema

# Shared properties
class DistrictBase(BaseModel):
    region_id: Optional[UUID4] = None
    name:Optional[str] = None 
    code: Optional[str] = None


# Properties to receive via API on creation
class DistrictCreate(DistrictBase):
    region_id: UUID4
    name: str
  

# Properties to receive via API on update
class DistrictUpdate(DistrictBase):
    pass

class DistrictInDBBase(DistrictBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class DistrictSchema(DistrictInDBBase):

    #matters = Optional[List[MatterSchema]]
    courts = Optional[List[CourtSchema]]


# Additional properties to return via API
class DistrictCourtsSchema(DistrictInDBBase):

    #matters = Optional[List[MatterSchema]]
    courts = Optional[List[CourtSchema]]

# Additional properties stored in DB
class DistrictInDB(DistrictInDBBase):
    pass
