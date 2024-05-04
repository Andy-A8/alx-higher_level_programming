#!/usr/bin/python3
"""
    Defines a class City
    Inherits from SQLAlchemy Base and links to the MYSQL table cities
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city class for a MYSQL database

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the city
        name (str): The name of city
        state_id (int): The state the city belongs to
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
