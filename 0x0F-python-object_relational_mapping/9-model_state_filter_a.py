#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
"""
    Lists all State objects that contain the letter a from the database
    Takes 3 arguments: mysql username, mysql password, and database name
    Stored in ascending order by states.id
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.contains('a')):
        print("{}: {}".format(state.id, state.name))

    session.close()
