from app.crud.base import CRUDBase
from .. import models
from ..schemas import  (
    DesignationCreate, DesignationUpdate
)

class CRUDDesignation(CRUDBase[models.Designation,DesignationCreate, DesignationUpdate]):
    pass
    

designation_actions = CRUDDesignation(models.Designation)

