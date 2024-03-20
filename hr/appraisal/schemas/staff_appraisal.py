from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from .department_target import DepartmentTargetSchema
from .review_period import ReviewPeriodSchema
from app.domains.hr.staff.schemas import StaffSchema


class HTTPError(BaseModel):
    detail: str


# Shared properties
class StaffAppraisalBase(BaseModel):
    quality_score: Optional[float] = None
    efficiency_score: Optional[float] = None
    timeliness_score: Optional[float] = None
    accuracy_score: Optional[float] = None
    evaluator_remarks: Optional[str] = None
    staff_remarks: Optional[str] = None
    staff_target_id:  Optional[UUID4] = None
    evaluator_id:  Optional[UUID4] = None
    review_period_id:  Optional[UUID4] = None
    status: Optional[str] = None


# Properties to receive via API on creation
class StaffAppraisalCreate(StaffAppraisalBase):
    evaluator_id:  UUID4
    staff_target_id: UUID4


# Properties to receive via API on update
class StaffAppraisalUpdate(StaffAppraisalBase):
   pass


class StaffAppraisalInDBBase(StaffAppraisalBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class StaffAppraisalSchema(StaffAppraisalInDBBase):
    evaluator: Optional[StaffSchema] = None
    review_period: Optional[ReviewPeriodSchema]
    department_target: Optional[DepartmentTargetSchema]