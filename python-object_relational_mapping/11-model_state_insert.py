#!/usr/bin/python3
"""
Add the State object “Louisiana” to the database hbtn_0e_6_usa
"""
# take 3 arguments: `mysql username`,`mysql password`, `database name`
# use the module `SQLAlchemy`
# must import State and Base from model_state
# - `from model_state import Base, State`
# script should connect to a MySQL server running on localhost at port 3306
# print the new states.id after creation
# your code should not be executed when imported

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # create a new State object
    new_state = State(name="Louisiana")

    # add and commit the new state
    session.add(new_state)
    session.commit()

    # print the new state's id
    print(new_state.id)

    # close the session
    session.close()
