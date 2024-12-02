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