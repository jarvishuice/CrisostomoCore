from Domain.Repository import IAuthorRepository
from Domain.Entity.AuthorEntity import AuthorEntity
from Domain.Entity.loginEntity import LoginEntity
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Cipher import Cipher
from Domain.Entity.UserEntity import UserEntity
from Domain.Repository import IUserRepository

class AuthorService:
    def __init__(self,repository:IAuthorRepository):
        self.repository = repository
    
    @property
    async  def getAllAutors(self) -> list[AuthorEntity]:
        res = []
        try:
            res = self.repository.getAuthors
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


    async def search(self,param:str)-> list[AuthorEntity]:
        res=[]
        try:
            res =  self.repository.searchAuthor(param.upper())
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