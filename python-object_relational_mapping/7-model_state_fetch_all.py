#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""
# take 3 arguments: `mysql username`,`mysql password`, `database name`,
# use the module `SQLAlchemy`
# must import State and Base from model_state 
# - `from model_state import Base, State`
# script should connect to a MySQL server running on localhost at port 3306
# results must be sorted in ascending order by states.id
# your code should not be executed when imported


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # create database engine connection
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all State objects, sorted by states.id in ASC order
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
