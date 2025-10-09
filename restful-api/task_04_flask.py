from flask import Flask, jsonify, request


# instantiate a Flask web server from the Flask module
app = Flask(__name__)

# in memory data storage
users = {}

@app.route("/")
def home():
    # root route
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    # status endpoint
    return "OK"

@app.route("/data")
def get_all_users():
    # return a list of all usernames
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    # return full user data related to a provided username
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # add a new user through POST
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()
