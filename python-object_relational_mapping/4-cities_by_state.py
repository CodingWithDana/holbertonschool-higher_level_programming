#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa
"""
# take 3 arguments: `mysql username`,`mysql password`, `database name`,
# use the module `MySQLdb` (import MySQLdb)
# script should connect to a MySQL server running on localhost at port 3306
# results must be sorted in ascending order by cities.id
# can use only execute() once
# your code should not be executed when imported

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # create a cursor to execute queries
    cursor = db.cursor()

    # execute SQL query to display all cities
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )

    # fetch and display all matching rows
    for row in cursor.fetchall():
        print(row)

    # close the connection
    cursor.close()
    db.close()
