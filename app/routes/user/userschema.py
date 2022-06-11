from pydantic import BaseModel

class UserSchema(BaseModel):
    firstName: str
    lastName: str
    username: str
    email: str
    profileImage: str
    profileCover: str
    bio: str
    country: str
    website: str