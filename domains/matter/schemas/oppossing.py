from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.common.schemas.comment import CommentSchema
from app.domains.matter.schemas.phase_code import PhaseCodeSchema
from app.domains.matter.schemas.matter import MatterSchema


#Opposing
class OppossingBase(BaseModel):
   
    opposing_type: Optional[str] = None 
    matter_id: Optional[UUID4] = None
    first_name: Optional[str] = None 
    last_namer: Optional[str] = None 
    description: Optional[str] = None 
    email: Optional[str] = None 
    phone: Optional[str] = None   


# Properties to receive via API on creation
class OppossingCreate(OppossingBase): 
    opposing_type: str
    matter_id: UUID4 
    first_name: UUID4
    last_name: UUID4

     
# Properties to receive via API on update
class OppossingUpdate(OppossingBase):
   pass


class OppossingInDBBase(OppossingBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class OppossingSchema(OppossingInDBBase):
    
    matter: Optional[MatterSchema] = None 

    

