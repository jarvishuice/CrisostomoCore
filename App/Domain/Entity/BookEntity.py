from pydantic import BaseModel


class BookEntity(BaseModel):
   

    id: int = 0
    title: str = None
    idEditorial: int
    idAutor: int = 0
    idCategory: int = 0
    idBaseCategory:int = 0
    idUserUpload:int = 0
    dateCreated:str = None 
    code:int = None
    
