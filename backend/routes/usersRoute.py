from flask import Blueprint
from models.User import User

all_users_bp = Blueprint('all_users', __name__)

@all_users_bp.route('/users', methods=['GET'])
def get_users_names():
    try:
        users = User.query.all()
        users_names = [user.name for user in users]
        print(users_names)
        return {"users_names": users_names}
    except Exception as e:
        print(f"Error retrieving user names: {e}")
        return {"error": "Failed to retrieve user names"}, 500