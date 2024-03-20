from app.domains.matter.models.trial import  Trial
from app.crud.base import CRUDBase

from app.domains.matter.schemas.trial import (
     TrialCreate, TrialUpdate
)

class CRUDTrial(CRUDBase[Trial, TrialCreate, TrialUpdate]):
    pass

    
trial_actions = CRUDTrial(Trial)

