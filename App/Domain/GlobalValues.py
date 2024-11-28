import os

class GlobalValues:
    DB_CONN_STR_PRIMARY = {
        'host': 'localhost',
        'database': 'crisostomo',
        'user': 'crisostomo',
        'password': '123456789',
        'port': 5432
    }
    def __init__(self):
        ...
    @property
    def getDbConnStrPrimary(self):
        return self.DB_CONN_STR_PRIMARY

    @property
    def getPathLogs(self):
        path = None
        if os.name == 'nt':
            path = "C:\\CrisostomoCore\\Logs\\"
        else:
            path = "/opt/CrisostomoCore/Logs/"
        return path

    @property
    def getIPServer(self):
        return "localhost"
    @property
    def getPortServer(self)-> int:
        return 8091
    @property
    def getVersionApp(self)-> str:
        return "1.0.0"
    @property
    def getDBEngine(self)->str:
        return "postgresql"
    @property
    def getMsgDbErro(self)->str:
        msg=f"""Actualmente tenemos problema para procesar tu solicitud 
            intente en un lapso de 5 minutos si el problema persiste 
            comuinquese con el aadministrador del sistema  """
        return msg
    

