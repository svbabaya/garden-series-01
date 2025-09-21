from sqlalchemy.orm import Mapped
from .base import Base
from enum import Enum


class Mode(str, Enum):
    ORDINARY = "ordinary"


class Message(Base):
    __tablename__ = "messages"

    text: Mapped[str]
    author: Mapped[str]
    mode: Mapped[Mode]
