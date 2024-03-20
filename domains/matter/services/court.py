from app.domains.matter.models.court import  Court
from app.crud.base import CRUDBase

from app.domains.matter.schemas.court import (
     CourtCreate, CourtUpdate
)

class CRUDCourt(CRUDBase[Court, CourtCreate, CourtUpdate]):
    pass

    
court_actions = CRUDCourt(Court)

