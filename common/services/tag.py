from app.domains.common.models.tag import Tag
from app.crud.base import CRUDBase

from app.domains.common.schemas.tag import  (
    TagCreate, TagUpdate,TagSchema
)

class CRUDTag(CRUDBase[Tag,TagCreate, TagUpdate]):
    pass
    

tag_actions = CRUDTag(Tag)

