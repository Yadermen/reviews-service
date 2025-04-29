from fastapi import FastAPI
from src.api.__init__ import main_router
import uvicorn

app = FastAPI()

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True, host="0.0.0.0")