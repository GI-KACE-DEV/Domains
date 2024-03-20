from app.domains.crm import models
from app.crud.base import CRUDBase

from app.domains.crm.schemas.consultation import  (
    ConsultationCreate, ConsultationUpdate,  ConsultationSchema
)

class CRUDConsultation(CRUDBase[models.Consultation,ConsultationCreate, ConsultationUpdate]):
    pass
    

consultation_actions = CRUDConsultation(models.Consultation)

#add every custom business logic here 