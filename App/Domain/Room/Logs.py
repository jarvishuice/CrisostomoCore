from Domain.GlobalValues import GlobalValues
import datetime
import logging


class Logs:
    """
    Clase Singleton para gestionar los logs de la aplicación, leyendo la configuración desde un archivo .conf.

    Attributes:
        __instance: Instancia única de la clase.
        logger: Objeto logger de Python para generar logs.
    """



  
    def __init__(self,name:str):
        
       
        # Configurar el logger
        logging.basicConfig(
            filename=f"{str(GlobalValues().getPathLogs)}Logs{datetime.date.today()}.log",
            level="INFO",
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        print(f"path:-> {str(GlobalValues().getPathLogs)}Logs{datetime.date.today()}.log")

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