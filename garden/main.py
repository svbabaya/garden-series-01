from contextlib import asynccontextmanager
from models import Base, db_helper

from fastapi import FastAPI
import uvicorn

from routes import api_plants, api_messages, web_plants

from core.config import settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(
    title="School Garden Learning Portal",
    version="1.0.0",
    lifespan=lifespan,
)

# API routes
app.include_router(
    api_plants.router,
    deprecated=False,
    prefix=settings.prefix.api_plants,
    tags=settings.tags.api_plants,
    responses={404: {"description": "Not found"}},
)
app.include_router(
    api_messages.router,
    deprecated=False,
    prefix=settings.prefix.api_messages,
    tags=settings.tags.api_messages,
    responses={404: {"description": "Not found"}},
)

# app.include_router(api_admin.router, deprecated=False, prefix=settings.prefix.api_admin, tags=settings.tags.api_admin)
# app.include_router(api_auth.router, deprecated=False, prefix=settings.prefix.api_auth, tags=settings.tags.api_auth)

# Web routes
app.include_router(
    web_plants.router,
    deprecated=False,
    prefix=settings.prefix.web_plants,
    tags=settings.tags.web_plants,
    responses={404: {"description": "Not found"}},
)
# app.include_router(web_admin.router, deprecated=False, prefix=settings.prefix.web_admin, tags=settings.tags.web_admin)
# app.include_router(web_auth.router, deprecated=False, prefix=settings.prefix.web_auth, tags=settings.tags.web_auth)


@app.get("/", tags=["home"])
async def index():
    return [{"template": "index.html"}]


if __name__ == "__main__":
    uvicorn.run(
        app="main:app", host=settings.run.host, port=settings.run.port, reload=True
    )
