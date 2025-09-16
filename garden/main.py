from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return "Hi, fastapi"


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
