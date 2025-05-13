#!/usr/bin/python3
"""
This module lists all states containing the letter 'a'
from a specified db
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)
    query = query.filter(State.name.like("%a%"))
    query = query.order_by(State.id)
    states = query.all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
