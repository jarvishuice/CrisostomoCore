from pydantic import BaseModel


class LoginEntity(BaseModel):
    username: str
    password: str