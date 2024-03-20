from app.domains.common.models.action import Reminder
from app.crud.base import CRUDBase

from app.domains.common.schemas.reminder import  (
    ReminderCreate, ReminderUpdate,ReminderSchema
)

class CRUDReminder(CRUDBase[Reminder,ReminderCreate, ReminderUpdate]):
    pass
    


reminder_actions = CRUDReminder(Reminder)

