from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from .review_period import ReviewPeriodSchema
from .firm_target import FirmTargetSchema

class HTTPError(BaseModel):
    detail: str



# Shared properties
class DepartmentTargetBase(BaseModel):
    title: Optional[str]
    description: Optional[str]
    review_period_id: Optional[UUID4]
    success_indicator: Optional[str]
    minimum_rating: Optional[float]
    maximum_rating: Optional[float]
    start_date: Optional[date]
    end_date: Optional[date]
    firm_target_id: Optional[UUID4]
    review_period_id: Optional[UUID4]
       

    
# Properties to receive via API on creation
class DepartmentTargetCreate(DepartmentTargetBase):
    title: str
    review_period_id: UUID4
    firm_target_id: UUID4


# Properties to receive via API on update
class DepartmentTargetUpdate(DepartmentTargetBase):
   pass


class DepartmentTargetInDBBase(DepartmentTargetBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class DepartmentTargetSchema(DepartmentTargetInDBBase):
   review_period: Optional[ReviewPeriodSchema]
   firm_target : Optional[FirmTargetSchema]