import os
from flask import Flask
from models import storage
from api.v1.views import app_views

# Declare environmental variables
HOST = os.getenv('HBNB_API_HOST', '0.0.0.0')
PORT = os.getenv('HBNB_API_PORT', 5000)

# Create an instance of flask
app = Flask(__name__)

# Register the blueprint `app_views` to app
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_storage(error):
    """Close DB session"""
    storage.close()

if __name__ == "__main__":
    """Run Flask app"""
    app.run(host=HOST, port=PORT, debug=True)