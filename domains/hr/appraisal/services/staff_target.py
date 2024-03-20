from app.domains.hr.appraisal import models
from app.crud.base import CRUDBase

from app.domains.hr.appraisal.schemas import  (
    StaffTargetCreate, StaffTargetUpdate,StaffTargetSchema
)

class CRUDStaffTarget(CRUDBase[models.StaffTarget,StaffTargetCreate, StaffTargetUpdate]):
    pass
    
    
staff_target_actions = CRUDStaffTarget(models.StaffTarget)

