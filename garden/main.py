from fastapi import FastAPI
import uvicorn
from api import router as api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")


@app.get("/")
def index():
    return "Hi, fastapi"


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
