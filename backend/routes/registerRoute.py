from flask import Blueprint, request, jsonify
from db import db
from models.User import User
import logging



register_user_bp = Blueprint('register_user', __name__)

@register_user_bp.route('/register', methods=['POST'])
def create_user():
        try:
            data = request.json 
            userName = data.get("name")
            password = data.get("password")
            email = data.get("email")
            logging.debug(f"userName: {userName}, password: {password}, email: {email}")
        
            new_user = User(name=userName, email=email, favorite_places=None)
            new_user.set_password(password)
        
            db.session.add(new_user)
            db.session.commit()
            print(f"New user created: {new_user}")
            response_data = {"success": True}
            return jsonify(response_data), 200 
        except Exception as e:
            logging.error(f"Error processing request: {e}")
            return jsonify({"error": "Failed to process request"}), 500

