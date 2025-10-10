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

# Initialise the Flask application
app = Flask(__name__)

# Create a Basic Authentication object
auth = HTTPBasicAuth()

# A dict of Users and their hashed passwords (User Data: in-memory)
users = {
    # Admin user
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    },
    # Regular user
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    }
}

# ====================
# BASIC AUTHENTICATION SETUP
# ====================
# Verify username and password for Basic Auth
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if (
        user and
        check_password_hash(user['password'], password)
    ):
        return username
    return None

    # # check if username exists in the users dictionary
    # if username in users:
    #     return None

    # # get the hashed password for this user
    # hashed_password = users[username]["password"]
    # # verify the user's provided password against the hashed password
    # if not check_password_hash(hashed_password, password):
    #     return None

    # return username

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
    return "Basic Auth: Access Granted"


# ================
# JWT SETUP
# ================
# Secret key for signing JWTs (replace in production)
app.config["JWT_SECRET_KEY"] = "SuPEr-SEcREt05"
# Initialise JWT Manager
jwt = JWTManager(app)

# Login route to generate JWT tokens
@app.route('/login', methods=['POST'])
def login():
    # Get JSON data from request body
    username = request.json.get("username")
    password = request.json.get("password")
    user = users.get(username)
    
    # Verify username and password
    if username in users:
        # if username exists, then retrieve the hashed password for the given username
        hashed_password = users[username]["password"]
        
        # compare the provided password with the hashed password
        if check_password_hash(hashed_password, password):
            # if password is correct, retrieve the user's role
            user_role = users[username]["role"]
            
            # create a JWT token with username and role as identity
            access_token = create_access_token(identity={"username": username, "role": user_role})
            
            # return the JWT token as JSON
            return jsonify(access_token=access_token)
        else:
            # if password is incorrect
            return jsonify({"error": "Invalid credentials"}), 401
    else:
        # if username does not exist
        return jsonify({"error": "Invalid credentials"}), 401
    
# JWT Protected Route
@app.route('/jwt-protected', methods=['GET'])
# Only accessible with a valid JWT token
@jwt_required()
def jwt_protected():
    # Get user info from JWT
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"

# Role-based Protected Route
@app.route('/admin-only', methods=['GET'])
# Only accessible with a valid JWT token
@jwt_required()
# Must have a valid JWT
def admin_only():
    # Get current user info
    current_user = get_jwt_identity()
    # Check if user role is admin
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__=='__main__':
    # run Flask app in debugg mode
    app.run(debug=True)
