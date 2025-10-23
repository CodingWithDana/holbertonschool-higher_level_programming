#!/usr/bin/python3
"""
Print the first State object from the database hbtn_0e_6_usa
"""
# take 3 arguments: `mysql username`,`mysql password`, `database name`,
# use the module `SQLAlchemy`
# must import State and Base from model_state
# - `from model_state import Base, State`
# script should connect to a MySQL server running on localhost at port 3306
# the state you display must be the first in states.id
# not allowed to fetch all states from the database before displaying the result
# if the table states is empty, print Nothing followed by a new line
# your code should not be executed when imported

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # create the engine connection string
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )
    
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # create a Sesion instance
    session = Session()
    
    # get the first State object (ordered by id)
    first_state = session.query(State).order_by(State.id).first()
    
    # display result
    # check: if first_state not empty
    if first_state is not None:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")


# $ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
# Expected Output:
# 1: California