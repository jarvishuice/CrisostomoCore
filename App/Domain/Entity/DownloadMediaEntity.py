from pydantic import BaseModel


class DownloadMediaEntity(BaseModel):
    path: str
    name:str
    ext:str