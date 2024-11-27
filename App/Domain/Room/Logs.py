import datetime
import inspect
import logging
import configparser
import os
from configAPP import PATH_LOGS

class Logs:
    """
    Clase Singleton para gestionar los logs de la aplicación, leyendo la configuración desde un archivo .conf.

    Attributes:
        __instance: Instancia única de la clase.
        logger: Objeto logger de Python para generar logs.
    """



  
    def __init__(self,name:str):
        # Cargar la configuración desde el archivo .conf
        config = configparser.ConfigParser()
        #print("esta es la ruta"+os.path.join(os.path.dirname(__file__), 'configApp.conf'))
        #config_path = os.path.join(os.path.dirname(__file__), 'configApp.conf')  # Ajusta la ruta
       # config.read(config_path)
        caller_class = inspect.stack()[2][3]
        # Configurar el logger
        logging.basicConfig(
            filename=f"{PATH_LOGS}\Logs{datetime.date.today()}.log",
            level="INFO",
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        self.logger = logging.getLogger(name)

    def info(self, message):
        """
        Logea un mensaje a nivel INFO.
        """
        self.logger.info(message)

    def debug(self, message):
        """
        Logea un mensaje a nivel DEBUG.
        """
        self.logger.debug(message)

    def warning(self, message):
        """
        Logea un mensaje a nivel WARNING.
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Logea un mensaje a nivel ERROR.
        """
        self.logger.error(message)