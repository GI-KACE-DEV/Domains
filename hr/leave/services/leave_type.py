from app.domains.hr.leave.models.leave_type import  LeaveType
from app.crud.base import CRUDBase

from app.domains.hr.leave.schemas.leave_type import (
    LeaveTypeCreate, LeaveTypeUpdate
)

class CRUDClient(CRUDBase[LeaveType, LeaveTypeCreate, LeaveTypeUpdate]):
    pass

    

leave_type_actions = CRUDClient(LeaveType)

