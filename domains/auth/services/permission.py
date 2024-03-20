#from app.domains.hr.staff import models
from app.domains.auth import models 

from app.crud.base import CRUDBase

from app.domains.auth.schemas.permission import  (
    PermissionCreate, PermissionUpdate
)

class CRUDPermission(CRUDBase[models.Permission, PermissionCreate, PermissionUpdate]):
    pass
    

permission_actions = CRUDPermission(models.Permission)

