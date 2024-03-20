from app.domains.matter.models.opposing_party import  OpposingParty
from app.crud.base import CRUDBase

from app.domains.matter.schemas.opposing_party import (
     OpposingPartyCreate, OpposingPartyUpdate
)

class CRUDOpposingParty(CRUDBase[OpposingParty, OpposingPartyCreate, OpposingPartyUpdate]):
    pass

    
oppossing_party_actions = CRUDOpposingParty(OpposingParty)

