from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def home(name=""):
    user_names = []
    with open('names.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            user_names.append(row)
    return render_template("index.html", username=user_names)

if __name__ =="__main__" :
    app.run(debug=True) # 5000번이 기본값