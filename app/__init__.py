from flask import Flask
from flask_cors import CORS
import os, subprocess, logging

def create_app():
    create_model()
    app = Flask(__name__)
    CORS(app)  # Add this line to enable CORS for all origins
    with app.app_context():
        from . import routes
        return app
def create_model():
    current_dir = os.path.dirname(os.path.abspath(__file__)) #redirect to /app
    target_dir = os.path.dirname(current_dir) #to /models
    model_path = target_dir+"\\models\\model-train.py"
    result = subprocess.run(
            ['python', model_path],
            check=True,
            capture_output=True,
            text=True
        )
    output = result.stdout.strip()
    print(output)