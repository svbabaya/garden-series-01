from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class Prefix(BaseModel):
    public_api_prefix: str = "/api/"
    admin_api_prefix: str = "/api/admin"
    # public_template_prefix: str = "/garden"
    # admin_template_prefix: str = "/garden/admin"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    prefix: Prefix = Prefix()
    db_url: str = "sqlite+aiosqlite:///garden.sqlite"


settings = Settings()
