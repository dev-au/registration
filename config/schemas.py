from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserModel(BaseModel):
    username: str
    fullname: str
    password: str


class LoginModel(BaseModel):
    username: str
    password: str
