from app.domains.hr.appraisal import models
from app.crud.base import CRUDBase

from app.domains.hr.appraisal.schemas.department_target import  (
    DepartmentTargetCreate, DepartmentTargetUpdate
)

class CRUDDepartmentTarget(CRUDBase[models.DepartmentTarget,DepartmentTargetCreate, DepartmentTargetUpdate]):
    pass
    


department_target_actions = CRUDDepartmentTarget(models.DepartmentTarget)

