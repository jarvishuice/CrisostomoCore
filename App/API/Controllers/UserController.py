from fastapi import APIRouter, HTTPException, Request
from Domain.Entity.loginEntity import LoginEntity
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Entity.UserEntity import UserEntity
from Application.UserService import UserService
from Domain.Room.Logs import Logs
from Infrastructure.DAO.UserDAO import UserDAO

UserController = APIRouter(prefix="/user", tags=["usuarios"])
logs = Logs(__name__)
dao = UserDAO()
service: UserService = UserService(dao)


@UserController.get("/all")
async def getAll(request: Request):
    try:
        logs.info(f"call {request.client.host} ->  getAll() ")
        return service.getAllUsers()
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))


@UserController.get("/byId")
async def getById(request: Request, userId: int):
    try:
        logs.info(f"call {request.client.host} ->  getById({userId}) ")
        return service.getUserById(userId)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))


@UserController.get("/search")
async def searchUser(request: Request, param):
    logs.info(f"call {request.client.host} -> searchUser({param})")
    try:
        return service.getUserByParam(param)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))


@UserController.post("/create")
def createUser(request: Request, user: UserEntity):
    logs.info(f"call {request.client.host} ->  createUser({user}) ")
    try:
        return service.createUser(user)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@UserController.post("/login")
async def login(request:Request,login:LoginEntity):
    logs.info(f"call {request.client.host} ->  login({login.username.upper()},**********) ")
    try:
        return service.login(login)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))
@UserController.put("/update")
def updateUser(request: Request, user: UserEntity):
    logs.info(f"call {request.client.host} ->  updateUser({user}) ")
    try:
        return service.update(user)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))
@UserController.put("/logout")
def logout(request: Request, idUser:int):
    logs.info(f"call {request.client.host} ->  logout({idUser}) ")
    try:
        return service.logout(idUser)
    except ExeptionDAO as e:
        raise HTTPException(status_code=400, detail=str(e))

