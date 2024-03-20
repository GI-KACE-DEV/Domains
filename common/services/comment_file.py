from app.domains.common.models.comment_file import CommentFile
from app.crud.base import CRUDBase

from app.domains.common.schemas.comment_file import  (
    CommentFileCreate, CommentFileUpdate,CommentFileSchema
)

class CRUDCommentFile(CRUDBase[CommentFile,CommentFileCreate, CommentFileUpdate]):
    pass
    


comment__file_actions = CRUDCommentFile(CommentFile)

