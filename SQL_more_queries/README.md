## Topics:
    - How to create a new MySQL user
    - How to manage privileges for a user to a database or table
    - What’s a PRIMARY KEY
    - What’s a FOREIGN KEY
    - How to use NOT NULL and UNIQUE constraints
    - How to retrieve datas from multiple tables in one request
    - What are subqueries
    - What are JOIN and UNION

### Notes:
- The database name will be passed as an argument of the mysql command:(mysql command starts with `mysql`)
    mysql -hlocalhost -uroot -p <database_name>


- How to test:
    cat <file_name>.sql | mysql -hlocalhost -uroot -p <database_name>