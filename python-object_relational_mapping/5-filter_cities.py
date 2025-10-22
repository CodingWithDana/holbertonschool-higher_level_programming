#!/usr/bin/python3
"""
Take the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""
# take 4 arguments: `mysql username`,`mysql password`, `database name`,
# `state name`
# use the module `MySQLdb` (import MySQLdb)
# script should connect to a MySQL server running on localhost at port 3306
# results must be sorted in ascending order by cities.id
# can use only execute() once
# your code should not be executed when imported


import MySQLdb
import sys

if __name__ == "__main__":
    # get command-line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # execute query (note %s cannot be quoted)
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;"
    )

    # execute with a tuple argument (state_name,)
    cursor.execute(query, (state_name,))

    # fetchall() returns a list of tuples (cities)
    rows = cursor.fetchall()
    # combine all row tuples into a single string separated by ,
    print(", ".join([row[0] for row in rows]))

    # close the connection
    cursor.close()
    db.close()
