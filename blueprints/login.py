from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from extensions import *
import bcrypt

user_login = Blueprint('login', __name__, url_prefix="/")

@user_login.route('/')
def index():
    if 'username' in session:
        return render_template('/home_index.html')
    
    return render_template('/logins/login_index.html')

@user_login.route('/signin', methods=['POST'])
def login():
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('login.index'))
    flash('Invalid username/password combination')
    return render_template('logins/login_index.html')
    

@user_login.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name' : request.form['username'], 'password' : hashpass })
            session['username'] = request.form['username']
            return redirect(url_for('login.index'))
        
        flash('That username already exists!')
        return render_template('logins/login_register.html')
    
    return render_template('/logins/login_register.html')

@user_login.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.index'))