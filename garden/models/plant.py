from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from enum import Enum


class Category(str, Enum):
    TREE = "tree"
    BUSH = "bush"
    HERB = "herb"

class Location(str, Enum):
    ZONE11 = "11"
    ZONE12 = "12"
    ZONE13 = "13"
    ZONE21 = "21"
    ZONE22 = "22"
    ZONE23 = "23"
    ZONE31 = "31"
    ZONE32 = "32"
    ZONE33 = "33"

class Plant(Base):
    # __tablename__ = "plants"

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    intro: Mapped[str] = mapped_column(unique=False, nullable=False)
    thumbnail: Mapped[str] = mapped_column(unique=True, nullable=False)
    location: Mapped[Location] = mapped_column(unique=False, nullable=True)
    category: Mapped[Category] = mapped_column(unique=False, nullable=True)
    # articles: Mapped[Article]
