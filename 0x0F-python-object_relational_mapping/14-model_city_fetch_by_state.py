#!/usr/bin/python3
"""
This module joins cities and states tables
and prints their rows
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base as StateBase, State
from model_city import Base as CityBase, City


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )

    StateBase.metadata.create_all(engine)
    CityBase.metadata.create_all(engine)

    with Session(bind=engine) as session:
        query = session.query(City, State)
        query = query.join(State, City.state_id == State.id)
        cities_and_states = query.order_by(City.id)

        for city, state in cities_and_states:
            print(f"{state.name}: ({city.id}) {city.name}")
