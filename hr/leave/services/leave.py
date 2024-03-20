from app.domains.hr.leave.models.leave import  Leave
from app.crud.base import CRUDBase

from app.domains.hr.leave.schemas.leave import (
    LeaveSchema, LeaveCreate, LeaveUpdate
)

class CRUDClient(CRUDBase[Leave, LeaveCreate, LeaveUpdate]):
    pass

    

leave_actions = CRUDClient(Leave)

