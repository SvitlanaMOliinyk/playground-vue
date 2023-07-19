from flask import Flask
import logging
import sys
from flask_cors import CORS
from dotenv import load_dotenv
import requests
from routes.places import places_bp

app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,  # Set the desired log level
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # Output logs to the console
    ]
)

app.register_blueprint(places_bp)

CORS(app)

if __name__ == '__main__':
    app.run()