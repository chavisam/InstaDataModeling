import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(Integer)
    email = Column(String(200),unique=True)
    posts = relationship('post', backref='User', lazy=True)
    follower = relationship('follower', backref='User', lazy=True)

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    follower_id = Column(Integer, ForeignKey('user.id'),nullable=False, primary_key=True)
    user_id = Column(Integer, nullable=False)


class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    media = relationship('media', backref='post', lazy=True)
    comment = relationship('comment', backref='Post', lazy=True)

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    post_id = Column(Integer,ForeignKey('post.id'), nullable=False)
    image_url = Column(String(250))
    type = Column(String(250), nullable=False)



class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    plot = Column(String(350),nullable=False)
    user_id = Column(Integer, nullable=False)
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e