from typing import Any, Optional
from pydantic import BaseModel
from .tweet import TweetResponseSchema

class TrendSchema(BaseModel):
    hashtag: Optional[str]
    user_id: Optional[str]
    tweet_id: Optional[str]


class TrendCreateSchema(TrendSchema):
    hashtag: str


class TrendsResponseSchema(TrendSchema):
    hashtag: str | Any
    user_id: int | Any
    tweet: Optional[TweetResponseSchema]

    class Config:
        orm_mode = True