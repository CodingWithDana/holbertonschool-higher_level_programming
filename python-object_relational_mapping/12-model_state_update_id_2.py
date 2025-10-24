#!/usr/bin/python3
"""
Change the name of a State object from the database hbtn_0e_6_usa
"""
# take 3 arguments: `mysql username`,`mysql password`, `database name`
# use the module `SQLAlchemy`
# must import State and Base from model_state
# - `from model_state import Base, State`
# script should connect to a MySQL server running on localhost at port 3306
# change the name of the State where id = 2 to New Mexico
# your code should not be executed when imported

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(
            "Usage: {} <username> <password> <db_name>".format(sys.argv[0])
        )
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

    # fetch the state with id = 2
    state = (
            session.query(State)
            .filter(State.id == 2)
            .first()
        )
    
    # change its name to "New Mexico" if it exists
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()