from fastapi import APIRouter, HTTPException, Request
from Domain.Entity.EditorialEntity import EditorialEntity
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Application.EditorialService import EditorialService
from Infrastructure.DAO.EditorialDAO import EditorialDAO
from Domain.Room.Logs import Logs


EditorialController = APIRouter(prefix="/editorial", tags=["editoriales"])
logs = Logs(__name__)
dao = EditorialDAO()
service: EditorialService = EditorialService(dao)


@EditorialController.get("/all", response_model=list[EditorialEntity])
async def getAll(request: Request):
    try:
        logs.info(f"call {request.client.host} ->  getAll() ")
        return  await service.getAllEditorials(0)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@EditorialController.get("/allWithUser", response_model=list[EditorialEntity])
async def allWithUser(request: Request,idUser:int):
    try:
        logs.info(f"call {request.client.host} ->  allWithUser({idUser}) ")
        return  await service.getAllEditorials(idUser)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@EditorialController.get("/byId")
async def getById(request:Request, id:int):
    try:
        logs.info(f"call {request.client.host} ->  getById({id}) ")
        return await service.getEditorialById(id)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))


@EditorialController.get("/search")
async def search(request:Request, param:str,userId:int):
    try:
        logs.info(f"call {request.client.host} ->  search({param},{userId}) ")
        return  await service.search(param,userId)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@EditorialController.post("/create")
async def createEditorial(request:Request,editorial:EditorialEntity):
    try:
        logs.info(f"call {request.client.host} ->  create({editorial}) ")
        return  await service.createEditorial(editorial)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))