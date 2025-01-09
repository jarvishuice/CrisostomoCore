from typing import Optional
from pydantic import BaseModel
from Domain.Entity.FavoriteTraceEntity import FavoriteTraceEntity


class EditorialEntity(BaseModel):
    id: int = 0
    name:str = None
    trace:Optional[FavoriteTraceEntity] = None