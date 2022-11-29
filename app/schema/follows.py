from pydantic import BaseModel

class FollowSchema(BaseModel):
    receiver: int