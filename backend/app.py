from flask import Flask, Blueprint
from db import init_db_and_tables
import logging
import sys
from flask_cors import CORS
import os
from dotenv import load_dotenv


from routes.places import places_bp
from routes.registerRoute import register_user_bp
from routes.usersRoute import all_users_bp
from routes.loginRoute import login_user_bp
from routes.loginRoute import logout_user_bp
from routes.authCheckRoute import auth_check_bp

load_dotenv()
app = Flask(__name__)
secret_key = os.environ.get('FLASK_SECRET_KEY')

if secret_key is None:
    raise ValueError("FLASK_SECRET_KEY environment variable is not set")

app.config['SECRET_KEY'] = secret_key
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
app.register_blueprint(login_user_bp)
app.register_blueprint(logout_user_bp)
app.register_blueprint(auth_check_bp)

CORS(app, origins="http://localhost:8080", supports_credentials=True)

init_db_and_tables(app)

if __name__ == '__main__': 
    app.run()
