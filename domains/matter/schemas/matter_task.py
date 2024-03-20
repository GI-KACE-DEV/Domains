from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date

from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.common.schemas.comment import CommentSchema
from app.domains.matter.schemas.matter import MatterSchema

#MatterTask
class MatterTaskBase(BaseModel):
    
    title: Optional[str] = None
    description: Optional[str] = None
    matter_id: Optional[UUID4] = None
    assigner_id: Optional[UUID4] = None
    assignee_id:Optional[UUID4] = None
    expected_start_date: Optional[datetime] = None
    expected_due_date: Optional[str] = None
    actual_start_date: Optional[str] = None
    actual_end_date: Optional[str] = None
    status:Optional[str] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None 
    

# Properties to receive via API on creation
class MatterTaskCreate(MatterTaskBase): 
    title: Optional[str] 
    description: Optional[str] 
    matter_id: Optional[UUID4] 
    assigner_id: Optional[UUID4] 
    assignee_id:Optional[UUID4] 

# Properties to receive via API on update
class MatterTaskUpdate(MatterTaskBase):
   pass


class MatterTaskInDBBase(MatterTaskBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class MatterTaskSchema(MatterTaskInDBBase):
    
    matter: Optional[MatterSchema] = None 

    #staff
    assignee: Optional[StaffSchema] = None
    
    assigner = Optional[StaffSchema]  = None
    

