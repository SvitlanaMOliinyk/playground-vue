from flask import Flask, Blueprint
from db import init_db_and_tables
import logging
import sys
from flask_cors import CORS

from routes.places import places_bp
from routes.registerRoute import register_user_bp
from routes.usersRoute import all_users_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # logs to the console
    ]
)

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return "Hello, World!"

app.register_blueprint(home_bp)
app.register_blueprint(places_bp)
app.register_blueprint(register_user_bp)
app.register_blueprint(all_users_bp)

CORS(app, origins="http://localhost:8080", supports_credentials=True)

init_db_and_tables(app)

if __name__ == '__main__': 
    app.run()
