from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime , date
from app.domains.hr.staff.schemas import (SectorSchema, StaffSchema, 
        PracticeAreaSchema, TeamSchema
    ) 

from app.domains.crm.schemas.contact import ContactSchema
from app.domains.common.schemas.action import ActionSchema
from app.domains.common.schemas.comment import CommentSchema
from app.domains.common.schemas.attachment import AttachmentSchema
from app.domains.common.schemas.tag import TagSchema
from pydantic import UUID4
import decimal

from app.domains.crm.schemas.client import ClientSchema

class HTTPError(BaseModel):
    detail: str


#Consultation
class ConsultationBase(BaseModel):

    client_id: Optional[UUID4] = None
    title: Optional[str] = None
    brief:Optional[str] = None 
    remarks: Optional[str]  = None  
    #estimated_value:Optional[decimal.Decimal] = None
    #probability:Optional[decimal.Decimal]   = None
    #consulting_fee: Optional[decimal.Decimal] = 0.0
    estimated_value:Optional[float] = None
    probability:Optional[float]   = None
    consulting_fee: Optional[float] = None
    is_paid: Optional[bool] = False
    start_date: Optional[datetime]= None
    end_date: Optional[datetime] = None  
    assigned_to: List[UUID] = []
    lead_counsel_id:Optional[UUID] = None
    creator_id: Optional[UUID]= None
    updator_id: Optional[UUID] = None
   
   
# Properties to receive via API on creation
class ConsultationCreate(ConsultationBase):
    
    client_id: UUID
    title: str
    brief: str
    
   
# Properties to receive via API on update
class ConsultationUpdate(ConsultationBase):
   pass


class ConsultationInDBBase(ConsultationBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True

# Additional properties to return via API
class ConsultationSchema(ConsultationInDBBase):
    
    #attachments: Optional[AttachmentSchema] = []
    client: ClientSchema
    lead_counsel: Optional[StaffSchema] = None
    assigned_to: Optional[List[StaffSchema]] = []

    #m2m fields
    #team_managers: List[TeamSchema] = []
    #account_managers: List[StaffSchema] = []
    comments: List[CommentSchema] = []
    sectors: Optional[List[UUID]] = []
    practice_areas: Optional[List[UUID]] = []
    actions: List[ActionSchema] = []


#Consultation with actions
class ConsultationActionSchema(ConsultationSchema):
    actions: List[ActionSchema] = []
    

    