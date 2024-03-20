from app.domains.common import models
from app.crud.base import CRUDBase

from app.domains.hr.staff.schemas import  (
    ContactCreate, ContactUpdate, ContactSchema
)

class CRUDContact(CRUDBase[models.ContactCreate, ContactUpdate]):
    pass
    

contact_actions = CRUDContact(models.Contact)

