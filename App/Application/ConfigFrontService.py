from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Entity.AppConfigRouteNavEntity import AppConbfigRouteNavEntity
from Infrastructure.DAO.AppConfigRouteNavDAO import AppConfigRouteNavDAO
from Domain.Repository.IAppConfigRouteNavReopository import IAppConfigRouteNavReopository


class ConfigFrontService():


    def __init__(self):
        self.repository: IAppConfigRouteNavReopository = AppConfigRouteNavDAO()

    
    @property
    async def allRoutes(self) -> list[AppConbfigRouteNavEntity]:
        res: list[AppConbfigRouteNavEntity] = []
        try:
            res = self.repository.getAll
            return res
        except ExeptionDAO as e:
            raise


    async def getRoutesByTypeUser(self, typeUser: int):
        res: list[AppConbfigRouteNavEntity] = []
        try:
            res = self.repository.getByTypeUser(typeUser)
            return res
        except ExeptionDAO as e:
            raise
