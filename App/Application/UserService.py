from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Cipher import Cipher
from Domain.Entity.UserEntity import UserEntity
from Domain.Repository import IUserRepository


class UserService:
    def __init__(self,repository:IUserRepository):
        self.repository = repository
    def getAllUsers(self) -> list[UserEntity] :
        return self.repository.getUsers()
    def getUserById(self, id:int) -> UserEntity:
        return self.repository.getUserById(id)
    def createUser(self,user:UserEntity) -> UserEntity:
        # encriptado de la contrasena 
        try:
            cipherHelper = Cipher()
            user.password = cipherHelper.encrypt(user.password)
            id = self.repository.addUser(user)
            return self.getUserById(id)
        except ExeptionDAO as e :
            raise 
    def getUserByParam(self,param:str)-> UserEntity:
        try:
            return self.repository.searchUser(param.upper())
        except ExeptionDAO as e :
            raise
    def update(self,user:UserEntity) -> UserEntity:
        try:
           return self.getUserById(self.repository.updateUser(user))
        except ExeptionDAO as e :
            raise