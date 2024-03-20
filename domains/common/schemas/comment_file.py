from typing import Any, Dict, List, Optional, Union
from uuid import UUID
import datetime
from pydantic import BaseModel
from datetime import  datetimea
from .comment import CommentSchema

class HTTPError(BaseModel):
    detail: str


# Shared properties
class CommentFileBase(BaseModel):
    
    file_name: Optional[str] = None
    comment_id: Optional[UUID] = None
    
          
# Properties to receive via API on creation
class CommentFileCreate(CommentFileBase):
    
    file_name: str
    comment_id: UUID
    
    
# Properties to receive via API on update
class CommentFileUpdate(CommentFileBase):
    
    pass


class CommentFileInDBBase(CommentFileBase):
    id: Optional[UUID] = None
    file_name: str
    comment_id: str

    class Config:
        orm_mode = True


# Additional properties to return via API
class CommentFileSchema(CommentFileInDBBase):
    
    comment: CommentSchema

       