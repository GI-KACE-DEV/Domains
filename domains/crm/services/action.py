from app.domains.common.models.action import Action
from app.crud.base import CRUDBase

from app.domains.common.schemas import (
    ActionCreate, ActionUpdate, ActionSchema
)


class CRUDAction(CRUDBase[Action, ActionCreate, ActionUpdate]):
    pass


action_actions = CRUDAction(Action)
