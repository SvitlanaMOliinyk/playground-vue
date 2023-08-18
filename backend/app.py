from flask import Flask
import logging
import sys
from flask_cors import CORS
from dotenv import load_dotenv
import requests
from routes.places import places_bp
from routes.registerRoute import register_user_bp
from routes.usersRoute import all_users_bp

app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # logs to the console
    ]
)

app.register_blueprint(places_bp)
app.register_blueprint(register_user_bp)
app.register_blueprint(all_users_bp)

CORS(app, origins="http://localhost:8080", supports_credentials=True)

if __name__ == '__main__':
    app.run()
