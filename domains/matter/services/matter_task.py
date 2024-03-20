from app.domains.matter.models.matter_task import  MatterTask
from app.crud.base import CRUDBase

from app.domains.matter.schemas.matter_task import (
     MatterTaskCreate, MatterTaskUpdate
)

class CRUDMatterTask(CRUDBase[MatterTask, MatterTaskCreate, MatterTaskUpdate]):
    pass

    
matter_task_actions = CRUDMatterTask(MatterTask)

