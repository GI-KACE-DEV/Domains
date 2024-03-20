from typing import Any, Dict, List, Optional, Union
from datetime import datetime , date

from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime , date
from app.domains.hr.staff.schemas import ( StaffSchema,  TeamSchema) 
from app.domains.common.schemas.comment import CommentSchema
from app.domains.matter.schemas.phase_code import PhaseCodeSchema
from app.domains.matter.schemas.matter import MatterSchema


# Properties to receive via API on creation
class PhaseCodeBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None


class PhaseCodeCreate(PhaseCodeBase):
    name: str
    code: str


# Properties to receive via API on update
class PhaseCodeUpdate(PhaseCodeBase):
    pass


class PhaseCodeInDBBase(PhaseCodeBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class PhaseCodeSchema(PhaseCodeInDBBase):
    pass


# Additional properties stored in DB
class PhaseCodeInDB(PhaseCodeInDBBase):
    pass

