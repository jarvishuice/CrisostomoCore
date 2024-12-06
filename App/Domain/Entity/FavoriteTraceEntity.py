from pydantic import BaseModel


class FavoriteTraceEntity(BaseModel):

    id: int = 0
    book: int = 0
    user: int = 0
    dateOperation: int = 0
