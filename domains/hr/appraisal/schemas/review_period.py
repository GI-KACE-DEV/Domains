from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date


class HTTPError(BaseModel):
    detail: str


# Shared properties
class ReviewPeriodBase(BaseModel):
    title: Optional[str]
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    year: Optional[int]

    
# Properties to receive via API on creation
class ReviewPeriodCreate(ReviewPeriodBase):
    title: str
    year: int

# Properties to receive via API on update
class ReviewPeriodUpdate(ReviewPeriodBase):
   pass


class ReviewPeriodInDBBase(ReviewPeriodBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ReviewPeriodSchema(ReviewPeriodInDBBase):
   pass