from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date
from app.domains.hr.staff.schemas import (StaffSchema,  TeamSchema)
from app.domains.common.schemas.comment import CommentSchema


class HTTPError(BaseModel):
    detail: str


# Action
class ActionBase(BaseModel):

    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    start_date_time: Optional[datetime] = None
    close_date_time: Optional[datetime] = None
    duration: Optional[int] = None
    status_id: Optional[UUID] = None
    is_active: Optional[UUID] = None

    assigned_to_ids: Optional[List[UUID]] = None
    team_ids: Optional[List[UUID]] = None
    contact_ids: Optional[List[UUID]] = None


# Properties to receive via API on creation
class ActionCreate(ActionBase):
    name: str
    description: str
    start_date_time: datetime


# Properties to receive via API on update
class ActionUpdate(ActionBase):
    pass


class ActionInDBBase(ActionBase):
    id: Optional[UUID] = None
    creator_id: Optional[UUID] = None
    updator_id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ActionSchema(ActionInDBBase):

    team: Optional[List[TeamSchema]] = []
    assigned_to: Optional[List[StaffSchema]] = []
    comments: Optional[List[CommentSchema]] = []
