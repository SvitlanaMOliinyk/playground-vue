from flask import Blueprint, request, jsonify
import logging


users = []

register_user_bp = Blueprint('register_user', __name__)

@register_user_bp.route('/register', methods=['POST'])
def create_user():
        try:
            data = request.json 
            userName = data.get("name")
            password = data.get("password")
            email = data.get("email")
            logging.debug(f"userName: {userName}, password: {password}, email: {email}")
        
            newUser = {
            "name": userName,
            "password": password,
            "email": email
            }
            logging.debug(f" newUser: { newUser}")
            users.append(newUser)
            print("Updated users list:", users)
            response_data = {"success": True}
            return jsonify(response_data), 200 
        except Exception as e:
            logging.error(f"Error processing request: {e}")
            return jsonify({"error": "Failed to process request"}), 500

