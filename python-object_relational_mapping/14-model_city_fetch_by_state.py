#!/usr/bin/python3
"""
Print all City objects from the database hbtn_0e_14_usa
"""
# take 3 arguments: `mysql username`,`mysql password`, `database name`
# use the module `SQLAlchemy`
# must import State and Base from model_state
# - `from model_state import Base, State`
# script should connect to a MySQL server running on localhost at port 3306
# results must be sorted in ascending order by cities.id
# results must be display as they are in the
# example below (<state name>: (<city id>) <city name>)
# your code should not be executed when imported

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: {} <username> <password> <db_name>".format(sys.argv[0])
        )
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL on localhost:3306
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}"
        f"@localhost:3306/{db_name}",
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # query all City objects, sorted by cities.id in ASC order
    for city in session.query(City).join(State).order_by(City.id).all():
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
