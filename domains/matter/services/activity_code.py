from app.domains.matter.models.activity_code import  ActivityCode
from app.crud.base import CRUDBase

from app.domains.matter.schemas.activity_code import (
    ActivityCodeSchema, ActivityCodeCreate, ActivityCodeUpdate
)

class CRUDActivityCode(CRUDBase[ActivityCode, ActivityCodeCreate, ActivityCodeUpdate]):
    pass

    
activity_code_actions = CRUDActivityCode(ActivityCode)

