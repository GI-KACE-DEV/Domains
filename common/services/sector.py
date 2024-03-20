from app.domains.common.models.sector import Sector
from app.crud.base import CRUDBase

from app.domains.common.schemas.sector import  (
    SectorCreate, SectorUpdate,SectorSchema
)

class CRUDSector(CRUDBase[Sector,SectorCreate, SectorUpdate]):
    pass
    
sector_actions = CRUDSector(Sector)

