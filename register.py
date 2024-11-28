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

    if not email or not password:
        return jsonify({'error': 'Email or password are required'}), 400

    users_ref = db.collection('users')
    query = users_ref.where('email', '==', email).stream()

    user_exists = False
    for user in query:
        user_exists = True
        break

    if user_exists:
        return jsonify({'error': 'User with this email already exists'}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {
        'email': email,
        'password': hashed_password.decode('utf-8'),
        'created_at': datetime.now(timezone.utc)
    }

    db.collection('users').add(user_data)
    return jsonify({'message': 'User created successfully'}), 201