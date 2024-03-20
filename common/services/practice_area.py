from app.domains.common.models.practice_area import PracticeArea
from app.crud.base import CRUDBase

from app.domains.common.schemas.practice_area import  (
    PracticeAreaCreate, PracticeAreaUpdate,PracticeAreaSchema
)

class CRUDPracticeArea(CRUDBase[PracticeArea,PracticeAreaCreate, PracticeAreaUpdate]):
    pass
    


practice_area_actions = CRUDPracticeArea(PracticeArea)

