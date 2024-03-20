from app.domains.matter.models.category import  Category
from app.crud.base import CRUDBase

from app.domains.matter.schemas.category import (
    CategorySchema, CategoryCreate, CategoryUpdate
)

class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    pass

    
category_actions = CRUDCategory(Category)

