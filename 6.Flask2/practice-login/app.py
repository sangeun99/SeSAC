from datetime import timedelta
from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

app.secret_key = "test_session"
app.permanent_session_lifetime = timedelta(minutes=1)

# 가상의 사용자 테이블
users = {
    "user1" : {"password" : "password123"},
    "user2" : {"password" : "password456"}
}

@app.route("/")
def main():
    if 'username' in session:
        username = session['username']
        return f'Hello. {username}! You are logged in.'
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login() :
    status = 0
    if request.method == "POST" :
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username]['password'] == password:
            session['username'] = username
            flash("Login success!")
            status = 1
        else :
            flash("Invalid username or password. Please try again")
            status = -1
    return render_template('login.html', status=status)

@app.route('/logout')
def logout() :
    session.pop('username', None)
    flash("Logout success!")

    return render_template('logout.html')
    
if __name__ == "__main__" :
    app.run(debug=True)

# 미션1. render_template 통해서 첫 화면에 login/logout 추가
# 미션2. 로그인 성공실패여부를 flash 메세지 통해서 처리
# 미션3. 디자인 적용해서 flash 메세지 색상 다르게 해보기. (성공 시 초록, 실패 시 빨강)