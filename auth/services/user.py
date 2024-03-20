# from app.domains.hr.staff import models
from app.domains.auth import models

from app.crud.base import CRUDBase

from app.domains.auth.schemas.user import (
    UserCreate, UserUpdate
)


class CRUDUser(CRUDBase[models.User, UserCreate, UserUpdate]):
    pass


user_actions = CRUDUser(models.User)
