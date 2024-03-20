from app.domains.matter.models.district import  District
from app.crud.base import CRUDBase

from app.domains.matter.schemas.district import (
     DistrictCreate, DistrictUpdate
)

class CRUDDistrict(CRUDBase[District, DistrictCreate, DistrictUpdate]):
    pass

    
district_actions = CRUDDistrict(District)

