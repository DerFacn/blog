from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, LargeBinary, ForeignKey
from typing import List

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    uuid: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25), index=True, unique=True)
    password: Mapped[str] = mapped_column(LargeBinary())
    posts: Mapped[List['Post']] = relationship(back_populates='user', cascade='all, delete-orphan')


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    body: Mapped[str]
    user_uuid: Mapped[str] = mapped_column(ForeignKey('users.uuid'))
    user: Mapped['User'] = relationship(back_populates='posts')
