#!/usr/bin/python3
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
"""
    Lists all City objects from the database hbtn_0e_101_usa
    Takes 3 arguments: mysql username, mysql password, and database name
    Must use the states relationship to access to the State object
        linked to the City object
    Results must be sorted in ascending order by cities.id
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for i_city in session.query(City).order_by(City.id):
        print("{}: {} -> {}". format(i_city.id, i_city.name,
              i_city.state.name))

    session.close()
