from app.domains.crm import models
from app.crud.base import CRUDBase

from app.domains.crm.schemas.lead import  (
    LeadCreate, LeadUpdate,LeadSchema
)

class CRUDLead(CRUDBase[models.Lead, LeadCreate, LeadUpdate]):
    pass
    

lead_actions = CRUDLead(models.Lead)

