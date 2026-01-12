"""Database models for users, posts, and likes"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # primary key
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # added password column

    posts = relationship("Post", back_populates="author")
    likes = relationship("Like", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # link to User by id
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    image_filename = Column(String, nullable=True)
    likes = Column(Integer, default=0)  # fixed typo

    author = relationship("User", back_populates="posts")
    liked_by = relationship(
        "Like", back_populates="post")  # fixed relationship


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="liked_by")
    user = relationship("User", back_populates="likes"
                        )
