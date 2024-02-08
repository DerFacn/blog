from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey
from typing import List
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    uuid: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    password: Mapped[str]

    posts: Mapped[List['Post']] = relationship(back_populates='user', cascade='all, delete-orphan')

    is_active: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

    created: Mapped[str] = mapped_column(DateTime(), default=datetime.now())


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    body: Mapped[str]

    user_uuid: Mapped[str] = mapped_column(ForeignKey('users.uuid'))
    user: Mapped['User'] = relationship(back_populates='posts')

    likes_count: Mapped[int] = mapped_column(default=0)
    likes: Mapped[List['Like']] = relationship(back_populates='post')

    created_at: Mapped[str] = mapped_column(DateTime(), default=datetime.now())


class Like(Base):
    __tablename__ = 'likes'

    id: Mapped[int] = mapped_column(primary_key=True)

    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    post: Mapped[List['Post']] = relationship(back_populates='likes')

    user_uuid: Mapped[str] = mapped_column(ForeignKey('users.uuid'))
