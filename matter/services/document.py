from app.domains.matter.models.document import  Document
from app.crud.base import CRUDBase

from app.domains.matter.schemas.document import (
     DocumentCreate, DocumentUpdate
)

class CRUDDocument(CRUDBase[Document, DocumentCreate, DocumentUpdate]):
    pass

    
document_actions = CRUDDocument(Document)

