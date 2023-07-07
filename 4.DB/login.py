import sqlite3
import hashlib

conn = sqlite3.connect('hello.db')
cursor = conn.cursor()

def cleanup_table():
    pass

def insert_users():
    pass

def hash_password(pw):
    hash_object = hashlib.sha256(pw.encode())
    return hash_object.hexdigest()

def get_input():   
    username = input('아이디를 입력하세요 : ')
    password = input('비밀번호를 입력하세요 : ')
    return username, password

def get_id_input():
    id = input('아이디를 입력하세요 : ')
    return id

def get_pw_input():
    pw = input('비밀번호를 입력하세요 : ')
    return pw

def is_exist(id):
    cursor.execute("SELECT * FROM users WHERE username = ?", [id])
    result = cursor.fetchall()
    if (result) :
        return True
    return False

def signup():
    while True:
        id_input = get_id_input()
        if is_exist(id_input):
            print("이미 존재하는 아이디입니다.")
        else :
            pw_input = get_pw_input()
            encoded_pw = hash_password(pw_input)
            cursor.execute("INSERT INTO users (username, password) VALUES(?, ?)", [id_input, encoded_pw])
            conn.commit()
            break

def login():
    id_input, pw_input = get_input()

    encoded_pw = hash_password(pw_input)
    cursor.execute("select * from users where username=? and password=?", [id_input, encoded_pw])
    result = cursor.fetchall()

    if len(result) == 1 :
        print("로그인에 성공하였습니다")
    else :
        print("로그인에 실패하였습니다")
    conn.commit()

mode = input("모드를 선택하세요 (signup, login) : ")

if (mode == "signup") :
    print("회원가입을 진행합니다")
    signup()
elif (mode == "login") :
    print("로그인을 진행합니다")
    login()
else :
    print("잘못된 t모드입니다. 다시 시작해주세요")
conn.close()