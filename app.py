from flask import Flask, render_template, request, make_response, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
import os
import base64
from datetime import datetime
import sqlite3
import uuid
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)  # Required for session management
db = SQLAlchemy(app)

# Generate a secret key for Fernet encryption
SECRET_KEY = Fernet.generate_key()
cipher_suite = Fernet(SECRET_KEY)

# Define the flags
FLAGS = {
    1: "CTF{C00k13_M0nst3r}",
    2: "CTF{R0T_M4st3r_2023}",
    3: "CTF{SQL_M4st3r_2023}"
}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    completion_time = db.Column(db.Float, nullable=False)  # Time in seconds
    completed_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Create the database and tables
with app.app_context():
    db.create_all()
    # Add a test user if none exists
    if not User.query.filter_by(username='admin').first():
        test_user = User(username='admin', password='supersecret123')
        db.session.add(test_user)
        db.session.commit()

# Initialize database
def init_db():
    conn = sqlite3.connect('ctf.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attempts 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id TEXT,
                  username TEXT,
                  level INTEGER,
                  completion_time REAL,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT, email TEXT)''')
    
    # Add some sample users for level 3
    c.execute('DELETE FROM users')  # Clear existing users
    c.execute('INSERT INTO users (username, email) VALUES (?, ?)', 
             ('admin', 'admin@example.com'))
    c.execute('INSERT INTO users (username, email) VALUES (?, ?)',
             ('user1', 'user1@example.com'))
    
    # Create hidden flags table
    c.execute('''CREATE TABLE IF NOT EXISTS flags
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  flag TEXT)''')
    c.execute('DELETE FROM flags')  # Clear existing flags
    c.execute('INSERT INTO flags (flag) VALUES (?)',
             (FLAGS[3],))
    
    conn.commit()
    conn.close()

init_db()

# Generate key for level 2
FERNET_KEY = Fernet.generate_key()
fernet = Fernet(FERNET_KEY)

def get_user_id():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return session['user_id']

def record_attempt(level):
    user_id = get_user_id()
    username = session.get('username', 'Anonymous')
    if f'level{level}_start' in session:
        start_time = session[f'level{level}_start']
        completion_time = datetime.now().timestamp() - start_time
        
        conn = sqlite3.connect('ctf.db')
        c = conn.cursor()
        c.execute('INSERT INTO attempts (user_id, username, level, completion_time) VALUES (?, ?, ?, ?)',
                 (user_id, username, level, completion_time))
        conn.commit()
        conn.close()
        
        session.pop(f'level{level}_start', None)
        return completion_time
    return None

def get_leaderboard(level):
    conn = sqlite3.connect('ctf.db')
    c = conn.cursor()
    c.execute('''SELECT username, MIN(completion_time) as best_time 
                 FROM attempts 
                 WHERE level = ? 
                 GROUP BY username 
                 ORDER BY best_time ASC 
                 LIMIT 10''', (level,))
    results = c.fetchall()
    conn.close()
    
    leaderboard = []
    for i, (username, time) in enumerate(results, 1):
        medal = '🥇' if i == 1 else '🥈' if i == 2 else '🥉' if i == 3 else ''
        leaderboard.append({
            'rank': i,
            'username': username,
            'time': f"{time:.2f}s",
            'medal': medal
        })
    return leaderboard

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        
        # Validate username
        if not re.match(r'^[A-Za-z0-9_]{3,20}$', username):
            return render_template('login.html', 
                                error="Username must be 3-20 characters long and can only contain letters, numbers, and underscores")
        
        session['username'] = username
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/level1', methods=['GET', 'POST'])
def level1():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        if 'level1_start' not in session:
            session['level1_start'] = datetime.now().timestamp()
        
        resp = make_response(render_template('level1.html', username=session['username']))
        # Store the actual flag in a cookie
        resp.set_cookie('totally_not_the_flag', FLAGS[1])
        return resp
    
    if request.method == 'POST':
        submitted_flag = request.form.get('flag', '').strip()
        if submitted_flag == FLAGS[1]:
            completion_time = record_attempt(1)
            return render_template('level1.html', 
                                success=f"Congratulations! You completed Level 1 in {completion_time:.2f} seconds!", 
                                redirect=url_for('index'),
                                username=session['username'])
        else:
            return render_template('level1.html', 
                                error="Incorrect flag. Try again! Hint: Check your cookies...",
                                username=session['username'])

@app.route('/level2', methods=['GET', 'POST'])
def level2():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        if 'level2_start' not in session:
            session['level2_start'] = datetime.now().timestamp()
        
        # Create a simple message that includes the flag
        secret_message = f"The flag is: {FLAGS[2]}"
        encrypted_message = simple_encrypt(secret_message)
        return render_template('level2.html', 
                            encrypted_message=encrypted_message,
                            username=session['username'])
    
    if request.method == 'POST':
        submitted_flag = request.form.get('flag', '').strip()
        if submitted_flag == FLAGS[2]:
            completion_time = record_attempt(2)
            return render_template('level2.html', 
                                success=f"Congratulations! You completed Level 2 in {completion_time:.2f} seconds!", 
                                redirect=url_for('index'),
                                username=session['username'])
        else:
            return render_template('level2.html', 
                                error="Incorrect flag. Try again! Remember: decode base64 first, then ROT13.",
                                username=session['username'])

@app.route('/level3', methods=['GET', 'POST'])
def level3():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        if 'level3_start' not in session:
            session['level3_start'] = datetime.now().timestamp()
        return render_template('level3.html', username=session['username'])
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'search':
            search_term = request.form.get('search', '')
            conn = sqlite3.connect('ctf.db')
            c = conn.cursor()
            try:
                # Intentionally vulnerable to SQL injection
                query = f"SELECT username, email FROM users WHERE username LIKE '%{search_term}%'"
                c.execute(query)
                results = c.fetchall()
                return render_template('level3.html', 
                                    username=session['username'],
                                    results=results)
            except Exception as e:
                return render_template('level3.html',
                                    username=session['username'],
                                    error=str(e))
            finally:
                conn.close()
        
        elif action == 'submit_flag':
            submitted_flag = request.form.get('flag', '').strip()
            if submitted_flag == FLAGS[3]:
                completion_time = record_attempt(3)
                return render_template('level3.html',
                                    success=f"Congratulations! You completed Level 3 in {completion_time:.2f} seconds!",
                                    redirect=url_for('index'),
                                    username=session['username'])
            else:
                return render_template('level3.html',
                                    error="Incorrect flag. Keep trying!",
                                    username=session['username'])
    
    return render_template('level3.html', username=session['username'])

@app.route('/leaderboard')
def leaderboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    level = request.args.get('level', 1, type=int)
    if level not in [1, 2, 3]:
        level = 1
    
    leaderboard_data = get_leaderboard(level)
    
    return render_template('leaderboard.html',
                         username=session['username'],
                         current_level=level,
                         leaderboard=leaderboard_data)

def simple_encrypt(text):
    # First apply ROT13
    rot13 = text.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    ))
    # Then apply base64
    return base64.b64encode(rot13.encode()).decode()

if __name__ == '__main__':
    # Initialize the database before starting
    init_db()
    app.run(host='localhost', port=8080, debug=True) 