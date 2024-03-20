from app.domains.matter.models.note import  Note
from app.crud.base import CRUDBase

from app.domains.matter.schemas.note import (
     NoteCreate, NoteUpdate
)

class CRUDNote(CRUDBase[Note, NoteCreate, NoteUpdate]):
    pass

    
note_actions = CRUDNote(Note)

