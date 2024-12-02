from fastapi import APIRouter, HTTPException, Request
from Application.CategoryService import CategoryService
from Infrastructure.DAO.CategoryDAO import CategoryDAO
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Logs import Logs

CategoryController = APIRouter(prefix="/category", tags=["categorias"])
logs = Logs(__name__)
dao = CategoryDAO()
service: CategoryService = CategoryService(dao)

@CategoryController.get("/base")
async def getBase(request: Request):
    try:
        logs.info(f"call {request.client.host} ->  getBase() ")
        return await service.getBaseCategory
    except ExeptionDAO as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener las categorias Base: {e}")
    

@CategoryController.get("/byParentId")
async def  getCategorieByParentId(request: Request,parentId:int):
    try:
        logs.info(f"call {request.client.host} ->  getCategorieByParentId({parentId}) ")
        return await service.getCategoryByParentId(parentId)
    except ExeptionDAO as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener las categorias por padre: {e}")
    
    
@CategoryController.get("/byId")
async def getCategoryById(request: Request,categoryId:int):
    try:
        logs.info(f"call {request.client.host} ->  getCategoryById({categoryId}) ")
        return await service.getCategoryById(categoryId)
    except ExeptionDAO as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener la categoria por id: {e}")
