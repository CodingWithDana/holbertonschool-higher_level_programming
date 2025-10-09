from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

flask_app = Flask(__name__)
auth = HTTPBasicAuth()

# Example: simple username/password dictionary
users = {
    "alice": "wonderland",
    "bob": "builder"
}

# Protect this route
@app.route('/secret')
@auth.login_required
def secret():
    return jsonify(message=f"Hello, {auth.current_user()}! This is a protected endpoint.")

if __name__ == '__main__':
    flask_app.run(debug=True)