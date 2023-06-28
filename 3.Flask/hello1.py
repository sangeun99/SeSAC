from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def home():
    users = []
    with open('user.csv', newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            users.append(row)
    return render_template("index.html", usernames=users)

if __name__ =="__main__" :
    app.run(debug=True) # 5000번이 기본값