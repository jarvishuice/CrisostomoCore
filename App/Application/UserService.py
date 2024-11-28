from Domain.Entity.loginEntity import LoginEntity
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Cipher import Cipher
from Domain.Entity.UserEntity import UserEntity
from Domain.Repository import IUserRepository


class UserService:
    
    def __init__(self,repository:IUserRepository):
        self.repository = repository
        self.__cipherHelper = Cipher()
    def getAllUsers(self) -> list[UserEntity] :
        return self.repository.getUsers()
    def getUserById(self, id:int) -> UserEntity:
        return self.repository.getUserById(id)
    def createUser(self,user:UserEntity) -> UserEntity:
        # encriptado de la contrasena 
        try:
            
            user.password = self.__cipherHelper.encrypt(user.password)
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
    def login(self,login:LoginEntity)-> UserEntity:
        passCipher = self.__cipherHelper.encrypt(login.password)
        user:UserEntity = None
        try:
            user = self.getUserByParam(param=login.username.upper())
            if(user is not None):
                if(user.password == passCipher):
                    user.status =2
                    self.update(user)
                    return user
                else:
                    raise ExeptionDAO("Contraseña incorrecta")
            else:
                raise ExeptionDAO("Usuario no encontrado")

        except ExeptionDAO as e :
            raise
    def logout(self,idUser:int) -> int :
        user:UserEntity = None
        try:
            user=self.getUserById(idUser)
            user.status =1
            user.token="NO POSEE TOKEN ACTIVO"
            self.update(user)
            return 1
        except ExeptionDAO as e :
            raise