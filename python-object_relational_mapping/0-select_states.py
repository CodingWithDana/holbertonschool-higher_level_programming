#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys
# write a script that lists all states from the database hbtn_0e_0_usa:
    # your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    # use the module MySQLdb (import MySQLdb)
    # your script should connect to a MySQL server running on localhost at port 3306
    # results must be sorted in ascending order by states.id
    # your code should not be executed when imported
    

# your code should not be executed when imported
if __name__== "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connect to MySQL server using provided credentials to interact with the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create a cursor object to send the SQL query to MySQL
    cur = db.cursor()
    
    # Execute SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all results
    rows = cur.fetchall()
    
    # Print results
    for row in rows:
        print(row)
        
    # Close cursor and connection
    cur.close()
    db.close()
    