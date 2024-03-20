from app.domains.matter.models.region import  Region
from app.crud.base import CRUDBase

from app.domains.matter.schemas.region import (
     RegionCreate, RegionUpdate
)

class CRUDRegion(CRUDBase[Region, RegionCreate, RegionUpdate]):
    pass

    
region_actions = CRUDRegion(Region)

