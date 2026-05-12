import os
from flask import Flask, jsonify

#Create Flask app instance
app = Flask(__name__)

# DB_HOST = os.environ.get('DB_HOST', 'localhost')
# DB_USER = os.environ.get('DB_USER', 'postgres')

#Run function when /health endpoint is accessed
@app.route('/health')
# Function to check endpoint health and return JSON response
def health_check():
    return jsonify({"status": "healthy"}), 200

# TODO: Add REST endpoints to connect to the database & return mock JSON data
# @app.route('/api/transactions')
# def get_transactions():
#     pass
