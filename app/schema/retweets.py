from pydantic import BaseModel

class RetweetSchema(BaseModel):
    status: str