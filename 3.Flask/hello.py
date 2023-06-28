from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello sesac from flask</h1>
    <p>welcome to flask</p>
    <a href="/user">connect to user page!</a>
    """

@app.route('/user')
def user_none():
    return """
    This is user page
    <a href="/">connect to home!</a>
    <ul>
    <li><a href="/user/Tom">tom's page</a></li>
    <li><a href="/user/Peter">peter's page</a></li>
    <li><a href="/user/Emily">emily's page</a></li>
    <li><a href="/user/Lucy">lucy's page</a></li>
    </ul>
    """

@app.route('/user/<name>')
def user(name):
    return f"""
    <h1>This is {name}'s page</h1>
    <a href="/">connect to home!</a> <br />
    <a href="/user">connect to user page!</a>

    """

@app.route('/admin')
def admin():
    return redirect(url_for('user', name="admin"))

if __name__ =="__main__" :
    app.run(debug=True, port=7000) # 5000번이 기본값