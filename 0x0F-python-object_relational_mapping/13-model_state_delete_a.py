#!/usr/bin/python3
"""
This module deletes a state containing
the letter 'a' from the db using sqlalchemy
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )

    Base.metadata.create_all(engine)

    with Session(bind=engine) as session:
        states = session.query(State)\
            .filter(State.name.like('%a%')).delete()
        session.commit()
