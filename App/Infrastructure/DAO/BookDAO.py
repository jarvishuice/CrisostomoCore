from Domain.Entity.BookEntity import BookEntity
from Domain.Repository.IBookRepository import IBookRepository
from Infrastructure.Providers.DB.PsqlProvider import PsqlProvider
from Domain.Room.Logs import Logs
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.GlobalValues import GlobalValues
from psycopg2.extras import RealDictCursor
from psycopg2 import IntegrityError,DatabaseError

class BookDAO(IBookRepository):

    def __init__(self):
        self.__log = Logs(__name__)
        self.__db:PsqlProvider = PsqlProvider.get_instance(100)
    
    
    @property
    def getAll(self) -> list[BookEntity]:
        res = []
        conn = self.__db.get_connection()
        query = "select * from books"
        try:
            with conn.cursor(cursor_factory = RealDictCursor) as cur:
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    res.append(BookEntity( id = row["id"],
                                           title = row["title"],
                                           idEditorial = row["editorial"],
                                           idAutor = row["autor"],
                                           idCategory = row["category"],
                                           idBaseCategory = row["base_category"],
                                           idUserUpload = row["user_upload"],
                                           dateCreated = str(row["date_create"]),                                         
                                           code = row["code"]
          
                                              ))
                self.__log.info(f"read all Books ->"+
                                f"[OK] ->[{res.__len__()}] books")
                
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
    
    
    def getBookById(self,id: int) -> BookEntity:
        res:BookEntity = None  
        conn = self.__db.get_connection()
        query = "select * from books where id = %s"
        try:
            with conn.cursor(cursor_factory = RealDictCursor) as cur:
                cur.execute(query,(id,))
                rows = cur.fetchall()
                for row in rows:
                    res = BookEntity( id = row["id"],
                                      title = row["title"],
                                      idEditorial = row["editorial"],
                                      idAutor = row["autor"],
                                      idCategory = row["category"],
                                      idBaseCategory = row["base_category"],
                                      idUserUpload = row["user_upload"],
                                      dateCreated = str(row["date_create"]),
                                      code = row["code"]
          
                                              )
                self.__log.info(f"get book byId #{id} ->"+
                                f"[OK] ->[{res.title}]")
                
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
    
    
    def searchBook(self,param:str) ->list[BookEntity]:
        res:BookEntity = None  
        conn = self.__db.get_connection()
        query = "select * from books where title like %s"
        try:
            with conn.cursor(cursor_factory = RealDictCursor) as cur:
                cur.execute(query,(f"%{param.upper()}%",))
                rows = cur.fetchall()
                for row in rows:
                    res = BookEntity( id = row["id"],
                                      title = row["title"],
                                      idEditorial = row["editorial"],
                                      idAutor = row["autor"],
                                      idCategory = row["category"],
                                      idBaseCategory = row["base_category"],
                                      idUserUpload = row["user_upload"],
                                      dateCreated = str(row["date_create"]),
                                      code = row["code"],
          
                                              )
                self.__log.info(f"search  Book ->{param} ->"+
                                f"[OK] ->[{res.__len__()}] books")
                
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
    


    def addBook(self,book:BookEntity) -> int:
        new_id = None
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = """
                    INSERT INTO public.books (title, editorial, 
                    autor, category, base_category, user_upload, 
                    code) VALUES(%s,%s,%s,%s,%s,%s,%s)
                    RETURNING id
                    """
                cur.execute(query, (book.title.upper(),
                                    book.idEditorial,
                                    book.idAutor,
                                    book.idCategory,
                                    book.idBaseCategory,
                                    book.idUserUpload,
                                    book.code
                                    ))
        
                new_id = cur.fetchone()['id']
                conn.commit() 
                self.__log.info(f"add book -> [OK] ->"+
                                f"#[{new_id}]")
            return new_id
            
        except IntegrityError as e :
            self.__log.error(f"""Error de integridad en la base de
                               datos ->{e} """)
            raise ExeptionDAO(GlobalValues().getMsgDbIntErrors)
        except DatabaseError as e :
            self.__log.error(f"""Error de operacion en la base de
                              datos en la base de datos ->{e} """)
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e :
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)
    