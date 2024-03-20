from typing import Any, Dict, List, Optional, Union
#from typing import (
#    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
#)
from uuid import UUID
import datetime
from pydantic import BaseModel
from datetime import  datetime

from  app.domains.hr.staff.schemas import StaffSchema


class HTTPError(BaseModel):
    detail: str


# Shared properties
class CommentBase(BaseModel):
    
    comment: Optional[str] = None
    commented_on: Optional[datetime] = None
    staff_id: Optional[UUID] = None
    
   
      
# Properties to receive via API on creation
class CommentCreate(CommentBase):
    
    comment: str
    commented_on: str
    staff_id: UUID
    
    
# Properties to receive via API on update
class CommentUpdate(CommentBase):
    #name: Optional[str] = None
    #start_date_time: Optional[datetime] = False
    pass


class CommentInDBBase(CommentBase):
    id: Optional[UUID] = None
    comment: str
    commented_on: str
    staff_id: UUID

    class Config:
        orm_mode = True


# Additional properties to return via API
class CommentSchema(CommentInDBBase):
    
    commented_by: Optional[List[UUID]]   
    leads: Optional[List[UUID]]

        
# Additional properties stored in DB
class CommentInDB(CommentInDBBase):
    pass