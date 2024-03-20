from app.domains.matter.models.judge import  Judge
from app.crud.base import CRUDBase

from app.domains.matter.schemas.judge import (
     JudgeCreate, JudgeUpdate
)

class CRUDJudge(CRUDBase[Judge, JudgeCreate, JudgeUpdate]):
    pass

    
judge_actions = CRUDJudge(Judge)

