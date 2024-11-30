from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Entity.EditorialEntity import EditorialEntity
from Domain.Repository.IEditorialRepository import IEditorialRepository


class EditorialService:
    def __init__(self, repository:IEditorialRepository):
        self.repository = repository

    @property
    async def getAllEditorials(self) -> list[EditorialEntity]:
        res = []
        try:
            res = self.repository.getEditorials
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
    

    async def search(self,param:str)-> list[EditorialEntity]:
        res=[]
        try:
            res =  self.repository.searchEditorial(param.upper())
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