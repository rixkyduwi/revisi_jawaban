import os
from flask import Flask,jsonify,request
from flask_httpauth import HTTPTokenAuth
import random
import string
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "login.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
auth = HTTPTokenAuth(scheme='Bearer')
class login(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    keterangan = db.Column(db.String(100))
    token = db.Column(db.String(225), unique=True, nullable=True, primary_key=False)
# nama kelompok 
# rizky dwi saputra (6A) 
# moh saefudin fikri (6B) 
@app.route("/api/v1/login", methods=["POST"])
def login_user():
    username= request.form['username']
    password= request.form['password']
    S=10
    user=login.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        access_token = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        user.token= access_token
        db.session.commit()
    return jsonify({
        "msg": "Succes Signin",
        "status": 200,
        "token": access_token,
    })
@auth.verify_token
def verify_token(token):
    user=login.query.filter_by(token=token).first() 
    return user.keterangan 
@app.route('/api/v2/users/info')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())
if __name__ == '__main__':
    app.run(debug = True, port=4000)
