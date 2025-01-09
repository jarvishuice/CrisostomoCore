from Infrastructure.Providers.DB.PsqlProvider import PsqlProvider
from Domain.Room.Logs import Logs
from Domain.Repository.IEditorialRepository import IEditorialRepository
from Domain.Entity.EditorialEntity import EditorialEntity
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.GlobalValues import GlobalValues
from psycopg2.extras import RealDictCursor
from psycopg2 import IntegrityError, DatabaseError


class EditorialDAO(IEditorialRepository):
    def __init__(self):
        self.__log = Logs(__name__)
        self.__db: PsqlProvider = PsqlProvider.get_instance(100)

    @property
    def getEditorials(self) -> list[EditorialEntity]:
        res = []
        conn = self.__db.get_connection()
        query = "select * from editorial"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    res.append(EditorialEntity(id=row["id"],
                                               name=row["name"]
                                               ))
                self.__log.info(f"read all Editorials ->" +
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


    def getEditorialById(self, id: int) -> EditorialEntity:
        res: EditorialEntity = None
        conn = self.__db.get_connection()
        query = "select * from editorial where id = %s"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, (id,))
                rows = cur.fetchall()
                if len(rows) > 0:

                    for row in rows:
                        res = EditorialEntity(id=row["id"],
                                              name=row["name"],
                                              )
                    self.__log.info(f"read  Editorial #{id} ->" +
                                    f"[OK] ->[{res.name}] ")
                else:
                    self.__log.info(f"read  Editorial #{id} ->" +
                                    "[Not Found]")
        except DatabaseError as e:
            self.__log.error("Error de operacion en la base " +
                             f"de datos en la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)

        return res


    def searchEditorial(self, param: str) -> list[EditorialEntity]:
        res = []
        conn = self.__db.get_connection()
        query = "select * from editorial where name like  %s ;"
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, (f"%{param}%",))
                rows = cur.fetchall()
                if len(rows) > 0:

                    for row in rows:
                        res.append(EditorialEntity(
                            id=row["id"],
                            name=row["name"],
                        )
                        )
                    self.__log.info(f"search  Editorial #{param} ->[OK] ->" +
                                    f"[{len(res)}] Editorial ")
                else:
                    self.__log.info(f"search  Editorial #{param} ->" +
                                    "[Not Found]")
        except DatabaseError as e:
            self.__log.error(f"Error de operacion en la base de datos en" +
                             "la base de datos ->{e} ")
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)
        return res


    def addEditorial(self, editorial: EditorialEntity) -> int:
        new_id = None
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = """
                    INSERT INTO public.editorial ( name) 
                    VALUES (%s)
                    RETURNING id
                 """
                cur.execute(query, (
                    editorial.name.upper(),
                ))

                new_id = cur.fetchone()['id']
                conn.commit()
                self.__log.info(f"add editorial -> [OK] ->" +
                                f"#[{new_id}]")
            return new_id

        except IntegrityError as e:
            self.__log.error(f"""Error de integridad en la base de
                               datos ->{e} """)
            raise ExeptionDAO(GlobalValues().getMsgDbIntErrors)
        except DatabaseError as e:
            self.__log.error(f"""Error de operacion en la base de
                              datos en la base de datos ->{e} """)
            raise ExeptionDAO(GlobalValues().getMsgDbError)
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)
