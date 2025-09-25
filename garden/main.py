from contextlib import asynccontextmanager
from models import db_helper, Base

from fastapi import FastAPI
import uvicorn

from routes import api_plants, api_messages, web_plants

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
    # lifespan=lifespan,
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

# main_app.include_router(api_admin.router, deprecated=False, prefix=settings.prefix.api_admin, tags=settings.tags.api_admin)
# main_app.include_router(api_auth.router, deprecated=False, prefix=settings.prefix.api_auth, tags=settings.tags.api_auth)

# Web routes
# main_app.include_router(
#     web_plants.router,
#     deprecated=False,
#     prefix=settings.prefix.web_plants,
#     tags=settings.tags.web_plants,
#     responses={404: {"description": "Not found"}},
# )

# main_app.include_router(web_admin.router, deprecated=False, prefix=settings.prefix.web_admin, tags=settings.tags.web_admin)
# main_app.include_router(web_auth.router, deprecated=False, prefix=settings.prefix.web_auth, tags=settings.tags.web_auth)


@main_app.get("/", tags=["home"])
async def index():
    return [{"template": "index.html"}]


if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
