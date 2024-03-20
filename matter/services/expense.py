from app.domains.matter.models.expense import  Expense
from app.crud.base import CRUDBase

from app.domains.matter.schemas.expense import (
     ExpenseCreate, ExpenseUpdate
)

class CRUDExpense(CRUDBase[Expense, ExpenseCreate, ExpenseUpdate]):
    pass

    
expense_actions = CRUDExpense(Expense)

