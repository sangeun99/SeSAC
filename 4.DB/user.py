import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('user.db')
cursor = conn.cursor()

# 사용자 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT)''')

# 몇 명의 사용자 추가
users = [
    ('John Doe', 25, 'Male'),
    ('Jane Smith', 30, 'Female'),
    ('Michael Johnson', 35, 'Male'),
    ('Emily Davis', 28, 'Female'),
    ('David Lee', 32, 'Male'),
    ('Emma Wilson', 27, 'Female'),
    ('Daniel Brown', 31, 'Male'),
    ('Olivia Taylor', 29, 'Female'),
    ('Sophia Anderson', 33, 'Female'),
    ('Matthew Martin', 26, 'Male')
]

# cursor.executemany('INSERT INTO users (name, age, gender) VALUES (?, ?, ?)', users)

# 변경사항 저장
conn.commit()

# ---------------
#   쿼리문 연습
# ---------------

cursor.execute("select * from users where gender = 'Female'")
users = cursor.fetchall()
print("여성 사용자 목록")
for user in users:
    print(user)
print()

cursor.execute("SELECT * FROM users WHERE age >= 30")
users = cursor.fetchall()
print("30세 이상 사용자 목록")
for user in users:
    print(user)
print()

cursor.execute("SELECT * FROM users WHERE age BETWEEN 25 AND 30")
users = cursor.fetchall()
print("25세 이상 30세 이하 사용자 목록")
for user in users:
    print(user)
print()

cursor.execute("SELECT gender, count(*) FROM users GROUP BY gender")
users = cursor.fetchall()
print("성별 별 사용자 수")
for gender, count in users:
    print(f"성별 {gender}, 사용자수 {count}")
print()

cursor.execute("UPDATE users SET age = 26 WHERE name = 'John Doe'")
conn.commit()
cursor.execute("SELECT age FROM users WHERE name='John Doe'")
user = cursor.fetchone()
if(user[0] == 26) :
    print("John Doe의 나이 정보가 업데이트 되었습니다.")
print()

cursor.execute("DELETE FROM users WHERE name ='Emily Davis'")
conn.commit()
cursor.execute("SELECT * FROM users WHERE name = 'Emily Davis'")
users = cursor.fetchall()
if not users:
    print('Emily Davis의 회원정보가 삭제되었습니다.')
