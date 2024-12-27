from Domain.Values.filterBookValues import FILTER_BOOK
from Domain.Entity.AppConfigRouteNavEntity import AppConbfigRouteNavEntity
from Domain.Repository.IAppConfigRouteNavReopository import IAppConfigRouteNavReopository
from Infrastructure.Providers.DB.PsqlProvider import PsqlProvider
from Domain.Room.Logs import Logs
from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.GlobalValues import GlobalValues
from psycopg2.extras import RealDictCursor
from psycopg2 import IntegrityError, DatabaseError


class AppConfigRouteNavDAO(IAppConfigRouteNavReopository):

    def __init__(self):
        self.__log = Logs(__name__)
        self.__db: PsqlProvider = PsqlProvider.get_instance(100)

    @property
    def getAll(self) -> list[AppConbfigRouteNavEntity]:
        res = []
        conn = self.__db.get_connection()
        query = """
                   SELECT * FROM public.app_config_routes_navigator
                   order by name_route asc
                """

        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    res.append(AppConbfigRouteNavEntity(id=row["id"],
                                                        cod=row["code"],
                                                        nameRoute=row["name_route"],
                                                        path=row["path"],
                                                        typeUser=row["type_user"],
                                                        pageName=row["page_name"],
                                                        status=row["status"],
                                                        icon=row["icon"],
                                                        ))
                self.__log.info(f"read all Routes path navigation ->" +
                                f"[OK] ->[{len(res)}] routes")

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

    def getByTypeUser(self, typeUser: int) -> list[AppConbfigRouteNavEntity]:
        res = []
        conn = self.__db.get_connection()
        query = """select * from public.app_config_routes_navigator
                   where type_user = %s and status = 1 """
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, (typeUser,))
                rows = cur.fetchall()
                for row in rows:
                    res.append(AppConbfigRouteNavEntity(id=row["id"],
                                                   cod=row["code"],
                                                   nameRoute=row["name_route"],
                                                   path=row["path"],
                                                   typeUser=row["type_user"],
                                                   pageName=row["page_name"],
                                                   status=row["status"],
                                                   icon=row["icon"],

                                                   ))
                self.__log.info(f"get Routes bytypeUser #{typeUser} ->" +
                                f"[OK] ->[{len(res)}]")

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
