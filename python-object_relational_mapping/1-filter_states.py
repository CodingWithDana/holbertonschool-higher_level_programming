#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa
"""
# write a script that lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa
# must use the module MySQLdb (import MySQLdb)
# connect to a MySQL server running on localhost at port 3306
# results must be sorted in ascending order by states.id
# your code should not be executed when imported


import MySQLdb
import sys


if __name__ == "__main__":
    # get command-line arguments
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

    # execute SQL query to find states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name 
                    LIKE BINARY 'N%' ORDER BY id ASC")

    # fetch all results
    rows = cursor.fetchall()

    # display results
    for row in rows:
        print(row)

    # close connections
    cursor.close()
    db.close()
