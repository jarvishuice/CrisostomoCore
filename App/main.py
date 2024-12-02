from fastapi import FastAPI
from API.Controllers.UserController import UserController
from API.Controllers.AuthorController import AuthorController
from API.Controllers.EditorialController import EditorialController
from API.Controllers.CategroyController import CategoryController
from Domain.GlobalValues import GlobalValues
from Domain.Room.Logs import Logs
import uvicorn

log = Logs(__name__)

app = FastAPI()
app.title = "CRISOSTO API"
app.version = "1.0.0"
log.info("init core")
log.info("starting server")
log.info(f"build map Controllers")


# mapeo de controladores
#=====================================================

app.include_router(UserController, prefix="/API",)
app.include_router(AuthorController, prefix="/API",)
app.include_router(EditorialController, prefix="/API",)
app.include_router(CategoryController, prefix="/API",)
#=====================================================

log.info(f" builder controller Complete") 
log.info(f"server Crisostomo started on " +
         f"http://{GlobalValues().getIPServer}" +
         f":{GlobalValues().getPortServer}")

if __name__ == "__main__":

    uvicorn.run(
        app,
        host=GlobalValues().getIPServer,
        port=GlobalValues().getPortServer
    )
