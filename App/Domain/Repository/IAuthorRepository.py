from abc import ABC, abstractmethod
from Domain.Entity.AuthorEntity import AuthorEntity

class IAuthorRepository(ABC):
    """
    Interfaz para gestionar los autores en el sistema.
    Define los métodos necesarios para realizar operaciones sobre los autores.
    """

    @abstractmethod
    def getAuthors(self) -> list[AuthorEntity]:
        """
        Devuelve una lista de todos los autores disponibles en el sistema.
        
        Returns:
            list[AuthorEntity]: Lista de instancias de AuthorEntity.
        """
        ...

    @abstractmethod
    def getAuthorById(self, id: int) -> AuthorEntity:
        """
        Busca y devuelve un autor específico basado en su identificador único.
        
        Args:
            id (int): El identificador del autor que se desea obtener.
        
        Returns:
            AuthorEntity: La instancia del autor correspondiente al id proporcionado.
        """
        ...

    @abstractmethod
    def searchAuthor(self, param: str) -> list[AuthorEntity]:
        """
        Busca autores que coincidan con el parámetro de búsqueda proporcionado.
        
        Args:
            param (str): Cadena de texto que se utilizará para buscar autores.
        
        Returns:
            list[AuthorEntity]: Lista de instancias de AuthorEntity que coinciden con la búsqueda.
        """
        ...

    @abstractmethod
    def addAuthor(self, author: AuthorEntity) -> int:
        """
        Agrega un nuevo autor al sistema.
        
        Args:
            author (AuthorEntity): Una instancia de AuthorEntity que representa al autor a agregar.
        
        Returns:
            int: El identificador del autor agregado.
        """
        ...

    @abstractmethod
    def update(self, author: AuthorEntity) -> int:
        """
        Actualiza la información de un autor existente en el sistema.
        
        Args:
            author (AuthorEntity): Una instancia de AuthorEntity que contiene la información actualizada del autor.
        
        Returns:
            int: El identificador del autor actualizado.
        """
        ...

    @abstractmethod
    def getAuthorFavorite(self, idUser: int) -> list[AuthorEntity]:
        """
        Devuelve una lista de autores favoritos de un usuario específico.
        
        Args:
            idUser (int): El identificador del usuario cuyas preferencias de autor se desean obtener.
        
        Returns:
            list[AuthorEntity]: Lista de instancias de AuthorEntity que son favoritos del usuario.
        """
        ...