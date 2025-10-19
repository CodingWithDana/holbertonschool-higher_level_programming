## Background Context
    - In this project, you will link two amazing worlds: Databases and Python!
    - In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries
    - In the second part, you will use the module SQLAlchemy (a Python module to help you match) an Object Relational Mapper (ORM)
    - With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”
        - You won’t write any SQL queries only Python code




## Learning Objectives
    - How to connect to a MySQL database from a Python script
    - How to SELECT rows in a MySQL table from a Python script
    - How to INSERT rows in a MySQL table from a Python script
    - What ORM means
    - How to map a Python Class to a MySQL table




## Examples
    # Without ORM
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database

    query_rows = cur.fetchall()

    for row in query_rows:

        print(row)

    cur.close()

    conn.close()


    # With ORM
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!

        print("{}: {}".format(state.id, state.name))
        
    session.close()
