### Server-side Rendering
- SSR is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML.

- This contrasts with client-side rendering, where web pages are built on the browser using JavaScript and dynamic data.

- Through this project, you will learn how to implement SSR using Python and Flask, leveraging the Jinja templating engine to create dynamic, efficient, and SEO-friendly web applications.

---

### How to test the program 
#### For Task 0: How to create personalized invitation cards from a template
    - In the terminal, run
        - cd python-server_side_rendering
        - python3 00-main.py

    - Then check the folder `python-server_side_rendering`, you should see files (each file for each guest)
        output_1.txt
        output_2.txt
        output_3.txt

#### For Task 1: How to render a web page using Jinja template and Flask
    - To start the Flask server, run `python3 task_01_jinja.py`

    - You will seel something like this:
        * Running on http://127.0.0.1:5000
        * Debug mode: on

    - Click the server link to view in browser
        - http://127.0.0.1:5000
        your Home page (index.html)

        - http://127.0.0.1:5000/about
        your About page

        - http://127.0.0.1:5000/contact
        your Contact page
        
    - If all pages render properly as per the requirements, your program works!

#### For Task 2: How to read data (a list) from a JSON file and display them dynamically on a web page
    - To start the Flask server, run `python3 task_02_logic.py`
    
    - Click the server link to view in browser
    
    - If all pages render properly: return HTTP 200 responses and as per the requirements , your program works!

#### For Task 3: How to display data from JSON or CSV Files in Flask application
    - To start the Flask server, run `python3 task_03_files.py`
    
    - Click the server link to view in browser
    
    - If all pages render properly: return HTTP 200 responses and as per the requirements , your program works!

#### For Task 4: How to display data from SQLite database in Flask application
    - To start the Flask server, run `python3 task_04_db.py`
    
    - Click the server link to view in browser
    
    - If all pages render properly: return HTTP 200 responses and as per the requirements , your program works!

---

### Resources
- MDN Web Docs on Server-Side Web Development: [MDN Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side)

- Client-side vs. Server-side vs. Pre-rendering for Web Apps: [Templating Engines in Web Development](https://www.toptal.com/front-end/client-side-vs-server-side-pre-rendering)

- Flask Documentation: [Flask Official Documentation](https://flask.palletsprojects.com/en/stable/)

- Python JSON Documentation: [Python JSON Documentation](https://docs.python.org/3/library/json.html)

- Python CSV Documentation: [Python CSV Documentation](https://docs.python.org/3/library/csv.html)

- Python SQLite Documentation: [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)

- Jinja2 Documentation: [Jinja2 Documentation](https://jinja.palletsprojects.com/en/latest/)
