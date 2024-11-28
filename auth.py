import bcrypt
import jwt
import datetime
from flask import Blueprint, request, jsonify
from firebase import get_user_by_email

auth_blueprint = Blueprint('auth', __name__)
SECRET_KEY = "YOUR_SECRET_KEY"

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = get_user_by_email(email)
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        token = jwt.encode({
            'email': user['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401
