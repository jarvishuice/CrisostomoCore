from Domain.Entity.AuthorEntity import AuthorEntity
from Infrastructure.Providers.DB.PsqlProvider import PsqlProvider
from psycopg2.extras import RealDictCursor
from psycopg2 import IntegrityError,DatabaseError
from Domain.GlobalValues import GlobalValues
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Logs import Logs
from Domain.Repository.IAuthorRepository import IAuthorRepository
class AuthorDAO(IAuthorRepository):
    def __init__(self ):
        self.__log = Logs(__name__)
        self.__db:PsqlProvider = PsqlProvider.get_instance(100)
    
    @property
    def getAuthors(self) -> list[AuthorEntity] :
        res = []
        conn = self.__db.get_connection()
        query = "select * from author"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    res.append(AuthorEntity(id=row["id"],
                                            name=row["name"],
                                            description = row["description"],
                                           ))
                self.__log.info(f"read all Authors ->[OK] ->[{res.__len__()}] authors")
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)   

        return res  

  
    def getAuthorById(self , id:int) -> AuthorEntity:
        res:AuthorEntity = None
        conn = self.__db.get_connection()
        query= "select * from author where id = %s"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query,(id,))
                rows = cur.fetchall()
                if len(rows) > 0:

                    for row in rows:
                        res=AuthorEntity(id=row["id"],
                                        name=row["name"],
                                        description = row["description"],
                                    )
                    self.__log.info(f"read  Author #{id} ->[OK] ->[{res.name}] ")
                else:
                    self.__log.info(f"read  Author #{id} ->[Not Found]")    
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)   

        return res  


    def searchAuthor(self,param:str)->list[AuthorEntity] :
        res = []
        conn = self.__db.get_connection()
        query= "select * from author where name like  %s ;"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query,(f"%{param}%",))
                rows = cur.fetchall()
                if len(rows) > 0:

                    for row in rows:
                        res.append(AuthorEntity(id=row["id"],
                                                name = row["name"],
                                                description = row["description"]
                                                ))
                    self.__log.info(f"search  Author #{param} ->[OK] ->[{res.__len__()}] Authors ")
                else:
                    self.__log.info(f"search  Author #{param} ->[Not Found]")    
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)
        return res
    

    def addAuthor(self,author:AuthorEntity)->int:
    
        new_id = None
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = """
                    INSERT INTO public.author ( name, description) 
                    VALUES (%s, %s)
                    RETURNING id
                 """
                cur.execute(query, (
                author.name.upper(),
                author.description,
                ))
                
           
                new_id = cur.fetchone()['id']
                conn.commit() 
                self.__log.info(f"add author -> [OK] -> #[{new_id}]")
            return new_id
            
        except IntegrityError as e :
            self.__log.error(f"Error de integridad en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbIntErrors)
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)
   
   
    def update(self,author:AuthorEntity)->int:
    
        new_id = None
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = """
                    UPDATE public.author SET "name"= %s, description=%s 
                    WHERE id=%s;
                 """
                cur.execute(query, (
                author.name.upper(),
                author.description,
                author.id,
                ))
                
                conn.commit()
                new_id = author.id 
                self.__log.info(f"update author -> [OK] -> #[{new_id}]")
            return new_id
            
        except IntegrityError as e :
            self.__log.error(f"Error de integridad en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbIntErrors)
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)
        