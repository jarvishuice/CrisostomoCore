from abc import ABC, abstractmethod
from Domain.Entity.EditorialEntity import EditorialEntity

class IEditorialRepository(ABC):
    """
    Interface para gestionar las editoriales.
    """
    @abstractmethod
    def getEditorials(self) -> list[EditorialEntity] :
        ...
    @abstractmethod
    def getEditorialById(self , id:int) -> EditorialEntity:
        ...
    @abstractmethod
    def searchEditorial(self,param:str)->list[EditorialEntity] :
        ...   

    @abstractmethod
    def addEditorial(self, editorial: EditorialEntity) -> int:
        ...