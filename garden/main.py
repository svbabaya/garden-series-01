from fastapi import FastAPI
import uvicorn
import routes
from core.config import settings

from sqlalchemy.ext.asyncio import create_async_engine

app = FastAPI()


@app.get("/")
async def index():
    return [
        {
            "template": "index.html",
            "category_list": [1, 2, 3, 4, 5],
            "message": "Text of message",
            "author": "Author of message",
            "routes": "ToDo",
        }
    ]


@app.get("/plants/{category_id}")
async def get_category(category_id: int):
    return [{"template": "category.html", "category_id": category_id, "routes": "ToDo"}]


@app.get("/plants/{category_id}/{plant_id}")
async def get_plant(category_id: int, plant_id: int):
    return [
        {
            "template": "plant.html",
            "category_id": category_id,
            "plant_id": plant_id,
            "routes": "ToDo",
        }
    ]


app.include_router(api_router, prefix=settings.api.prefix)
# app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app", host=settings.run.host, port=settings.run.port, reload=True
    )
