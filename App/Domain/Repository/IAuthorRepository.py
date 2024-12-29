from abc import ABC, abstractmethod
from Domain.Entity.AuthorEntity import AuthorEntity

class IAuthorRepository(ABC):
    """
    Interface para gestionar los autores.
    
    """
    
    @abstractmethod
    def getAuthors(self) -> list[AuthorEntity] :
        ...
    
    
    @abstractmethod
    def getAuthorById(self , id:int) -> AuthorEntity:
        ...
    
    
    @abstractmethod
    def searchAuthor(self,param:str)->list[AuthorEntity] :
        ...  


    @abstractmethod
    def addAuthor(self,author:AuthorEntity)->int:
        ...
    
    @abstractmethod
    def update(self,author:AuthorEntity)->int:
        ...