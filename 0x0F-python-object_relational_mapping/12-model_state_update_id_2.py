#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
"""
    Changes the name of a State object from the database hbtn_0e_6_usa
    Takes 3 arguments: mysql username, mysql password, and database name
    Change the name of the State where id = 2 to New Mexico
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
