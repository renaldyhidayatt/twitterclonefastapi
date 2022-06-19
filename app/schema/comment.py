from typing import Any, Optional
from pydantic import BaseModel

from app.schema.user import UserResponseSchema

class CommentSchema(BaseModel):
    comment: str


class CommentCreateSchema(CommentSchema):
    comment: str


class CommentResponseSchema(CommentSchema):
    commentOn_id: int
    comment: str
    commentBy: Optional[UserResponseSchema]
    commentAt: str | Any

    class Config:
        orm_mode = True