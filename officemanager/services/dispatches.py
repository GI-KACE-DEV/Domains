from app.domains.officemanager.models.dispatch import Incoming, Outgoing
from app.crud.base import CRUDBase
from app.domains.officemanager.schemas.dispatches import  (
    IncomingCreate, IncomingUpdate,
    OutgoingCreate, OutgoingUpdate
)

class CRUDIncoming(CRUDBase[Incoming, IncomingCreate, IncomingUpdate]):
    pass
    

incoming_actions = CRUDIncoming(Incoming)
    

class CRUDOutgoing(CRUDBase[Outgoing, OutgoingCreate, OutgoingUpdate]):
    pass
    

outgoing_actions = CRUDOutgoing(Outgoing)
    
