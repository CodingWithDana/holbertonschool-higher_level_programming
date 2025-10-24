#!/usr/bin/python3
""" Definition of a City and an instance Base = declarative_base() """


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


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
    state = relationship("State")
