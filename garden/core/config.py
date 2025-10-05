from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class DefaultStrings(BaseModel):
    message_caption: str = "Confucius"
    message_text: str = "Rice keeps me alive, but flowers give me a reason to stay alive"


class Prefix(BaseModel):
    api_plants: str = "/api/plants"
    api_messages: str = "/api/messages"
    view_user: str = "/user"
    view_admin: str = "/admin"


class Tags:
    api_plants: list[str] = ["api-plants"]
    api_messages: list[str] = ["api-messages"]
    view_user: list[str] = ["view-user"]
    view_admin: list[str] = ["view-admin"]
    view_home: list[str] = ["view-home"]


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
    default_strings: DefaultStrings = DefaultStrings()


settings = Settings()
