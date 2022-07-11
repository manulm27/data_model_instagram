import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
class followers(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship(User)

class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text_comment = Column(String(500))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class MyEnum(enum.Enum):
    img = 'jpg'
    music = 'mp3'
    video = 'mp4'

class media(Base):
    __tablename__= 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MyEnum))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e