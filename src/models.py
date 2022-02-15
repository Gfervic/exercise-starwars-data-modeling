import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user.
    #  Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(22), nullable=False)
    login = Column(Boolean)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table user.
    #  Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    age = Column(Integer)
    # Age should be an integer or a string. When which one? 🤔

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table user.
    #  Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    weater = Column(String(150))

class FavChar(Base):
    __tablename__ = 'favchar'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class FavPlan(Base):
    __tablename__ = 'favplanet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')