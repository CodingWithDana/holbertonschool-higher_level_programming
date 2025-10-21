#!/usr/bin/python3
""" 
Display all values in `states` table of `hbtn_0e_0_usa`
where `name` matches the argument 
"""
# take 4 arguments: `mysql username`,`mysql password`, `database name`,
# `state name searched`
# use the module `MySQLdb` (import MySQLdb)
# script should connect to a MySQL server running on localhost at port 3306
# use format to create the SQL query with the user input
# results must be sorted in ascending order by states.id
# your code should not be executed when imported


import MySQLdb
import sys


if __name__ == "__main__":
    # get command-line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]
    
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
    
    # execute SQL query to display all values where 
    # `name` matches the argument
    cursor.execute(
        " SELECT * FROM states WHERE name = %s", (state_name_searched,)
    )
    
    # fetch and display all matching rows
    for row in cursor.fetchal():
        print(row)
        
    # close the connection
    cursor.close()
    db.close()