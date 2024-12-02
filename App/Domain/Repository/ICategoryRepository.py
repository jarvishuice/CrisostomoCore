from abc import ABC,abstractmethod
from Domain.Entity.CategoryEntity import CategoryEntity

class ICategoryRepository(ABC):
    """
    Interface para gestionar las categorías.
    """
    @abstractmethod 
    def getBaseCategory()-> list[CategoryEntity]:
        ...

    @abstractmethod
    def getCategoriesByParentId(parentId:int)-> list[CategoryEntity]:
        ...
    @abstractmethod 
    def getCategoryById(categoryId:int)-> CategoryEntity:
        ...