# Flask framework and helpers for JSON responses and handling requests
from flask import Flask
from flask import jsonify
from flask import request
# For Basic HTTP Authentication
from flask_httpauth import HTTPBasicAuth
# For hashing and verifying passwords
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
# JWT handling for authentication
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager

# Initialize the Flask application
app = Flask(__name__)

# Create a Basic Authentication object
auth = HTTPBasicAuth()

# Secret key for signing JWTs (replace in production)
app.config["JWT_SECRET_KEY"] = "SuPEr-SEcREt05"
# Initialise JWT Manager
jwt = JWTManager(app)

# A dict of Users and their hashed passwords (User Data: in-memory)
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


# Verify username and password for Basic Auth
@auth.verify_password
def verify_password(username, password):
    #Verify user credentials for HTTP Basic Auth.
    user = users.get(username)
    if (
        user and
        check_password_hash(user['password'], password)
    ):
        return username
    return None


# Custom error handler for missing/invalid credentials
@auth.error_handler
def auth_error():
    # Return 401 response for missing/invalid Basic Auth
    return jsonify({"error": "Unauthorized access"}), 401


# Protect routes using Basic Auth
@app.route('/basic-protected', methods=['GET'])
# Only accessible if passed the Basic Authentication
@auth.login_required
def basic_protected():
    #Basic Auth protected endpoint.
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    # Get JSON data from request body
    username = request.json.get("username")
    password = request.json.get("password")
    user = users.get(username)
    
    # Verify username and password
    if username not in users or not (
        check_password_hash(user["password"], password)
    ):
        return jsonify({"error": "Invalid credentials"}), 401
    # create a JWT token with username and role as identity
    access_token = create_access_token(identity={'username': username,
                                                 'role': user['role']})
    # return the JWT token as JSON
    return jsonify(access_token=access_token)


# JWT Protected Route
@app.route('/jwt-protected', methods=['GET'])
# Only accessible with a valid JWT token
@jwt_required()
def jwt_protected():
    # JWT protected endpoint
    return "JWT Auth: Access Granted"


# Role-based Protected Route
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    # Admin-only endpoint.
    identity = get_jwt_identity()
    # Check if user role is admin
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    # Handler for missing or unauthorized JWT token
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    # Handler for invalid JWT token
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    # Handler for expired JWT token
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    # Handler for revoked JWT token
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    # Handler for fresh JWT token required
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    # run Flask app in debugg mode
    app.run()