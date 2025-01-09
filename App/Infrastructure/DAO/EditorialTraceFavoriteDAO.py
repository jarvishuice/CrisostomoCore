from Domain.Room.Logs import Logs
from Infrastructure.Providers.DB.PsqlProvider import PsqlProvider
from Domain.Entity.FavoriteTraceEntity import FavoriteTraceEntity
from Domain.Repository.IFavoriteTraceRepository import IFavoriteTraceRepository
from Domain.GlobalValues import GlobalValues
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from psycopg2.extras import RealDictCursor
from psycopg2 import IntegrityError, DatabaseError


class EditorialTraceFavoriteDAO(IFavoriteTraceRepository):

    def __init__(self):
        self.__log = Logs(__name__)
        self.__db: PsqlProvider = PsqlProvider.get_instance(100)


    def getFavoriteByUserId(self, userId: int) -> list[FavoriteTraceEntity]:
        res = []
        conn = self.__db.get_connection()
        query = """
                   SELECT id, id_user, id_editorial, date_trace
                   FROM public.editorial_favorite_trace WHERE 
                   id_user =%s order by id_editorial asc;
                """

        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, (userId,))
                rows = cur.fetchall()

                for row in rows:
                    res.append(FavoriteTraceEntity(id=row["id"],
                                                   idUser=row["id_user"],
                                                   idElement=row["id_editorial"],
                                                   dateOperation=str(row["date_trace"])
                                                   ))
                self.__log.info(f"read editorial favorites the user #{userId} ->" +
                                f"[OK] ->[{len(res)}] editorials")

        except DatabaseError as e:
            self.__log.error(f"Error de operacion en la base" +
                             f"de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)

        return res

    
    def checkFavorite(self, userId: int, elementId: int) -> bool:
        res = False
        conn = self.__db.get_connection()
        query = """
                  select count(id) as cantidad from 
                  public.editorial_favorite_trace WHERE 
                  id_user =%s and id_editorial = %s
                """

        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, (userId, elementId))
                rows = cur.fetchall()

                for row in rows:
                    res = int(row["cantidad"]) > 0
                self.__log.info(f"ckeck  favorites  the editorial #{elementId}" +
                                f"the user #{userId} -> [OK] ->[{res}]")

        except DatabaseError as e:
            self.__log.error(f"Error de operacion en la base" +
                             f"de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)

        return res
    
    
    def getTraceById(self,id:int) -> FavoriteTraceEntity:
        res:FavoriteTraceEntity = FavoriteTraceEntity() 
        conn = self.__db.get_connection()
        query = """
                   SELECT id, id_user, id_editorial, date_trace
                   FROM public.editorial_favorite_trace WHERE 
                   id = %s;
                """

        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, (id,))
                rows = cur.fetchall()

                for row in rows:
                   res = FavoriteTraceEntity(id=row["id"],
                                                   idUser=row["id_user"],
                                                   idElement=row["id_editorial"],
                                                   dateOperation=str(row["date_trace"])
                                                   )
                self.__log.info(f"read trace editorial by id[{id}] ->" +
                                f"[OK] ->[{res.dateOperation}] date trace")

        except DatabaseError as e:
            self.__log.error(f"Error de operacion en la base" +
                             f"de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)

        return res
    

    def createTraceFavorite(self,trace: FavoriteTraceEntity) -> FavoriteTraceEntity:
        new_id = None
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = """
                   INSERT INTO public.editorial_favorite_trace
                   (id_user, id_category, date_trace) 
                   VALUES(%s, %s, now());
                    RETURNING id
                 """
                cur.execute(query, (
                trace.idUser,
                trace.idElement,
                ))
                
           
                new_id = cur.fetchone()['id']
                conn.commit() 
                self.__log.info(f"add trace favorite editorial -> [OK] -> #[{new_id}]")
            return self.getTraceById(new_id)
            
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


    def deleteTraceFavorite(self,trace: FavoriteTraceEntity) -> bool:
        res = False
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = """
                  DELETE FROM public.editorial_favorite_trace WHERE id=%s;
                 """
                cur.execute(query, (
                trace.id,
                
                ))

            
                conn.commit() 
                self.__log.info(f"delete trace favorite editorial -> [OK] -> #[{trace.id}]")
                res = True
            return res
            
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