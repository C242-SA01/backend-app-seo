from datetime import datetime, timezone
import bcrypt
from flask import Blueprint, request, jsonify
from firebase import db

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 200
    
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    if not first_name or not last_name or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    users_ref = db.collection('users')
    query = users_ref.where('email', '==', email).stream()

    user_exists = any(query)

    if user_exists:
        return jsonify({'error': 'User with this email already exists'}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': hashed_password.decode('utf-8'),
        'created_at': datetime.now(timezone.utc)
    }

    db.collection('users').add(user_data)
    return jsonify({'message': 'User created successfully'}), 201