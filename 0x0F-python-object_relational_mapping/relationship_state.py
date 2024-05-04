#!/usr/bin/python3
"""
    Defines a class State, and an instance from SQLAlchemy Base
        and links to the MYSQL table state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state class for a MYSQL database

    Attributes:
        __tablename__(str): The table name of the class to store States
        id (integer): The id of states
        name (str): The name of states
        cities: The State-City relationship
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", brackref="state", cascade="all, delete")
