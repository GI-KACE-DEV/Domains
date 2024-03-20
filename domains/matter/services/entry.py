from app.domains.matter.models.entry import  Entry
from app.crud.base import CRUDBase

from app.domains.matter.schemas.entry import (
     EntryCreate, EntryUpdate
)

class CRUDEntry(CRUDBase[Entry, EntryCreate, EntryUpdate]):
    pass

    
entry_actions = CRUDEntry(Entry)

