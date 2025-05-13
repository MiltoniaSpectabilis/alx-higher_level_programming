#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # noqa

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.get(State, 1)
    print(f"{state.id}: {state.name}")
