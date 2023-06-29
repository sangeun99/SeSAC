from flask import Flask, render_template, url_for
import csv

app = Flask(__name__, static_folder="static")

@app.route("/")
def root() :
    return render_template("index.html")

@app.route("/users")
def user():
    users = []
    with open('src/user.csv', newline='', encoding="utf-8") as user:
        reader = csv.DictReader(user)
        next(reader)
        for user in reader:
            users.append(user)
    return render_template("users.html", users=users)


@app.route("/user_detail/<userid>")
def user_detail(userid):
    users = []
    with open('src/user.csv', newline='', encoding="utf-8") as user:
        reader = csv.reader(user)
        next(reader)
        for user in reader:
            users.append(user)
    for user in users:
        if user[0] == userid:
            userinfo = user
    return render_template("user_detail.html", userinfo=userinfo)


@app.route("/stores")
def store():
    stores = []
    with open('src/store.csv', newline='', encoding="utf-8") as store:
        reader = csv.DictReader(store)
        next(reader)
        for store in reader:
            stores.append(store)
    return render_template("stores.html", stores=stores)

@app.route("/store_detail/<storeid>")
def store_detail(storeid):
    with open('src/store.csv', newline='', encoding="utf-8") as store:
        reader = csv.reader(store)
        next(reader)
        for store in reader:
            if store[0] == storeid :
                storeinfo = store
    return render_template("store_detail.html", storeinfo=storeinfo)


if __name__=="__main__":
    app.run(port=8080, debug=True)