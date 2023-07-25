from datetime import timedelta
from flask import Flask, render_template
from flask import request, redirect, url_for
from flask import session
from flask import flash

app = Flask(__name__)
app.secret_key = 'super secret key'
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET" :        
        name = request.args.get('name')
    elif request.method == "POST" :
        name = request.form["name"]
        session['userid'] = name
        flash("login에 성공하였습니다.")
        flash("메세지 플래슁 예제입니다")
    else:
        return "UNKNOWN METHOD"
    return render_template('index.html', name=name)

@app.route('/mypage')
def mypage():
    if "userid" in session:
        return f"hello, {session['userid']}"
    else:
        return redirect(url_for('home'))

@app.route('/redirect')
def redirect_example():
    # return redirect('/')
    return redirect(url_for('home'))

if __name__ == "__main__" :
    app.run()