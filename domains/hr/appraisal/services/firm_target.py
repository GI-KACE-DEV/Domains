from app.domains.hr.appraisal import models
from app.crud.base import CRUDBase
from app.domains.hr.appraisal import models

from app.domains.hr.appraisal.schemas import  (
    FirmTargetCreate, FirmTargetUpdate
)

class CRUDFirmTarget(CRUDBase[models.FirmTarget,FirmTargetCreate, FirmTargetUpdate]):
    pass
    

firm_target_actions = CRUDFirmTarget(models.FirmTarget)

