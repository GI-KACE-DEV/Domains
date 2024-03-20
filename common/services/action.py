from app.domains.common.models import action as models
from app.crud.base import CRUDBase

from app.domains.common.schemas.action import  (
    ActionCreate, ActionUpdate,ActionSchema
)

class CRUDAction(CRUDBase[models.Action,ActionCreate, ActionUpdate]):
    pass
    

action_actions = CRUDAction(models.Action)

