from .base import Base
from enum import Enum

class Mode(str, Enum):
    pass

class Message(Base):
    text
    author
    mode
