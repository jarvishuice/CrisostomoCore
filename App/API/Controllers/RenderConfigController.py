from fastapi import APIRouter, HTTPException, Request
from Application.ConfigFrontService import ConfigFrontService
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Logs import Logs

RenderConfigController = APIRouter(prefix="/config", tags=[" configuracion de la aplicvacion fornt end "])
logs = Logs(__name__)

service: ConfigFrontService = ConfigFrontService()

@RenderConfigController.get("/ByTypeUSer")
async def ConfigNaveRenderByTypeUser(request: Request,typeuser:int):
    try:
        logs.info(f"call {request.client.host} ->  ConfigNaveRenderByTypeUser({typeuser}) ")
        return await service.getRoutesByTypeUser(typeuser)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener las rutas : {e}")
    
"""
@RenderConfigController.get("/byParentId")
async def  getCategorieByParentId(request: Request,parentId:int):
    try:
        logs.info(f"call {request.client.host} ->  getCategorieByParentId({parentId}) ")
        return await service.getCategoryByParentId(parentId)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener las categorias por padre: {e}")
    
    
@RenderConfigController.get("/byId")
async def getCategoryById(request: Request,categoryId:int):
    try:
        logs.info(f"call {request.client.host} ->  getCategoryById({categoryId}) ")
        return await service.getCategoryById(categoryId)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener la categoria por id: {e}")
"""