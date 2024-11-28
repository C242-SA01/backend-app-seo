from datetime import datetime, timezone
import bcrypt
from flask import Blueprint, request, jsonify
from firebase import db

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {
        'email': email,
        'password': hashed_password.decode('utf-8'),
        'created_at': datetime.now(timezone.utc)
    }

    db.collection('users').add(user_data)
    return jsonify({'message': 'User created successfully'}), 201
