from abc import ABC, abstractmethod
from Domain.Entity.UserEntity import UserEntity
class IUserRepository(ABC):
    """
    Interface para gestionar los usuarios.
    """
    @abstractmethod
    def getUsers(self) -> list[UserEntity] :
        ...
    @abstractmethod
    def getUserById(self , id:int) -> UserEntity:
        ...
    @abstractmethod
    def addUser(self, user: UserEntity) -> int:
        ...
    @abstractmethod
    def searchUser(param:str)->UserEntity:
        ...
    @abstractmethod
    def updateUser(self, user: UserEntity) -> int:
        ...