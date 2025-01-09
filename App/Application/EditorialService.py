from Domain.Room.Logs import Logs
from Infrastructure.DAO.EditorialTraceFavoriteDAO import EditorialTraceFavoriteDAO
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Entity.EditorialEntity import EditorialEntity
from Domain.Repository.IEditorialRepository import IEditorialRepository


class EditorialService:
    def __init__(self, repository:IEditorialRepository):
        self.repository = repository
        self.traceRepository = EditorialTraceFavoriteDAO()
        self.__log = Logs(__name__)
    
    async def getAllEditorials(self,idUser:int=0) -> list[EditorialEntity]:
        res = []
        try:
            editorials:list[EditorialEntity]= self.repository.getEditorials
            trace = self.traceRepository.getFavoriteByUserId(idUser)
            if idUser == 0:
                res = editorials
                return res
            for i in editorials:
                value = list(filter(lambda e: e.idElement == i.id,trace))
                if len(value) > 0:
                    i.trace = value[0]
                    self.__log.info(f"add trace the editorial #{i.id}")
                res.append(i)
            return res
        except ExeptionDAO as  e :
            raise


    async def getEditorialById(self,id:int)-> EditorialEntity: 
        res:EditorialEntity=None 
        try:
            res = self.repository.getEditorialById(id)
            return res
        except ExeptionDAO as  e :
            raise    
    

    async def search(self,param:str,idUser:int)-> list[EditorialEntity]:
        res=[]
        try:
           
            trace = self.traceRepository.getFavoriteByUserId(idUser)
            editorials =  self.repository.searchEditorial(param.upper())
            for i in editorials:
                value = list(filter(lambda e: e.idElement == i.id,trace))
                print(f"lonfgitud del filtor {len(value)}")
                if len(value) > 0:
                    i.trace = value[0]
                    self.__log.info(f"add trace the editorial #{i.id}")
                res.append(i)
            return res
        except ExeptionDAO as e :
            raise
    

    async def createEditorial(self,editorial:EditorialEntity)->EditorialEntity:
        res:EditorialEntity = None
        try:
            id:int= self.repository.addEditorial(editorial)
            res = await self.getEditorialById(id)
            return res
        except ExeptionDAO as e :
            raise