from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date

from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.common.schemas.comment import CommentSchema


#ExpenseCode
class ExpenseCodeBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None 
    code: Optional[str] = None 

   
# Properties to receive via API on creation
class ExpenseCodeCreate(ExpenseCodeBase): 
    name: Optional[str] = None
    code: Optional[] = None 

    
# Properties to receive via API on update
class ExpenseCodeUpdate(ExpenseCodeBase):
   pass


class ExpenseCodeInDBBase(ExpenseCodeBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ExpenseCodeSchema(ExpenseCodeInDBBase):
    pass
    
   





