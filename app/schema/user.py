from pydantic import BaseModel
from typing import Any, Optional

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


class UserResponseSchema(BaseModel):
    id: int
    firstName: str
    lastName: str
    username: str
    email: str
    profileImage: str
    profileCover: str
    bio: Optional[str]
    country: Optional[str]
    website: Optional[str]

    class Config:
        orm_mode = True

class UserResponseLoginSchema(UserSchema):
    firstname: str
    lastname: str
    username: str
    email: str
    jwtToken: str


class UserLoginSchema(UserSchema):
    username: str
    password: str
