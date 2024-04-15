#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
"""
    Lists all State objects from the database hbtn_0e_6_usa
    Takes 3 arguments: mysql username, mysql password, and database name
    Stored in ascending order by states.id
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bird=engine)
    session = Session()

    for state in session.query(state).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    session.close()
