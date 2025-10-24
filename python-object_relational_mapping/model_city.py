#!/usr/bin/python3
""" Definition of a City and an instance Base = declarative_base() """


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


# Create the instance Base
Base = declarative_base()


class City(Base):
    """
    City class that links to the MySQL table 'cities'
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False,
        unique=True
    )
