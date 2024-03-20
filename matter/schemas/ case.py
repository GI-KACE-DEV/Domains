from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, UUID4
from datetime import datetime , date

from app.domains.hr.staff.schemas import StaffSchema
from .matter import MatterSchema

from .opposing_party import OpposingPartySchema
from .opposing_party_lawyer import OpposingPartyLawyerSchema
from .court import CourtSchema
from .document import DocumentSchema
from .hearing import HearingSchema
from .note import NoteSchema
from .journal import JournalSchema
from .action import ActionSchema
from .notification import NotificationSchema

from .expense import ExpenseSchema
from .activity import ActivitySchema
from .phase import PhaseSchema
from .task import TaskSchema


# Shared properties
class CaseBase(BaseModel):

    title: Optional[str] = None
    suite_number: Optional[str] = None
    brief: Optional[str] = None 
    matter_id: Optional[UUID4]  = None
    start_date: Optional[date] = None 
    end_date:Optional[date] = None    
    status: Optional[str] = None

    opposing_party_ids = Optional [List[UUID4]] = []
    opposing_party_lawyer_ids = Optional[List[UUID4]] = []
    court_ids = Optional[List[UUID4]] = []
    hearing_ids = Optional[List[UUID4]] = []
    journal_ids = Optional[List[UUID4]] = []
    document_ids = Optional[List[UUID4]] = []
    notification_ids = Optional[List[UUID4]] = []

    matter: Optional[MatterSchema] = None
    opposing_parties: Optional[List[OpposingPartySchema]] = None
    opposing_party_lawyers: Optional[
                List[OpposingPartyLawyerSchema]] = None
    hearing: Optional[List[HearingSchema]] = []
    notes: Optional[List[NoteSchema]] = []
    journals: Optional[List[JournalSchema]] = []
    documents: Optional[List[DocumentSchema]] = []
    team: Optional[List[StaffSchema]] = [] 
    courts: Optional[List[CourtSchema]] = []
    expenses: Optional[List[ExpenseSchema]] = []
    expenses: Optional[List[ExpenseSchema]] = []
    actions: Optional[List[ActionSchema]] = []
    

# Properties to receive via API on creation
class CaseCreate(CaseBase):
    name: str
    location: Optional[str] = None
    #department_head_id: Optional[UUID] = None


# Properties to receive via API on update
class CaseUpdate(CaseBase):
    name: Optional[str] = None
    location: Optional[str] = None


class CaseInDBBase(CaseBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class CaseSchema(CaseInDBBase):
    pass


# Additional properties stored in DB
class CaseInDB(CaseInDBBase):
    pass







  