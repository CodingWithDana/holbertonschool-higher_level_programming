from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask import jsonify
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for HTTP Basic Auth.

    Args:
        username (str): Username provided by client.
        password (str): Password provided by client.

    Returns:
        str or None: Username if valid credentials, else None.
    """
    user = users.get(username)
    if (
        user and
        check_password_hash(user['password'], password)
    ):
        return username
    return None

@auth.error_handler
def auth_error():
    return jsonify({"error": "Unauthorized access"}), 401

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Basic Auth protected endpoint.

    Returns:
        JSON message confirming access granted.
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and provide JWT access token.

    Expects JSON body with 'username' and 'password'.

    Returns:
        JSON with access_token if credentials valid,
        or JSON error with 401 status otherwise.
    """
    username = request.json.get("username")
    password = request.json.get("password")
    user = users.get(username)
    if username not in users or not (
        check_password_hash(user["password"], password)
    ):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity={'username': username,
                                                 'role': user['role']})
    return jsonify(access_token=access_token)

if __name__ == '__main__':
    app.run(debug=True)
    

# TODOLIST
    # 1. must hash password later on (werkzeug.security library)