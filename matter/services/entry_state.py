from app.domains.matter.models.entry_state import  EntryState
from app.crud.base import CRUDBase

from app.domains.matter.schemas.entry_state import (
     EntryStateCreate, EntryStateUpdate
)

class CRUDEntryState(CRUDBase[EntryState, EntryStateCreate, EntryStateUpdate]):
    pass

    
entry_state_actions = CRUDEntryState(EntryState)

