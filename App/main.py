from fastapi import FastAPI
from API.Controllers.UserController import UserController
import uvicorn

app = FastAPI()
app.title = "CRISOSTO API"
app.version = "1.0.0"
# mapeo de controladores 
app.include_router(UserController,prefix="/API",)

if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8000)