from fastapi import FastAPI
import uvicorn

from routes import api_plants, web_plants

from core.config import settings

# from sqlalchemy.ext.asyncio import create_async_engine

app = FastAPI(title="School Garden Learning Portal", version="1.0.0")

# API routes
app.include_router(api_plants.router, prefix="/api/plants", tags=["api-plants"])
# app.include_router(api_admin.router, prefix="/api/admin", tags=["api-admin"])
# app.include_router(api_auth.router, prefix="/api/auth", tags=["api-auth"])

# Web routes
app.include_router(web_plants.router, prefix="/plants", tags=["web-plants"])
# app.include_router(web_admin.router, prefix="/admin", tags=["web-admin"])
# app.include_router(web_auth.router, prefix="/auth", tags=["web-auth"])


@app.get("/")
async def index():
    return [{"template": "index.html"}]


# @app.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(
        app="main:app", host=settings.run.host, port=settings.run.port, reload=True
    )
