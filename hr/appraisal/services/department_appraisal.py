from app.domains.hr.appraisal import models
from app.crud.base import CRUDBase

from app.domains.hr.appraisal.schemas import  (
    DepartmentAppraisalCreate, DepartmentAppraisalUpdate,DepartmentAppraisalSchema
)

class CRUDDepartmentAppraisal(CRUDBase[models.DepartmentAppraisal,DepartmentAppraisalCreate, DepartmentAppraisalUpdate]):
    pass
    

department_appraisal_actions = CRUDDepartmentAppraisal(models.DepartmentAppraisal)

