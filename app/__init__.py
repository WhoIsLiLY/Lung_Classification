from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Add this line to enable CORS for all origins
    
    with app.app_context():
        from . import routes
        return app