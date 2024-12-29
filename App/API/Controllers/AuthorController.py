from fastapi import APIRouter, HTTPException, Request
from Domain.Entity.AuthorEntity import AuthorEntity
from Application.AuthorService import AuthorService
from Infrastructure.DAO.AuthorDAO import AuthorDAO
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Logs import Logs

AuthorController = APIRouter(prefix="/Author", tags=["autores"])
logs = Logs(__name__)
dao = AuthorDAO()
service: AuthorService = AuthorService(dao)


@AuthorController.get("/all",response_model=list[AuthorEntity])
async def getAll(request: Request):
    try:
        logs.info(f"call {request.client.host} ->  getAll() ")
        return  await service.getAllAutors
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@AuthorController.get("/byId")
async def getById(request: Request, authorId: int):    
    try:
        logs.info(f"call {request.client.host} ->  getById({authorId}) ")
        return await service.getAuthorById(authorId)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))

@AuthorController.get("/search")
async def search(request:Request,param:str):
    try:
        logs.info(f"call {request.client.host} ->  search({param}) ")
        return  await service.search(param)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))    


@AuthorController.post("/create")
async def create(request: Request,author:AuthorEntity):
    try:
        logs.info(f"call {request.client.host} ->  create({author}) ")
        return  await service.createAuthor(author)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@AuthorController.put("/update")
async def update(request: Request,author:AuthorEntity):
    try:
        logs.info(f"call {request.client.host} ->  update({author.id}) ")
        return await service.update(author)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))