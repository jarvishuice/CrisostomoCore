from psycopg2.pool import SimpleConnectionPool
from Domain.Room.Logs import Logs
class PsqlProvider:
    """
    Clase Singleton para manejar una única conexión a PostgreSQL a través de un pool.
    """
    log = Logs(__name__)

    __instance = None

    @staticmethod
    def get_instance(max_connections=100):
        """
        Devuelve la única instancia de la clase.

        Args:
            max_connections: Número máximo de conexiones en el pool (opcional).

        Returns:
            La instancia de la clase.
        """

        if PsqlProvider.__instance is None:
            params = {
                'host': 'localhost',  # Reemplaza con tu host
                'database': 'crisostomo',  # Reemplaza con tu base de datos
                'user': 'crisostomo',  # Reemplaza con tu usuario
                'password': '123456789',  # Reemplaza con tu contraseña
                'port': 5432  # Reemplaza si el puerto es diferente
            }
            PsqlProvider.__instance = PsqlProvider(params, max_connections)
        return PsqlProvider.__instance

    def __init__(self, params, max_connections):
     #   self.log.info("iniciando el pool ")
        self.pool = SimpleConnectionPool(minconn=1,maxconn=100, **params)

    def return_connection(self, conn):
        """
        Devuelve una conexión al pool.

        Args:
            conn: La conexión a devolver.
        """
        print("return conn  pool ")
        self.pool.putconn(conn)

    def close_all_connections(self):
        """
        Cierra todas las conexiones del pool.
        """
        self.pool.closeall()
    def get_connection(self):
        """
        Obtiene una conexión del pool.

        Returns:
            Una conexión a la base de datos.
        """

        return self.pool.getconn()


# Cerrar todas las conexiones (al finalizar la aplicación)
