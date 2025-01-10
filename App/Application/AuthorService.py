from Domain.Entity.FavoriteTraceEntity import FavoriteTraceEntity
from Domain.Room.Logs import Logs
from Infrastructure.DAO.AuthorTraceFavoriteDAO import AuthorTraceFavoriteDAO
from Domain.Repository import IAuthorRepository
from Domain.Entity.AuthorEntity import AuthorEntity
from Domain.Exeptions.ExecptionDAO import ExeptionDAO



class AuthorService:
    def __init__(self,repository:IAuthorRepository):
        self.repository = repository
        self.traceRepository = AuthorTraceFavoriteDAO()
        self.__log = Logs(__name__)


    async  def getAllAutors(self,idUser:int=0 ) -> list[AuthorEntity]:
        res = []
        try:
            authors:list[AuthorEntity] = self.repository.getAuthors
            trace= self.traceRepository.getFavoriteByUserId(idUser)
            if idUser==0:
                res = authors
                return res
            for i in authors:
                value = list(filter(lambda e: e.idElement == i.id,trace ))
                if len(value) > 0:
                    i.trace = value[0]
                    self.__log.info(f"add trace the author #{i.id}")    
                res.append(i) 
            return res           
        except ExeptionDAO as e :
            raise   

    async def getAuthorById(self, id) -> AuthorEntity:
        res:AuthorEntity= None
        try:
            res = self.repository.getAuthorById(id)
            return res
        except ExeptionDAO as e :
            raise  


    async def createAuthor(self,author:AuthorEntity)->AuthorEntity:
        res:AuthorEntity = None
        try:
            id:int= self.repository.addAuthor(author)
            res = await self.getAuthorById(id)
            return res
        except ExeptionDAO as e :
            raise 


    async def search(self,param:str,idUser:int=0)-> list[AuthorEntity]:
        res=[]
        try:
            authors =  self.repository.searchAuthor(param.upper())
            trace= self.traceRepository.getFavoriteByUserId(idUser)

            if idUser==0:
                res = authors
                return res
            for i in authors:
                value = list(filter(lambda e: e.idElement == i.id,trace ))
                if len(value) > 0:
                    i.trace = value[0]
                    self.__log.info(f"add trace the author #{i.id}")    
                res.append(i) 
            return res           
        except ExeptionDAO as e :
            raise 


    async def update(self,author:AuthorEntity)->AuthorEntity:
        res:AuthorEntity= None
        try :
            r = self.repository.update(author)
            res = await self.getAuthorById(r)
            return res
        except ExeptionDAO as e:
            raise

    
    async def tapFavorite(self,idUser:int,element:int)->bool:
        res = False
        trace:FavoriteTraceEntity = FavoriteTraceEntity()
        traceRes:FavoriteTraceEntity = FavoriteTraceEntity()
        try:
            check = self.traceRepository.checkFavorite(idUser,element)
            self.__log.info(f"check favorite author #{element}"+ 
                               f"by user #{idUser} ->[{check}]")
            if check:
                trace  = self.traceRepository.traceByItemAndUser(idUser,element)
                self.traceRepository.deleteTraceFavorite(trace)
                res = True
                return res
            else:
                trace.id = -1
                trace.idUser = idUser
                trace.idElement = element
                trace.dateOperation = "vacio se llena solo"
                traceRes = self.traceRepository.createTraceFavorite(trace)
                if traceRes.id > 0:
                    res= True
            return res
        
        except ExeptionDAO as e :
            raise
    

    async def getAuthorFavoriteByUser(self,idUser:int)-> list[AuthorEntity] :
        res=[]
        try:
           
            trace = self.traceRepository.getFavoriteByUserId(idUser)
            editorials =  self.repository.getAuthorFavorite(idUser)
            for i in editorials:
                value = list(filter(lambda e: e.idElement == i.id,trace))
              
                if len(value) > 0:
                    i.trace = value[0]
                    self.__log.info(f"add trace the editorial #{i.id}")
                res.append(i)
            return res
        except ExeptionDAO as e :
            raise


    