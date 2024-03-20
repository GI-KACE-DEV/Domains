from app.domains.matter.models.type import  Type
from app.crud.base import CRUDBase

from app.domains.matter.schemas.type import (
     TypeCreate, TypeUpdate
)

class CRUDType(CRUDBase[Type, TypeCreate, TypeUpdate]):
    pass

    
type_actions = CRUDType(Type)

