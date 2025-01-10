from typing import Optional
from pydantic import BaseModel
from Domain.Entity.FavoriteTraceEntity import FavoriteTraceEntity


class AuthorEntity(BaseModel):
    id: int = 0
    name: str = None
    description: str = None
    trace: Optional[FavoriteTraceEntity] = None
