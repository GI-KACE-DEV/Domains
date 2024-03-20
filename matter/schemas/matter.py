from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date

from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.common.schemas.comment import CommentSchema
from pydantic import EmailStr

#Matter
class MatterBase(BaseModel):
    reference_number: Optional[str] = None 
    brief:Optional[str] = None
    client_id: Optional[UUID4] = None
    authourized_representative: Optional[str] = None
    authourized_representative_email: Optional[EmailStr] = None
    authourized_representative_phone: Optional[str] = None
    nature_of_engagement: Optional[str] = None
    fee =  Optional[float] = None
    date_of_engagement: Optional[date] = None
    assistance_required_from_partners: Optional[str] = None
    special_observations_remarks: Optional[str] = None 
    fee: Optional[float] = None
    
    
# Properties to receive via API on creation
class MatterCreate(MatterBase): 
    #reference_number: Optional[str] = None 
    brief:str
    client_id: UUID4 | None
    authourized_representative: str
    authourized_representative_phone: Optional[str] = None
    nature_of_engagement: Optional[str] = None
    date_of_engagement: Optional[date] = None
    assistance_required_from_partners: Optional[str] = None
    
    #creator_id: Optional[UUID]  = None
    #updator_id: Optional[UUID] = None 
    
   

# Properties to receive via API on update
class MatterUpdate(MatterBase):
   pass


class MatterInDBBase(MatterBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class MatterSchema(MatterInDBBase):
    pass
    
   




   