from app.domains.matter.models.task_code import  TaskCode
from app.crud.base import CRUDBase

from app.domains.matter.schemas.task_code import (
     TaskCodeCreate, TaskCodeUpdate
)

class CRUDTaskCode(CRUDBase[TaskCode, TaskCodeCreate, TaskCodeUpdate]):
    pass

    
task_code_actions = CRUDTaskCode(TaskCode)

