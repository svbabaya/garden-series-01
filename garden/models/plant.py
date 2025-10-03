from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from enum import Enum


class Category(str, Enum):
    TREE = "tree"
    BUSH = "bush"
    HERB = "herb"

class Location(str, Enum): # ToDo make individuals names for each zone not matrix
    ZONE11 = "1_1"
    ZONE12 = "1_2"
    ZONE13 = "1_3"
    ZONE21 = "2_1"
    ZONE22 = "2_2"
    ZONE23 = "2_3"
    ZONE31 = "3_1"
    ZONE32 = "3_2"
    ZONE33 = "3_3"

class Plant(Base):
    # __tablename__ = "plants"

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    intro: Mapped[str] = mapped_column(unique=False, nullable=False)
    thumbnail: Mapped[str] = mapped_column(unique=True, nullable=False)
    location: Mapped[Location] = mapped_column(unique=False, nullable=True)
    category: Mapped[Category] = mapped_column(unique=False, nullable=True)
    # articles: Mapped[Article]
