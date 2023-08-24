from flask import Blueprint, jsonify, session
from models.User import User
import logging

auth_check_bp = Blueprint('auth_check', __name__)

@auth_check_bp.route('/check', methods=['GET'])
def check_auth():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)

        if user:
            logging.info(f"user after checking: {user}")
            return jsonify({
                'id': user.id,
                'name': user.name,
                'email': user.email,
            }), 200
        else:
            return jsonify({'message': 'User not found'}), 401
    else:
        return jsonify({'message': 'User not authenticated'}), 401
