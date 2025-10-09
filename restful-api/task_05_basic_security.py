from flask import Flask
from flask_httpauth import HTTPBasicAuth

flask_app = Flask(__name__)
auth = HTTPBasicAuth()

# Example: simple username/password dictionary
users = {
    "alice": "wonderland",
    "bob": "builder"
}

@flask_app.route('/')
def index():
    return "Public endpoint — no login needed."

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