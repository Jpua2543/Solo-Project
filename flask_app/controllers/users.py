from flask import render_template,session,request,redirect
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def landing():
    return render_template('landing.html')