from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from enum import Enum


# class Display(str, Enum):
#     ENABLED = "enabled"
#     DISABLED = "disabled"
#
#
# class State(str, Enum):
#     CREATED = "created"
#     UPDATED = "updated"
#     DELETED = "deleted"


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
    # display: Mapped[Display] = mapped_column(default=Display.DISABLED)
    # state: Mapped[State] = mapped_column(default=State.CREATED)
    # timestamp: Mapped

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=True)
