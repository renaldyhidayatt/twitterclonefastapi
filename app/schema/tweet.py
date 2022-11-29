from typing import Any, Optional
from pydantic import BaseModel
from .user import UserResponseSchema

class TweetSchema(BaseModel):
    status: Optional[str]
    tweetBy_id: Optional[str]
    postedOn: Optional[str]


class TweetCreateSchema(TweetSchema):
    status: str


class TweetResponseSchema(BaseModel):
    status: str | Any
    tweetBy: Optional[UserResponseSchema]
    postedOn: str | Any

    

    class Config:
        orm_mode = True