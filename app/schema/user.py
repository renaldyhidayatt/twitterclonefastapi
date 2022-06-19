from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    profileImage: Optional[str]
    profileCover: Optional[str]
    bio: Optional[str]
    country: Optional[str]
    website: Optional[str]


class UserCreateSchema(UserSchema):
    firstName: str
    lastName: str
    username: str
    email: str
    password: str

class UserUpdateSchema(UserSchema):
    firstName: Optional[str]
    lastName: Optional[str]
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    profileImage: Optional[str]
    profileCover: Optional[str]
    bio: Optional[str]
    country: Optional[str]
    website: Optional[str]


class UserResponseSchema(UserSchema):
    id: int
    firstName: str
    lastName: str
    username: str
    email: str
    profileImage: str
    profileCover: str
    bio: str
    country: str
    website: str

    class Config:
        orm_mode = True

class UserResponseLoginSchema(UserSchema):
    firstname: Optional[str]
    lastname: Optional[str]
    username: Optional[str]
    email: Optional[str]
    jwtToken: str


class UserLoginSchema(UserSchema):
    username: str
    password: str
