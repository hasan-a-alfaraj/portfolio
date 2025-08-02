import os
from flask import Flask, send_from_directory, jsonify

# Initialize Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Hello world!"


# API endpoint
@app.route("/members")
def members():
    return jsonify({"members": ["Member1", "Member2", "Member3"]})


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
