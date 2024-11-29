from pydantic import BaseModel


class EditorialEntity(BaseModel):
    id: int = 0
    name:str = None