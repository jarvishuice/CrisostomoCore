from pydantic import BaseModel


class CategoryEntity(BaseModel):
    id:int =0
    name:str =None
    description:str = None
    parentID:int =-1