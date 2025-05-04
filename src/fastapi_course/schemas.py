from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class MessagePassword(BaseModel):
    password: str


class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(User):
    id: int


class UserPassword(BaseModel):
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]
