from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy

"""
LoginManager: 로그인 관리를 담당하는 클래스로, Flask 애플리케이션에서 로그인 기능을 초기화하고 관리하는 역할을 합니다.
UserMixin: UserMixin 클래스는 Flask-Login이 기본적으로 사용하는 사용자 모델 클래스를 정의하기 위해 사용됩니다. 이 클래스를 사용하여 사용자 모델 클래스에 필요한 메서드들을 간단하게 추가할 수 있습니다.
login_user: 로그인 처리를 위해 사용되는 함수로, 인증이 성공적으로 완료된 사용자를 로그인 상태로 만듭니다. 이 함수를 호출하면 세션에 사용자 정보가 저장되어 사용자를 인증된 상태로 유지할 수 있습니다.
login_required: 데코레이터로, 특정 뷰 함수를 보호하는 데 사용됩니다. 이 데코레이터가 적용된 뷰 함수는 로그인된 사용자만 접근할 수 있으며, 로그인되지 않은 사용자는 로그인 페이지로 리디렉션됩니다.
logout_user: 로그아웃 처리를 위해 사용되는 함수로, 현재 로그인된 사용자를 로그아웃 상태로 만듭니다. 세션에서 사용자 정보를 삭제하여 인증을 끝내는 역할을 합니다.
current_user: 현재 로그인된 사용자를 나타내는 객체입니다. 로그인되지 않은 경우 AnonymousUserMixin 객체가 반환됩니다. 이를 통해 로그인된 사용자의 정보를 뷰 함수에서 간단하게 접근할 수 있습니다.
"""

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # password_hash = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80))

    def set_password(self, password):
        # self.password_hash = generate_password_hash(password)
        self.password = password

    def check_password(self, password):
        # return check_password_hash(self.password_hash, password)
        return self.password == password

    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.password}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def main() :
    return render_template('main.html', current_user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login() :
    # 1. form으로부터 id/pw 받아온다
    # 2. form의 정보가 맞는지 db와 대조
    # 3. 성공했다면 로그인 정보를 저장하고 로그인한 페이지로 이동한다
    #    실패했다면 오류를 알려준다
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        result = User.query.filter(User.username==username).first()
        if result and result.check_password(password):
            login_user(result)
        else :
            flash('로그인에 실패하였습니다.')
    return redirect(url_for('main'))

@app.route('/logout')
@login_required
def logout() :
    logout_user()
    return redirect(url_for('main'))

@app.route('/profile_edit', methods=['GET', 'POST'])
@login_required
def profile_edit():
    # 미션 : 프로필 수정 기능 구현
    # 1. form을 통해서 수정할 정보를 가져온다. (password를 받아온다)
    # 2. 저장할 장소(즉, 현재 사용자)를 가져온다. (current_user를 통해 접근 가능)
    # 3. 받아온 정보를 db에 저장한다.
    if request.method == 'POST' :
        password = request.form['password']
        current_user.set_password(password)
        db.session.commit()
        flash('비밀번호가 변경되었습니다.')
        return redirect(url_for('main'))
    return render_template('profile_edit.html', current_user=current_user)

# 신규 사용자 생성
@app.route('/register', methods=['GET', 'POST'])
def register():
    # 1. 회원가입 폼을 만든다
    # 2. 회원가입 정보를 저장한다
    # 3. DB에 저장한다
    logout_user()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        try :
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash("회원가입이 완료되었습니다")
        except sqlalchemy.exc.IntegrityError :
            flash("아이디가 중복되었습니다. 다시 가입해주세요")
            return render_template('register.html')
        return redirect(url_for('main'))
    return render_template('register.html')

@app.route('/delete')
@login_required
def delete():
    db.session.delete(current_user)
    db.session.commit()
    flash('회원탈퇴가 완료되었습니다')
    return redirect(url_for('main'))

@app.route('/users/')
@login_required
def users():
    # 사용자 정보를 모두 조회한다
    users = User.query.all()
    return render_template('user.html', users=users)

if __name__ == "__main__" :
    with app.app_context():
        db.create_all()
    app.run(debug=True)