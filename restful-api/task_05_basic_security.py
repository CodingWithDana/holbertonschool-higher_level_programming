from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager

flask_app = Flask(__name__)
jwt = JWTManager(flask_app)
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


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401
    
if __name__ == '__main__':
    flask_app.run(debug=True)
    

# TODOLIST
    # 1. must hash password later on (werkzeug.security library)