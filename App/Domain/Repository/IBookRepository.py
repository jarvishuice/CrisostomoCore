from abc import ABC,abstractmethod
from Domain.Entity.BookEntity import BookEntity
class IBookRepository(ABC):


    @abstractmethod
    def getAll() -> list[BookEntity]:
        ...
    @abstractmethod 
    def getBookById(id: int) -> BookEntity:
        ...
    @abstractmethod
    def searchBook(param:str) ->list[BookEntity]:
        ...
    @abstractmethod
    def addBook(book:BookEntity) -> int:
        ...
