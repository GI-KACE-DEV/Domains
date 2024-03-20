#from app.domains.hr.staff import models
from app.domains.auth import models 

from app.crud.base import CRUDBase

from app.domains.auth.schemas.role import  (
    RoleCreate, RoleUpdate
)

class CRUDRole(CRUDBase[models.Role, RoleCreate, RoleUpdate]):
    pass
    

role_actions = CRUDRole(models.Role)

