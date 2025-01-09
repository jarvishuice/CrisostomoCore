"""
Módulo: IFavoriteTraceRepository

Este módulo define la interfaz para el repositorio de trazas de favoritos. 
Utiliza el patrón de diseño de repositorio y se basa en la clase abstracta 
de Python (ABC) para definir métodos que deben ser implementados por 
cualquier clase que herede de esta interfaz.

Clases:
    FavoriteTraceRepository (ABC): 
        Clase abstracta que define los métodos para interactuar con 
        las trazas de favoritos.

Métodos abstractos:
    getFavoriteByUserId(userId: int) -> list[FavoriteTraceEntity]:
        Recupera una lista de trazas de favoritos asociadas a un 
        identificador de usuario específico.

    checkFavorite(userId: int, elementId: int) -> bool:
        Verifica si un elemento específico está marcado como favorito 
        por un usuario dado.

    createTraceFavorite(trace: FavoriteTraceEntity) -> FavoriteTraceEntity:
        Crea una nueva traza de favorito.

    deleteTraceFavorite(trace: FavoriteTraceEntity) -> bool:
        Elimina una traza de favorito existente.
"""

from abc import ABC, abstractmethod
from Domain.Entity.FavoriteTraceEntity import FavoriteTraceEntity


class IFavoriteTraceRepository(ABC):
    """
    Clase abstracta que define los métodos para interactuar con 
    las trazas de favoritos.
    """

    @abstractmethod
    def getFavoriteByUserId(userId: int) -> list[FavoriteTraceEntity]:
        """
        Recupera una lista de trazas de favoritos asociadas a un 
        identificador de usuario específico.

        Parámetros:
            userId (int): El identificador del usuario.

        Retorna:
            list[FavoriteTraceEntity]: Lista de trazas de favoritos 
            del usuario.
        """
        ...


    @abstractmethod
    def checkFavorite(userId: int, elementId: int) -> bool:
        """
        Verifica si un elemento específico está marcado como favorito 
        por un usuario dado.

        Parámetros:
            userId (int): El identificador del usuario.
            elementId (int): El identificador del elemento a verificar.

        Retorna:
            bool: True si el elemento es favorito del usuario, 
            False en caso contrario.
        """
        ...

    
    @abstractmethod
    def createTraceFavorite(trace: FavoriteTraceEntity) -> FavoriteTraceEntity:
        """
        Crea una nueva traza de favorito.

        Parámetros:
            trace (FavoriteTraceEntity): La traza de favorito a crear.

        Retorna:
            FavoriteTraceEntity: La traza de favorito creada.
        """
        ...

    
    
    @abstractmethod
    def deleteTraceFavorite(trace: FavoriteTraceEntity) -> bool:
        """
        Elimina una traza de favorito existente.

        Parámetros:
            trace (FavoriteTraceEntity): La traza de favorito a eliminar.

        Retorna:
            bool: True si la eliminación fue exitosa, 
            False en caso contrario.
        """
        ...
