from app.domains.common.models.attachment import Attachment
from app.crud.base import CRUDBase

from app.domains.common.schemas.attachement import  (
    AttachmentCreate, AttachmentUpdate,AttachmentSchema
)

class CRUDAttachment(CRUDBase[Attachment,AttachmentCreate, AttachmentUpdate]):
    pass
    


attachment_actions = CRUDAttachment(Attachment)

