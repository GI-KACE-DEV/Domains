from app.domains.hr.staff import models
from app.crud.base import CRUDBase

from app.domains.hr.staff.schemas import (
    DepartmentCreate, DepartmentUpdate, DepartmentSchema
)


class CRUDDepartment(CRUDBase[models.Department, DepartmentCreate, DepartmentUpdate]):
    pass


department_actions = CRUDDepartment(models.Department)
