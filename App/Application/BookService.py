from Domain.Values.filterBookValues import FILTER_BOOK
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Entity.BookEntity import BookEntity
from Domain.Repository.IBookRepository import IBookRepository
from Domain.Room.Logs import Logs
from Domain.GlobalValues import GlobalValues
import time
import fitz 

class BookService:
    

    def __init__(self,repository:IBookRepository):
        self.repository = repository
        self.__log = Logs(__name__)
      
    
    async def getBookById(self,id:int) -> BookEntity:
        try:
            return  self.repository.getBookById(id)
        
        except ExeptionDAO as  e :
            raise
    

    async def createBook(self, book:BookEntity,pdf_file) -> BookEntity:
        try:  
            book.code = int(time.time())

            path = f"{GlobalValues().PathBooks}/{book.idCategory}/"
            
            with open(path+f"{book.code}.pdf", "wb") as buffer:
                content = await pdf_file.read()  # Leer el contenido del archivo PDF
                buffer.write(content) 
            self.__log.info(F"CODE  ADD NEW BOOK -> {book.code}")
            #apertura del pdf para obtner la primera pagina 
            # y crear la imagen de previsualizacion 
            pdf = fitz.open(path + f"{book.code}.pdf")           
            page = pdf[0]
            #conversion de primera pagina a una img .png
            pix = page.get_pixmap()
            #guardar la imagen
            pix.save(path + f"{book.code}.png")
            #cierre del pdf 
            pdf.close()
            id = self.repository.addBook(book)
            return self.repository.getBookById(id)
        except ExeptionDAO as  e :
            raise
        except Exception as e :
            raise


    async def getPreviewImageByidBook(self,idBook:int)->str:
        book:BookEntity =  await self.getBookById(idBook)
        path = f"{GlobalValues().PathBooks}/{book.idCategory}/{book.code}.png"
        return path
    
    async def filterBook(self,param:str,value:int) -> list[BookEntity]:
        try:            
                return  self.repository.filterByParam(param,value)
         
        except ExeptionDAO as  e :
            raise