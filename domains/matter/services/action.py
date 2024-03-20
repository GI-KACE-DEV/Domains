from app.domains.matter.models.action import  Action
from app.crud.base import CRUDBase

from app.domains.matter.schemas.action import (
    ActionSchema, ActionCreate, ActionUpdate
)

class CRUDAction(CRUDBase[Action, ActionCreate, ActionUpdate]):
    pass

    
action_actions = CRUDAction(Action)

