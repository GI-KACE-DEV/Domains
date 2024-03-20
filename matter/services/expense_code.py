from app.domains.matter.models.expense_code import  ExpenseCode
from app.crud.base import CRUDBase

from app.domains.matter.schemas.expense_code import (
     ExpenseCodeCreate, ExpenseCodeUpdate
)

class CRUDExpenseCode(CRUDBase[ExpenseCode, ExpenseCodeCreate, ExpenseCodeUpdate]):
    pass

    
expense_code_actions = CRUDExpenseCode(ExpenseCode)

