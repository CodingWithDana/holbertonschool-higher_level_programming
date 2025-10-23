#!/usr/bin/python3
"""
List all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
# take 3 arguments: `mysql username`,`mysql password`, `database name`,
# use the module `SQLAlchemy`
# must import State and Base from model_state
# - `from model_state import Base, State`
# script should connect to a MySQL server running on localhost at port 3306
# must be sorted in ascending order by states.id
# your code should not be executed when imported

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # create the SQLAlchemy engine
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True       
    )
    
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # create a Sesion instance
    session = Session()
    
    # query all State objects sorted by states.id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # print results
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # close session
    session.close()
    