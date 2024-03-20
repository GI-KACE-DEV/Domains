from app.domains.hr.appraisal import models
from app.crud.base import CRUDBase

from app.domains.hr.appraisal.schemas import  (
    StaffAppraisalCreate, StaffAppraisalUpdate,StaffAppraisalSchema
)

class CRUDStaffAppraisal(CRUDBase[models.StaffAppraisal,StaffAppraisalCreate, StaffAppraisalUpdate]):
    pass
    
    
staff_appraisal_actions = CRUDStaffAppraisal(models.StaffAppraisal)

