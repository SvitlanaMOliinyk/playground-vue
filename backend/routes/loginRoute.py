from flask import Blueprint, request, session, jsonify
from models.User import User
import logging

login_user_bp = Blueprint('login_user', __name__)
profile_bp = Blueprint('profile', __name__)
logout_user_bp = Blueprint('logout_user', __name__)

@login_user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        logging.info(f"user password and email: {email, password}")

        user = User.query.filter_by(email=email).first()
        logging.info(f"user password: {user}")
        if user and user.check_password(password):
            session['user_id'] = user.id
            return jsonify({"message": "User authenticated",
                             "user_id": user.id,
                             "user_name": user.name}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    except Exception as e:
        logging.error(f"Error processing login request: {e}")
        return jsonify({"error": "Failed to process login request"}), 500
    
@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        return jsonify({"user_id": user.id, "name": user.name, "email": user.email})
    else:
        return jsonify({"message": "Not authenticated"}), 401
    
@logout_user_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out"}), 200