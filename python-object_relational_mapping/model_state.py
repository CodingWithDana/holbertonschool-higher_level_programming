#!/usr/bin/python3
""" Definition of a State and an instance Base = declarative_base() """


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# Create the instance Base
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )
    name = Column(String(128), nullable=False)
