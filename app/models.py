from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, LargeBinary

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    uuid: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25), index=True, unique=True)
    password: Mapped[str] = mapped_column(LargeBinary())
