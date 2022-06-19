from pydantic import BaseModel

class TrendSchema(BaseModel):
    hashtag: str