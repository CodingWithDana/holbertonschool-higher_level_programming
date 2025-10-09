from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask import jsonify
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

flask_app = Flask(__name__)
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

@flask_app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Basic Auth protected endpoint.

    Returns:
        JSON message confirming access granted.
    """
    return "Basic Auth: Access Granted"

if __name__ == '__main__':
    flask_app.run(debug=True)
    

# TODOLIST
    # 1. must hash password later on (werkzeug.security library)