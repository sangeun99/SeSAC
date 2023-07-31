from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import json

app = Flask(__name__)

app.secret_key = 'secret-key'

# DB 초기화
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sessions.db"
db = SQLAlchemy(app)

# 세션 확장도구 설정
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
Session(app)

class SessionData(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    data = db.Column(db.Text)

def session_store(sid, data):
    session_data = SessionData.query.get(sid)
    if not session_data:
        session_data = SessionData(id=sid)
    session_data.data = json.dumps(data)
    db.session.add(session_data)
    db.session.commit()

def get_session_data(sid):
    session_data = SessionData.query.get(sid)
    if session_data:
        return json.loads(session_data.data)
    return {}

@app.route('/')
def main() :
    session['username'] = 'user'
    session['data'] = '1234'

    # 숫자 데이터 저장
    session['count'] = 42

    # 리스트 데이터 저장
    session['my_list'] = [1, 2, 3, 4]

    # 세션 데이터 저장
    session_store(session.sid, dict(session))

    return 'Hello'

@app.route('/get_session')
def get_session():
    username = session.get('username')
    data = session.get('data')

    stored_session_data = get_session_data(session.sid)
    print(stored_session_data)

    stored_session_data_str = json.dumps(stored_session_data, indent=4)

    return f"username: {username}, {data}, my-data: {stored_session_data_str}"

if __name__ == "__main__" :
    with app.app_context():
        db.create_all()
    app.run(debug=True)