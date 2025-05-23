#!/usr/bin/python3
"""
This module contains the City class definition using SQLAlchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """ORM class representing the 'cities' table in the database."""
    __tablename__ = 'cities'

    id = Column(
        Integer,
        unique=True,
        autoincrement=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
    state = relationship("State", backref="cities")
