from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime, date
from app.domains.hr.staff.schemas import (SectorSchema, StaffSchema,
                                          PracticeAreaSchema, TeamSchema
                                          )

from app.domains.crm.schemas.contact import ContactSchema
from app.domains.common.schemas.action import ActionSchema
from app.domains.common.schemas.comment import CommentSchema
from app.domains.common.schemas.attachment import AttachmentSchema
from app.domains.common.schemas.tag import TagSchema


class HTTPError(BaseModel):
    detail: str


# Lead
class LeadBase(BaseModel):

    description: Optional[str] = None
    salutation: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    primary_email:  Optional[str] = None
    secondary_email: Optional[str] = None
    primary_cellphone: Optional[str] = None
    secondary_cellphone: Optional[str] = None
    # source_id: Optional[UUID4] = None
    source: Optional[str] = None
    address_line: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state_region: Optional[str] = None
    postcode: Optional[str] = None
    website: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    estimated_value: Optional[float] = None
    probability: Optional[float] = None
    creator_id: Optional[UUID4] = None
    updator_id: Optional[UUID4] = None


# Properties to receive via API on creation
class LeadCreate(LeadBase):

    description: Optional[str] = None
    salutation: Optional[str] = None
    first_name: Optional[str] = None
    primary_email:  Optional[str] = None
    primary_cellphone: Optional[str] = None

    # sector_ids: Optional[List[UUID4]] = []
    # practice_area_ids: Optional[List[UUID4]] = []


# Properties to receive via API on update
class LeadUpdate(LeadBase):
    pass


class LeadInDBBase(LeadBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class LeadSchema(LeadInDBBase):

    sectors: Optional[SectorSchema] = []
    practice_areas: Optional[PracticeAreaSchema] = []
    attachments: Optional[AttachmentSchema] = []
    contacts: Optional[ContactSchema] = []

    # m2m fields
    # team_managers: List[TeamSchema] = []
    account_managers: Optional[List[StaffSchema]] = []
    comments: Optional[List[CommentSchema]] = []
    sectors: Optional[List[SectorSchema]] = []
    practice_areas: Optional[PracticeAreaSchema] = []

    # created_or:Optional[StaffSchema] = None
    # updator_id: Optional[StaffSchema] = None

    def dict(self, *args, **kwargs) -> dict[str, Any]:
        """
            Override the default dict method to exclude None values in the response
        """
        kwargs.pop('exclude_none', None)
        return super().dict(*args, exclude_none=True, **kwargs)

    # actions: Optional[List[ActionSchema]] = []


# Lead with actions
class LeadActionSchema(LeadSchema):
    actions: List[ActionSchema] = []
