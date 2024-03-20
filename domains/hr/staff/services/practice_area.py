#from app.domains.hr.staff import models
from app.domain.common.models import practice_area as models

from app.crud.base import CRUDBase

from app.domains.hr.staff.schemas import  (
    PracticeAreaCreate, PracticeAreaUpdate
)

class CRUDPracticeArea(CRUDBase[models.PracticeArea, PracticeAreaCreate, PracticeAreaUpdate]):
    pass
    


practice_area_actions = CRUDPracticeArea(models.PracticeArea)

