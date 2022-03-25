# curl -H "Authorization: Bearer secret-token-1" http://127.0.0.1:7001/
import os
from flask import Flask,jsonify,request
from flask_httpauth import HTTPTokenAuth
import random
import string
from flask_httpauth import HTTPTokenAuth
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
  # request sesuai spec sbg data body bukan parameter lihat contoh book_ws.db
    username= request.form['username']
    password= request.form['password']
    S=10
    user=login.query.filter_by(username=username).first()
  # pada def create line 50 dan parsingnya line 51
  # cari kedalam db user username dan passwordusername=login.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        
  # jika ketemu maka update kolom token ybs dengen random string
  
        access_token = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        user.token= access_token
        db.session.commit()
  # response kan sbb
  # body {"token": "randomsetringnyaaahh"}, http code: 200
    return jsonify({
        "msg": "Succes Signin",
        "status": 200,
        "data": access_token,
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
    app.run( debug = True, port=4000)
