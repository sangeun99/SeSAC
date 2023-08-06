from flask import Flask, render_template, request, jsonify, redirect
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/create', methods=['post'])
def create():
    title = request.form['title']
    message = request.form['message']
    sql = "INSERT INTO board(title, message) VALUES (?, ?)"
    db.execute(sql, (title, message))
    db.commit()
    return "ok"

@app.route('/delete', methods=['post'])
def delete():
    id = request.form['id']
    sql = "DELETE FROM board WHERE id=?"
    db.execute(sql, (id, ))
    db.commit()
    return "ok"

@app.route('/update', methods=['post'])
def update():
    id = request.form['id']
    title = request.form['title']
    message = request.form['message']
    sql = "UPDATE board SET title=?, message=? WHERE id=?"
    db.execute(sql, (title, message, id))
    db.commit()
    return "ok"

@app.route('/list', methods=['get'])
def list():
    sql = "SELECT * FROM board"
    result = db.execute_fetch(sql)
    tuple_keys = ('id', 'title', 'message')
    dict_list = []
    for r in result:
        dict_value = dict(zip(tuple_keys, r))
        dict_list.append(dict_value)
    return jsonify(dict_list)

if __name__ == "__main__" :
    app.run(debug=True)