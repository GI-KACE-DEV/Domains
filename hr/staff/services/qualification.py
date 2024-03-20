from app.crud.base import CRUDBase
from .. import models
from ..schemas import  (
    QualificationCreate, QualificationUpdate
)

class CRUDQualification(CRUDBase[models.Qualification,QualificationCreate, QualificationUpdate]):
    pass
    

qualification_actions = CRUDQualification(models.Qualification)

