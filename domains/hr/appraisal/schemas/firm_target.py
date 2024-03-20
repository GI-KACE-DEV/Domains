from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date
from .review_period import ReviewPeriodSchema


class HTTPError(BaseModel):
    detail: str


# Shared properties
class FirmTargetBase(BaseModel):
    title: Optional[str]
    description: Optional[str]
    review_period_id: Optional[UUID4]
    success_indicator: Optional[str]
    minimum_rating: Optional[float]
    maximum_rating: Optional[float]
    start_date: Optional[date]
    end_date: Optional[date]
    year: Optional[int]


# Properties to receive via API on creation
class FirmTargetCreate(FirmTargetBase):
    title: str
    review_period_id: UUID4
    year: int


# Properties to receive via API on update
class FirmTargetUpdate(FirmTargetBase):
   pass


class FirmTargetInDBBase(FirmTargetBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class FirmTargetSchema(FirmTargetInDBBase):
   review_period: Optional[ReviewPeriodSchema]