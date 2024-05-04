#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
"""
    Adds the State object "Louisiana" to the database hbtn_0e_6_usa
    Takes 3 arguments: mysql username, mysql password, and database name
    Print the new states.id after creation
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    Print("{}".format(new_state.id))

    session.close()
