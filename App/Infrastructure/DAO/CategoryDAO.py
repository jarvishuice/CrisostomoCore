
from Infrastructure.Providers.DB.PsqlProvider import PsqlProvider
from Domain.Room.Logs import Logs
from Domain.Repository.ICategoryRepository import ICategoryRepository
from Domain.Entity.CategoryEntity import CategoryEntity
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.GlobalValues import GlobalValues
from psycopg2.extras import RealDictCursor
from psycopg2 import IntegrityError,DatabaseError
 

class CategoryDAO(ICategoryRepository):
    def __init__(self):
        self.__log = Logs(__name__)
        self.__db:PsqlProvider = PsqlProvider.get_instance(100)
    
    @property
    def getBaseCategory(self) -> list[CategoryEntity]:
        res = []
        conn = self.__db.get_connection()
        query = "select * from category c  where c.parent_id = -1"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    res.append(CategoryEntity(id=row["id"],
                                               name=row["name_category"],
                                               description=row["description"],
                                               parentID=row["parent_id"],
                                              ))
                self.__log.info(f"read all BaseCategory ->"+
                                f"[OK] ->[{res.__len__()}] category")
                
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base"+ 
                             f"de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)   

        return res    
     
    def getCategoriesByParentId(self,parentId:int)-> list[CategoryEntity]:
        res = []
        conn = self.__db.get_connection()
        query = "select * from category c  where c.parent_id = %s"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query,(parentId,))
                rows = cur.fetchall()
                for row in rows:
                    res.append(CategoryEntity(id=row["id"],
                                               name=row["name_category"],
                                               description=row["description"],
                                               parentID=row["parent_id"],
                                              ))
                self.__log.info(f"read all category by parentId({parentId}) ->"+
                                f"[OK] ->[{res.__len__()}] category")
                
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base"+ 
                             f"de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)   

        return res

    def getCategoryById(self,categoryId:int)-> CategoryEntity:
        res:CategoryEntity = None
        conn = self.__db.get_connection()
        query = "select * from category c  where id = %s"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query,(categoryId,))
                rows = cur.fetchall()
                for row in rows:
                    res=CategoryEntity(id=row["id"],
                                               name=row["name_category"],
                                               description=row["description"],
                                               parentID=row["parent_id"],
                                              )
                self.__log.info(f"read all category by parentId({categoryId}) ->"+
                                f"[OK] ->[{res.name}]")
                
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base"+ 
                             f"de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)   

        return res