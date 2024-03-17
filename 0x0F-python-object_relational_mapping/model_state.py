#!/usr/bin/python3
"""
This module defines the State class and an instance of Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Represents a state in the MySQL table states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Import necessary modules and create engine
    from sqlalchemy import create_engine
    engine = create_engine('mysql://username:password@localhost:3306/database')

    # Create tables
    Base.metadata.create_all(engine)
