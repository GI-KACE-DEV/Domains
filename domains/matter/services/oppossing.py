from app.domains.matter.models.oppossing import Opposing
from app.crud.base import CRUDBase

from app.domains.matter.schemas.opposing import (
     OpposingCreate, OpposingUpdate
)

class CRUDOpposing(CRUDBase[Opposing, OpposingCreate, OpposingUpdate]):
    pass

    
opposing_actions = CRUDOpposing(Opposing)

