from pydantic import BaseModel


class DownloadTraceEntity(BaseModel):

    id: int = 0
    book: int = 0
    User: str = None
    dateOperation: str = None
