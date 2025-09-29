from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from enum import Enum


class Mode(str, Enum):
    ORDINARY = "ordinary"


class Message(Base):
    # __tablename__ = "messages"

    text: Mapped[str] = mapped_column(unique=True, nullable=False)
    caption: Mapped[str] = mapped_column(unique=False, nullable=False)
    mode: Mapped[Mode] = mapped_column(default=Mode.ORDINARY, unique=False)
