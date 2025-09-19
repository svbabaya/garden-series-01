from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class Prefix(BaseModel):
    api_plants: str = "/api/plants"
    api_admin: str = "/api/admin"
    api_auth: str = "/api/auth"
    web_plants: str = "/plants"
    web_admin: str = "/admin"
    web_auth: str = "/auth"


class Tags:
    api_plants: list[str] = ["api-plants"]
    api_admin: list[str] = ["api-admin"]
    api_auth: list[str] = ["api-auth"]
    web_plants: list[str] = ["web-plants"]
    web_admin: list[str] = ["web-admin"]
    web_auth: list[str] = ["web-auth"]


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    prefix: Prefix = Prefix()
    tags: Tags = Tags()
    # db_url: str = "sqlite+aiosqlite:///garden.sqlite"


settings = Settings()
