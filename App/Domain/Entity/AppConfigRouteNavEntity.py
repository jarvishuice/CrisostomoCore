from pydantic import BaseModel


class AppConbfigRouteNavEntity(BaseModel):
    id: int = 0
    cod: str = None
    nameRoute: str = None
    path: str = None
    typeUser: int = 0
    pageName: str = None
    icon: str = None
    status: int = 0
