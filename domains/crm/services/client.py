from app.domains.crm.models  import client as  models
from app.crud.base import CRUDBase

from app.domains.crm.schemas.client import  (
    ClientCreate, ClientUpdate,ClientSchema
)

class CRUDClient(CRUDBase[models.Client,ClientCreate, ClientUpdate]):
    pass
    

client_actions = CRUDClient(models.Client)

