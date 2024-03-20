from app.domains.hr.leave.models.annual_leave import  AnnualLeave
from app.crud.base import CRUDBase

from app.domains.hr.leave.schemas.annual_leave import (
    AnnualLeaveSchema, AnnualLeaveCreate, AnnualLeaveUpdate
)

class CRUDClient(CRUDBase[AnnualLeave, AnnualLeaveCreate, AnnualLeaveUpdate]):
    pass

    
annual_leave_actions = CRUDClient(AnnualLeave)

