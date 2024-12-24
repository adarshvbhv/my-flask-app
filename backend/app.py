
from models import db, User  # Ensure User is imported from models.py
from flask import Flask, request, jsonify, send_from_directory, redirect, url_for, render_template, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from video_downloader import run_downloader
from youtube_uploader import Y_uploader_run
from file_eraser import delete_all_files_and_folders
import os

app = Flask(__name__, static_folder='../frontend', template_folder= '../frontend', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database URI
app.config['SECRET_KEY'] = os.urandom(24)  # Change this to a random secret key

db.init_app(app)  
CORS(app)



# db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
# @login_required  # Ensure the user is logged in

def index():
    
    if(current_user.is_authenticated):
        return send_from_directory('../frontend', 'index2.html')
    return send_from_directory('../frontend', 'index.html')

# @app.route('/login')
# def login():
#     return send_from_directory('../frontend', 'login.html')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('../frontend', path)

@app.route('/download', methods=['POST'])
@login_required  # Ensure the user is logged in
def download():
    delete_all_files_and_folders(current_user.username)
    data = request.json
    n = data.get('count')
    urls = data.get('urls')

    if not n or not urls:
        return jsonify({'error': 'Count and URLs are required'}), 400
    
    # Run the downloader
    run_downloader(urls, current_user.username)  
    return jsonify({'message': 'Download completed'}), 200

@app.route('/upload', methods=['POST'])
@login_required  # Ensure the user is logged in
def upload():
    # Run the upload process
    Y_uploader_run(current_user.username)
    return jsonify({'message': 'Upload completed'}), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username_ = request.form['username']
        password = request.form['password']
        print(username_)
        print(password)
        # hashed_password = generate_password_hash(password, method='sha256')
        if User.query.filter_by(username = username_).first():
            return jsonify({'error': 'Username already exists'}), 400
        new_user = User(username=username_)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)