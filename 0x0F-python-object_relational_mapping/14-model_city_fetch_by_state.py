#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
"""
    Prints all City objects from the database hbtn_0e_14_usa
    Takes 3 arguments: mysql username, mysql password, and database name
    Results must be sorted in ascending order by cities.id
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(City.state_id == State.id) \
                    .order_by(city.id)

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()

    session.close()
