from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Entity.CategoryEntity import CategoryEntity
from Domain.Repository.ICategoryRepository import ICategoryRepository

class CategoryService:
    def __init__(self,repository:ICategoryRepository):
        self.repository = repository

    @property
    async def getBaseCategory(self) -> list[CategoryEntity]:
        try:
            return  self.repository.getBaseCategory
        except ExeptionDAO as  e :
            raise
