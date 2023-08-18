from flask import Blueprint, request
from .registerRoute import users


print("Imported users from register module:", users)
all_users_bp = Blueprint('all_users', __name__)

@all_users_bp.route('/users', methods=['GET'])
def get_users_names():
    print(users)
    users_names = []
    for user in users:
            users_names.append(user["name"])
    print(users_names)
    return {"users_names": users_names}

