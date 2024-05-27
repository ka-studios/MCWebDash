from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import subprocess

app = Flask(__name__)
app.secret_key = 'example' # replace this pls
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/start', methods=['POST'])
def start():
    if 'username' not in session:
        return render_template('401.html'), 401

    try:
        output = subprocess.check_output(['java', '-jar', '/root/newlobby/server/server.jar'], text=True)
        return jsonify({'output': output})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stop', methods=['POST'])
def stop():
    if 'username' not in session:
        return render_template('401.html'), 401

    try:
        output = subprocess.check_output(['fuser', '-k', '95/tcp', '95/udp'], text=True)
        return jsonify({'output': output})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start_lifesteal', methods=['POST'])
def start_lifesteal():
    if 'username' not in session:
        return render_template('401.html'), 401

    try:
        output = subprocess.check_output(['java', '-jar', '/root/anarchy/server/server.jar'], text=True)
        return jsonify({'output': output})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stop_lifesteal', methods=['POST'])
def stop_lifesteal():
    if 'username' not in session:
        return render_template('401.html'), 401

    try:
        output = subprocess.check_output(['fuser', '-k', '1/tcp', '1/udp'], text=True)
        return jsonify({'output': output})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start_skyblock', methods=['POST'])
def start_skyblock():
    if 'username' not in session:
        return render_template('401.html'), 401

    try:
        output = subprocess.check_output(['java', '-jar', '/root/skyblock/server/server.jar'], text=True)
        return jsonify({'output': output})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stop_skyblock', methods=['POST'])
def stop_skyblock():
    if 'username' not in session:
        return render_template('401.html'), 401

    try:
        output = subprocess.check_output(['fuser', '-k', '97/tcp', '97/udp'], text=True)
        return jsonify({'output': output})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start_pvp', methods=['POST'])
def start_pvp():
    if 'username' not in session:
        return render_template('401.html'), 401

    try:
        output = subprocess.check_output(['java', '-jar', '/root/mc/server/server.jar'], text=True)
        return jsonify({'output': output})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stop_pvp', methods=['POST'])
def stop_pvp():
    if 'username' not in session:
        return render_template('401.html'), 401

    try:
        output = subprocess.check_output(['fuser', '-k', '25565/tcp', '25565/udp'], text=True)
        return jsonify({'output': output})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(401)
def unauthorized(e):
    return render_template('401.html'), 401

if __name__ == '__main__':
    app.run(debug=True)
