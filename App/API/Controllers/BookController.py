from fastapi import APIRouter, File, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse
from Domain.Entity.BookEntity import BookEntity
from Application.BookService import BookService
from Infrastructure.DAO.BookDAO import BookDAO
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Logs import Logs
import os

BookController = APIRouter(prefix="/books", tags=["libros"])
logs = Logs(__name__)
dao = BookDAO()
service: BookService = BookService(dao)

@BookController.get("/byID")
async def getBookById(request:Request,id:int):
    try:
        logs.info(f"call {request.client.host} ->  getBookById({id}) ")
        return await service.getBookById(id)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener el libro [{e}]")
    

@BookController.post("/createBook")
async def createBook(editorial:int,autor:int,title:str,category:int,category_base:int,userUpload:int,request:Request,pdf_file: UploadFile = File(...), ): #):  # Recibiendo el archivo PDF

    res:BookEntity = None
    logs.info(f"call {request.client.host} ->  createBook({title}) ")
    book:BookEntity = BookEntity(id = 0,
                                 title = title,
                                 idEditorial= editorial,
                                 idAutor=autor,
                                 idCategory = category,
                                 idBaseCategory = category_base,
                                 idUserUpload = userUpload,
                                 )
    
    if pdf_file.content_type != 'application/pdf':
         raise HTTPException(status_code=400, detail=f"El archivo debe ser un PDF.") 
    try:
        res= await service.createBook(book,pdf_file)
        return res
    except ExeptionDAO as e:
           raise HTTPException(status_code=400, detail=f"Error al subir  el libro [{e}]")
    except Exception as e:
          raise HTTPException(status_code=400, detail=f"Error al subir  el libro [{e}]")
    

@BookController.get("/getImagePreview")
async def getImagePreview(request:Request,idBook:int):
    logs.info(f"call {request.client.host} ->  getImagePreview({id}) ")
    imagePath =  await service.getPreviewImageByidBook(idBook)
    if not os.path.exists(imagePath):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(imagePath) 
