from app.domains.common.models.document import Document
from app.crud.base import CRUDBase

from app.domains.common.schemas.document import  (
    DocumentCreate, DocumentUpdate,DocumentSchema
)

class CRUDDocument(CRUDBase[Document,DocumentCreate, DocumentUpdate]):
    pass
    


document_actions = CRUDDocument(Document)

