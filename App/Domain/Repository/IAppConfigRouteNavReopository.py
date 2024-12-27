from abc import ABC, abstractmethod
from Domain.Entity.AppConfigRouteNavEntity import AppConbfigRouteNavEntity


class IAppConfigRouteNavReopository(ABC):

    @abstractmethod
    def getByTypeUser(typeUser: int) -> list[AppConbfigRouteNavEntity]: ...


    @abstractmethod
    def getAll() -> list[AppConbfigRouteNavEntity]: ...
