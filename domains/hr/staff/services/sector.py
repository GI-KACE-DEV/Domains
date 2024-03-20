from app.crud.base import CRUDBase
#from .. import models
from app.domains.common.models.sector import Sector

from ..schemas import  (
    SectorCreate, SectorUpdate
)

class CRUDSector(CRUDBase[Sector,SectorCreate, SectorUpdate]):
    pass
    

sector_actions = CRUDSector(Sector)

