# from flask import Blueprint, request, jsonify
# from flask_login import login_user, login_required, logout_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from db import db
# from models import User

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/register', methods=['POST'])
# def register():
#     data = request.json
#     if User.query.filter_by(username=data.get('username')).first():
#         return jsonify({'error': 'Username already exists'}), 400

#     new_user = User(username=data.get('username'), password_hash=generate_password_hash(data.get('password')))
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'message': 'User registered successfully'}), 201

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     user = User.query.filter_by(username=data.get('username')).first()

#     if user and check_password_hash(user.password_hash, data.get('password')):
#         login_user(user)
#         return jsonify({'message': 'Login successful'}), 200
    
#     return jsonify({'error': 'Invalid credentials'}), 401

# @auth_bp.route('/logout', methods=['POST'])
# @login_required
# def logout():
#     logout_user()
#     return jsonify({'message': 'Logout successful'}), 200