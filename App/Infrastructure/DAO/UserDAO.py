from Domain.Exeptions.ExecptionDAO import ExeptionDAO
from Domain.Room.Logs import Logs
from Domain.Entity.UserEntity import UserEntity
from Infrastructure.Providers.DB.PsqlProvider import PsqlProvider
from Domain.Repository.IUserRepository import IUserRepository
from psycopg2.extras import RealDictCursor
from psycopg2 import IntegrityError,DatabaseError
class UserDAO(IUserRepository):
    """
    Clase para interactuar con la base de datos de usuarios.

    """
   
    def __init__(self):
        self.__log = Logs(__name__)
        self.__db:PsqlProvider = PsqlProvider.get_instance(100)
        
   
    def getUsers(self) -> list[UserEntity] :
        user =[]
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("select * from users")
                rows = cur.fetchall()
                for row in rows:
                    user.append(UserEntity(id=row["id"],
                                           name=row["name_primary"],
                                           lastname=row["last_name"],
                                           email=row["email"],
                                           password=row["password"],
                                           phone=row["phone"],
                                           username=row["username"],
                                           birthDate=str(row["birthdate"]),
                                           token=row["token"],
                                           status=row["status"], ))
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(f"Actualmente tenemos problema para procesar tu solicitud"+
                               "intente en un lapso de 5 minutos si el problema persiste"+
                               "comuinquese con el aadministrador del sistema  ")
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)   

        return user    
            
        
    
    def getUserById(self , id:int) -> UserEntity:
        user:UserEntity = None
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("select * from users where id = %s", (id,))
                rows = cur.fetchall()
                for row in rows:
                    user=UserEntity(       id=row["id"],
                                           name=row["name_primary"],
                                           lastname=row["last_name"],
                                           email=row["email"],
                                           password=row["password"],
                                           phone=row["phone"],
                                           username=row["username"],
                                           birthDate=str(row["birthdate"]),
                                           token=row["token"],
                                           status=row["status"],
                                           dateCreated=row["date_create"],
                                           dateUpdate=row["date_update"]
                                          )
        
        except DatabaseError as e :
            self.__log.warning(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(f"Actualmente tenemos problema para procesar tu solicitud"+
                               "intente en un lapso de 5 minutos si el problema persiste"+
                               "comuinquese con el aadministrador del sistema  ")
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
            
        
        finally:
            self.__db.return_connection(conn)   
            self.__log.info("devolviendo conexion") 
        
        return user    
    def addUser(self, user: UserEntity)->int:
        new_id = None
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = """
                    INSERT INTO public.users (name_primary, last_name, email, password,
                    phone, username, birthdate, token)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                 """
                cur.execute(query, (
                user.name.upper(),
                user.lastname.upper(),
                user.email,
                user.password,
                user.phone,
                user.username.upper(),
                user.birthDate,
                user.token
                ))
                
           
                new_id = cur.fetchone()['id']
                conn.commit() 
                self.__log.info("add user -> [OK]")
           
            
        except IntegrityError as e :
            self.__log.error(f"Error de integridad en la base de datos ->{e} ")
            raise ExeptionDAO(f"Error esta ingresando datos cuyos valores ya fueron "+ 
                              f"registrados por favor reviselos y si el problema persiste "+
                              f"comuniquese con el administrador del sistema ")
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(f"Actualmente tenemos problema para procesar tu solicitud"+
                               "intente en un lapso de 5 minutos si el problema persiste"+
                               "comuinquese con el aadministrador del sistema  ")
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)
        return new_id  
    
    def searchUser(self,param:str)->UserEntity:
        user:UserEntity = None
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""select * from users where name_primary = %s or 
                                phone = %s or email = %s or username = %s""", 
                                (param,param,param,param))
                rows = cur.fetchall()
                for row in rows:
                    user=UserEntity(id=row["id"],
                                           name=row["name_primary"],
                                           lastname=row["last_name"],
                                           email=row["email"],
                                           password=row["password"],
                                           phone=row["phone"],
                                           username=row["username"],
                                           birthDate=str(row["birthdate"]),
                                           token=row["token"],
                                           status=row["status"],
                                           dateCreated=row["date_create"],
                                           dateUpdate=row["date_update"]  )
        except DatabaseError as e :
            self.__log.warning(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(f"Actualmente tenemos problema para procesar tu solicitud"+
                               "intente en un lapso de 5 minutos si el problema persiste"+
                               "comuinquese con el aadministrador del sistema  ")
        except Exception as e:
            self.__log.warning(e)
            raise ExeptionDAO(e)
            
        
        finally:
            self.__db.return_connection(conn)   
            self.__log.info("devolviendo conexion") 
        
        return user
  
    def updateUser(self, user: UserEntity) -> int:
        res = 0
        conn = self.__db.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = """
                    UPDATE public.users SET name_primary= %s, last_name=%s, 
                    email=%s,username=%s , birthdate= %s, phone=%s, "token"=%s, 
                    status=%s,date_update= now() WHERE id=%s;
                 """
                cur.execute(query, (
                user.name.upper(),
                user.lastname.upper(),
                user.email,
                user.username.upper(),
                user.birthDate,
                user.phone,
                user.token,
                user.status,
                user.id
                ))
                
           
                res = user.id
                conn.commit() 
                self.__log.info("add user -> [OK]")
           
            
        except IntegrityError as e :
            self.__log.error(f"Error de integridad en la base de datos ->{e} ")
            raise ExeptionDAO(f"Error esta ingresando datos cuyos valores ya fueron "+ 
                              f"registrados por favor reviselos y si el problema persiste "+
                              f"comuniquese con el administrador del sistema ")
        except DatabaseError as e :
            self.__log.error(f"Error de operacion en la base de datos en la base de datos ->{e} ")
            raise ExeptionDAO(f"Actualmente tenemos problema para procesar tu solicitud"+
                               "intente en un lapso de 5 minutos si el problema persiste"+
                               "comuinquese con el aadministrador del sistema  ")
        except Exception as e:
            self.__log.error(e)
            raise ExeptionDAO(e)
        finally:
            self.__db.return_connection(conn)
        return res
    
