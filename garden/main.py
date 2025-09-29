from contextlib import asynccontextmanager

from models import db_helper, Base

from fastapi import FastAPI
import uvicorn

from routes import api_plants, api_messages, views_index, views_plants

from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown
    await db_helper.dispose()

main_app = FastAPI(
    title="School Garden Learning Portal",
    version="1.0.0",
    lifespan=lifespan,
)

# API routes
# main_app.include_router(
#     api_plants.router,
#     deprecated=False,
#     prefix=settings.prefix.api_plants,
#     tags=settings.tags.api_plants,
#     responses={404: {"description": "Not found"}},
# )
main_app.include_router(
    api_messages.router,
    deprecated=False,
    prefix=settings.prefix.api_messages,
    tags=settings.tags.api_messages,
    responses={404: {"description": "Not found"}},
)

# Views routes
main_app.include_router(
    views_index.router,
    deprecated=False,
    tags=settings.tags.views_index,
    responses={404: {"description": "Not found"}},
)


if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
