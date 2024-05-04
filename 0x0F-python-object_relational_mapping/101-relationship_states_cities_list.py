#!/usr/bin/python3
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
"""
    Lists all state Objects, and corresponding City objects,
        contained in the database hbtn_0e_101_usa
    Takes 3 arguments: mysql username, mysql password, and database name
    Must use the cities relationship for all State objects
    Results must be sorted in ascending order by states.id and cities.id
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id city.name))

    session.close()
