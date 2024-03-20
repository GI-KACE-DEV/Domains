from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from .department_target import DepartmentTargetSchema
from .review_period import ReviewPeriodSchema
from app.domains.hr.staff.schemas import StaffSchema

class HTTPError(BaseModel):
    detail: str



# Shared properties
class DepartmentAppraisalBase(BaseModel):
    quality_score: Optional[float] = None
    efficiency_score: Optional[float] = None
    timeliness_score: Optional[float] = None
    accuracy_score: Optional[float] = None
    evaluator_remarks: Optional[str] = None
    department_remarks: Optional[str]
    date_recorded: Optional[date]
    status: Optional[str]
    evaluator_id:  Optional[UUID4]
    review_period_id:  Optional[UUID4]
    department_target_id:  Optional[UUID4]



# Properties to receive via API on creation
class DepartmentAppraisalCreate(DepartmentAppraisalBase):
    evaluator_id:  UUID4
    department_target_id: UUID4



# Properties to receive via API on update
class DepartmentAppraisalUpdate(DepartmentAppraisalBase):
   pass


class DepartmentAppraisalInDBBase(DepartmentAppraisalBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class DepartmentAppraisalSchema(DepartmentAppraisalInDBBase):
    evaluator: Optional[StaffSchema] = None
    review_period: Optional[ReviewPeriodSchema]
    department_target: Optional[DepartmentTargetSchema]