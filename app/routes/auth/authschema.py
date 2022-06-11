from pydantic import BaseModel


class RegisterUser(BaseModel):
    firstName: str
    lastName: str
    username: str
    email: str
    password: str
    