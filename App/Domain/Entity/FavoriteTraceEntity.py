from pydantic import BaseModel


class FavoriteTraceEntity(BaseModel):

    id: int = 0
    idUser: int = 0
    idElement: int = 0
    dateOperation: str= ""
