from app.domains.common.models.comment import Comment
from app.crud.base import CRUDBase

from app.domains.common.schemas.comment import  (
    CommentCreate, CommentUpdate,CommentSchema
)

class CRUDComment(CRUDBase[Comment,CommentCreate, CommentUpdate]):
    pass
    


comment_actions = CRUDComment(Comment)

