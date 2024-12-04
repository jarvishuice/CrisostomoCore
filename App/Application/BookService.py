from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Entity.BookEntity import BookEntity
from Domain.Repository.IBookRepository import IBookRepository
from Domain.Room.Logs import Logs
from Domain.GlobalValues import GlobalValues
import time

class BookService:
    
    #self.__SEPARATOR = "/" en linux  y en windows "\\"
    def __init__(self,repository:IBookRepository):
        self.repository = repository
        self.__log = Logs(__name__)
        self.__SEPARATOR = GlobalValues().DirectoryChar
    
    async def getBookById(self,id:int) -> BookEntity:
        try:
            return  self.repository.getBookById(id)
        
        except ExeptionDAO as  e :
            raise
    

    async def createBook(self, book:BookEntity,pdf_file) -> BookEntity:
        try:  
            book.code = int(time.time())

            path = f"{GlobalValues().PathBooks}/{book.idCategory}/{book.code}.pdf"
            with open(path, "wb") as buffer:
                content = await pdf_file.read()  # Leer el contenido del archivo PDF
                buffer.write(content) 
            self.__log.info(F"CODE  ADD NEW BOOK -> {book.code}")

            id = self.repository.addBook(book)
            return self.repository.getBookById(id)
        except ExeptionDAO as  e :
            raise
        except Exception as e :
            raise