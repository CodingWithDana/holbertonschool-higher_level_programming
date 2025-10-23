#!/usr/bin/python3
"""
Print the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
# take 3 arguments: `mysql username`,`mysql password`, `database name`,
# `state name to search``
# use the module `SQLAlchemy`
# must import State and Base from model_state
# - `from model_state import Base, State`
# script should connect to a MySQL server running on localhost at port 3306
# assume you have one record with the state name to search
# results must display the states.id
# if no state has the name you searched for, display Not found
# your code should not be executed when imported

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("""
            "Usage: {} <username> <password> <db_name> <state_name>"
            .format(sys.argv[0]))
        """)
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL on localhost:3306
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}"
        f"@localhost:3306/{db_name}",
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Parameterise SQLAlchemy query (safe from SQL injection)
        state = (
            session.query(State)
            .filter(State.name == state_name)
            .first()
        )
        if state is not None:
            print(state.id)
        else:
            print("Not found")
    finally:
        session.close()
