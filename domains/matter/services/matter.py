from app.domains.matter.models.matter import  Expense
from app.crud.base import CRUDBase

from app.domains.matter.schemas.matter import (
     ExpenseCreate, ExpenseUpdate
)

class CRUDExpense(CRUDBase[Expense, ExpenseCreate, ExpenseUpdate]):
    pass

    
matter_actions = CRUDExpense(Expense)

