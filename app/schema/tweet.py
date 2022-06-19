from pydantic import BaseModel

class TweetSchema(BaseModel):
    status: str