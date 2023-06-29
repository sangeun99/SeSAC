from flask import Flask, render_template, url_for
import csv

app = Flask(__name__, static_folder="static")

@app.route("/")
def root() :
    return "hello"

@app.route("/users")
@app.route("/users/<int:index>")
def user(index = 1):
    per_page = 20
    data = []
    with open('src/user.csv', newline='', encoding="utf-8") as user:
        reader = csv.DictReader(user)
        next(reader)
        for row in reader:
            clean_row = {key.strip(): value.strip() for key, value in row.items()}
            data.append(clean_row)
    total_pages = int(len(data) / per_page) + 1
    start_index = (index - 1) * per_page
    end_index = index * per_page
    users = data[start_index: end_index]
    return render_template("users.html", users=users, total_pages=total_pages, index=index)

@app.route("/user_detail/<userid>")
def user_detail(userid):
    users = []
    with open('src/user.csv', newline='', encoding="utf-8") as user:
        reader = csv.DictReader(user)
        next(reader)
        for row in reader:
            clean_row = {key.strip(): value.strip() for key, value in row.items()}
            if clean_row['Id'] == userid :
                userinfo = clean_row
    return render_template("user_detail.html", userinfo=userinfo)

@app.route("/stores")
def store():
    stores = []
    with open('src/store.csv', newline='', encoding="utf-8") as store:
        reader = csv.DictReader(store)
        next(reader)
        for row in reader:
            clean_row = {key.strip(): value.strip() for key, value in row.items()}
            stores.append(clean_row)
    return render_template("stores.html", stores=stores)

@app.route("/store_detail/<storeid>")
def store_detail(storeid):
    with open('src/store.csv', newline='', encoding="utf-8") as store:
        reader = csv.DictReader(store)
        next(reader)
        for row in reader:
            clean_row = {key.strip(): value.strip() for key, value in row.items()}
            if clean_row['Id'] == storeid :
                storeinfo = clean_row
    return render_template("store_detail.html", storeinfo=storeinfo)

if __name__=="__main__":
    app.run(port=8080, debug=True)