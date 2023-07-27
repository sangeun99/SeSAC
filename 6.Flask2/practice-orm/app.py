import datetime
import uuid
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "test_session"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 직접 커밋해야 객체와 DB가 동기화됨

db = SQLAlchemy(app)

def datetime_sqlalchemy(value):
    return datetime.datetime.strptime(value, '%Y-%m-%d')

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    birthdate = db.Column(db.DateTime())
    address = db.Column(db.String(100))

    def __init__(self, id, password, name, gender, birthdate, address):
        self.id = id
        self.password = password
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.address = address

@app.route("/")
def main():
    if 'username' in session:
        username = session['username']
        return f'Hello. {username}! You are logged in.'
    return render_template('index.html')

@app.route("/view")
def view():
    return render_template('view.html', values=User.query.all())
# User.query.all()는 select * from User 역할

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login() :
    status = 0
    if request.method == "POST" :

        id = request.form['id']
        password = request.form['password']
        name = request.form['name']
        gender = request.form['gender']
        birthdate = datetime_sqlalchemy(request.form['birthdate'])
        address = request.form['address']

        user = User(id, password, name, gender, birthdate, address)
        db.session.add(user)
        db.session.commit()
        flash("User Created")
        session['user'] = id
    

        # # 
        # username = 
        # password = request.form['password']
        
        # found_user = User.query.filter_by(name=username).first() # select query limit 1과 같은 역할
        # if (found_user) :
        #     flash('Login Successful')
        # else :
        #     user = User(username, password, "")
        #     db.session.add(user)
        #     db.session.commit()
        #     flash("User Created")
        # session['user'] = username
        # return redirect(url_for('main'))

    return render_template('login.html', status=status)

@app.route('/logout')
def logout() :
    session.pop('username', None)
    flash("Logout success!")

    return render_template('logout.html')
    

@app.route('/delete', methods=['POST'])
def delete():
    user = session['username']
    if request.method == 'POST' :
        action = request.form["action"]
        if action == "DELETE":
            User.query.filter_by(name=user).delete()
            db.session.commit()
            return redirect(url_for('logout'))


if __name__ == "__main__" :
    with app.app_context():
        db.create_all()
    app.run(debug=True)
