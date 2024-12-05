from pydantic import BaseModel


class AuthorEntity(BaseModel):
    id: int = 0
    name:str = None
    description:str = None
