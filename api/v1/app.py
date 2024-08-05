#!/usr/bin/python3
"""Flask application entry point"""

import os
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

# Declare environmental variables
HOST = os.getenv('HBNB_API_HOST', '0.0.0.0')
PORT = os.getenv('HBNB_API_PORT', 5000)

# Create an instance of flask
app = Flask(__name__)

# Initiate CORS
CORS(app, origins='0.0.0.0')

# Register the blueprint `app_views` to app
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(error):
    """Close DB session"""
    storage.close()


@app.errorhandler(404)
def e_not_found(error):
    '''
    return JSON formatted 404 status code response
    '''
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    """Run Flask app"""
    app.run(host=HOST, port=PORT, debug=True)
