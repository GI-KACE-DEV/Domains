from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.common.schemas.comment import CommentSchema
from app.domains.matter.schemas.phase_code import PhaseCodeSchema
from app.domains.matter.schemas.matter import MatterSchema


#Expense
class ExpenseBase(BaseModel):
   
    description: Optional[str] = None 
    matter_id: Optional[str] = None
    expense_code_id: Optional[UUID4] = None
    phase_code_id: Optional[UUID4] = None 
    amount: Optional[float] = 0.0
    date: Optional[date] = None 
    #responsible = Optional[UUID4] = None
    
    
# Properties to receive via API on creation
class ExpenseCreate(ExpenseBase): 
    
    description: Optional[str] = None 
    matter_id: Optional[str] = None
    expense_code_id: Optional[UUID4] = None
    phase_code_id: Optional[UUID4] = None 
    

# Properties to receive via API on update
class ExpenseUpdate(ExpenseBase):
   pass


class ExpenseInDBBase(ExpenseBase):
    id: Optional[UUID4] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ExpenseSchema(ExpenseInDBBase):
    
    phase_code: Optional[PhaseCodeSchema] = None
    matter: Optional[MatterSchema] = None 
