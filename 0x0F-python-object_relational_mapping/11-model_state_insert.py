#!/usr/bin/python3

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    new_state = State(name="Louisiana")
    session.add(new_state)

    state = session.query(State).filter(State.name == "Louisiana").first()
    print(state.id)
