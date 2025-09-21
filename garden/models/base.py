from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    # @declared_attr.directive
    # def __tablename__(self) -> str:
    #     return f"{self.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_displayed: Mapped[bool] = mapped_column(default=False)
    # created_at = Column(DateTime, default=func.now())
    # updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    # is_active = Column(Boolean, default=True)
