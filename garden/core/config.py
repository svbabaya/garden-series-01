from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

class DefaultText(BaseModel):
    author: str = ""
    message: str = ""


class Prefix(BaseModel):
    api_plants: str = "/api/plants"
    api_messages: str = "/api/messages"
    api_admin: str = "/api/admin"
    api_auth: str = "/api/auth"
    views_plants: str = "/plants"
    views_admin: str = "/admin"
    views_auth: str = "/auth"


class Tags:
    api_plants: list[str] = ["api-plants"]
    api_messages: list[str] = ["api-messages"]
    api_admin: list[str] = ["api-admin"]
    api_auth: list[str] = ["api-auth"]
    views_index: list[str] = ["home"]
    views_plants: list[str] = ["views-plants"]
    views_admin: list[str] = ["views-admin"]
    views_auth: list[str] = ["views-auth"]


class DatabaseConfig(BaseModel):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    echo: bool = True
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    prefix: Prefix = Prefix()
    tags: Tags = Tags()
    db: DatabaseConfig = DatabaseConfig()
    default_text: DefaultText = DefaultText()


settings = Settings()
