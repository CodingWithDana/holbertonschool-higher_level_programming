from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

flask_app = Flask(__name__)
auth = HTTPBasicAuth()

# Example: simple username/password dictionary
users = {
    "alice": "wonderland",
    "bob": "builder"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username  # returning something truthy means "authenticated"
    return None

@flask_app.route('/')
def index():
    return "Public endpoint — no login needed."

# Protect this route
@flask_app.route('/login')
@auth.login_required
def secret():
    return jsonify(message=f"Hello, {auth.current_user()}! This is a protected endpoint.")

if __name__ == '__main__':
    flask_app.run(debug=True)
    

# TODOLIST
    # 1. must hash password later on (werkzeug.security library)