from app.domains.matter.models.notification import  Notification
from app.crud.base import CRUDBase

from app.domains.matter.schemas.notification import (
     NotificationCreate, NotificationUpdate
)

class CRUDNotification(CRUDBase[Notification, NotificationCreate, NotificationUpdate]):
    pass

    
notification_actions = CRUDNotification(Notification)

