#!/usr/bin/python3
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
"""
    Creates the State “California” with the City “San Francisco”
        from the database hbtn_0e_100_usa
    Takes 3 arguments: mysql username, mysql password, and database name
    Must use the cities relationship for all State objects
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    city = City(name="San Francisco", state=State(name="California"))
    session.add(city)

    session.commit()

    session.close()
