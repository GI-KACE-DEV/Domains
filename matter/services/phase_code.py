from app.domains.matter.models.phase_code import  PhaseCode
from app.crud.base import CRUDBase

from app.domains.matter.schemas.phase_code import (
     PhaseCodeCreate, PhaseCodeUpdate
)

class CRUDPhaseCode(CRUDBase[PhaseCode, PhaseCodeCreate, PhaseCodeUpdate]):
    pass

    
phase_code_actions = CRUDPhaseCode(PhaseCode)

