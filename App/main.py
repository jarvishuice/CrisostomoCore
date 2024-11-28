from fastapi import FastAPI
from API.Controllers.UserController import UserController
from Domain.GlobalValues import GlobalValues
import uvicorn

from Domain.Room.Logs import Logs
log = Logs(__name__)


app = FastAPI()
app.title = "CRISOSTO API"
app.version = "1.0.0"
log.info("init core")
log.info("starting server")
log.info(f"check path Logs ->[ok] -> {str(GlobalValues().getPathLogs)}")
log.info(f"check engine Db -> [ok] -> {GlobalValues().getDBEngine}")
# mapeo de controladores
app.include_router(UserController, prefix="/API",)
log.info(f"server Crisostomo started on " +
         f"http://{GlobalValues().getIPServer}" +
         f":{GlobalValues().getPortServer}")

if __name__ == "__main__":

    uvicorn.run(
        app,
        host=GlobalValues().getIPServer,
        port=GlobalValues().getPortServer
    )
