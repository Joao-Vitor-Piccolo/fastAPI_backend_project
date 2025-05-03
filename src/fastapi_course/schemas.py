from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(User):
    id: int


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
