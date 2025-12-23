"""
User
id
name 
surname
username
password
phone_number
email
date_of_birth
reg_date


UserPost
id
main_text
uid
reg_date


PostPhoto
id
photo_path
pid


Comment
id
text
uid
pid
reg_date

"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False) 
    surname = Column(String)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    date_of_birth = Column(String)
    reg_date = Column(DateTime, default=datetime.now())


class UserPost(Base):
    __tablename__ = "userposts"
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_text = Column(String, nullable=False)
    uid = Column(Integer, ForeignKey("users.id"))
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship("User", lazy="subquery")


class PostPhoto(Base):
    __tablename__ = "photos"
    id = Column(Integer, autoincrement=True, primary_key=True)
    photo_path = Column(String, nullable=False)
    pid = Column(Integer, ForeignKey("userposts.id"))

    post_fk = relationship("UserPost", lazy="subquery")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String, nullable=False)
    uid = Column(Integer, ForeignKey("users.id"))
    pid = Column(Integer, ForeignKey("userposts.id"))
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship("User", lazy="subquery")
    post_fk = relationship("UserPost", lazy="subquery")







