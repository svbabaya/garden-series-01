# from sqlalchemy.testing.schema import mapped_column

from .base import Base
from enum import Enum


class Mode(str, Enum):
    ORDINARY = "ordinary"


class Message(Base):
    pass
    # text: Mapped[str] = mapped_column()
    # author: Mapped[str] = mapped_column()
    # mode: Mapped[Mode] = mapped_column()
