from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.instance_path = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user-sample.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFIATIONS'] = False
app.debug = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    Id = db.Column(db.String(64), primary_key=True)
    Name = db.Column(db.String(16))
    Gender = db.Column(db.String(16))
    Age = db.Column(db.Integer())
    Birthdate = db.Column(db.String(32))
    Address = db.Column(db.String(64))
    # 관계 (relation) 셋업
    orderR = db.relationship('Order', backref='users') # 앞쪽 인자는 클래스명, 뒤쪽 backref는 table명

    def __repr__(self): # 파이썬 내장함수
        return f'<User {self.Id}, {self.Name}, {self.Gender}, {self.Age}, {self.Address}>'

class Store(db.Model):
    __tablename__ = 'stores'
    Id = db.Column(db.String(64), primary_key=True)
    Name = db.Column(db.String(32))
    Type = db.Column(db.String(32))
    Address = db.Column(db.String(64))
    orderR = db.relationship('Order', backref='stores')

    def __repr__(self):
        return f'<Store {self.Id}, {self.Name}, {self.Type}, {self.Address}>'

class Order(db.Model):
    __tablename__ = 'orders'
    Id = db.Column(db.String(64), primary_key=True)
    OrderAt = db.Column(db.String(64))
    StoreId = db.Column(db.String(64), db.ForeignKey('stores.Id'))
    UserId = db.Column(db.String(64), db.ForeignKey('users.Id'))

    def __repr__(self):
        return f'<Order {self.Id}, {self.OrderAt}, {self.StoreId}, {self.UserId}>'
        
@app.route('/')
def main():
    # 미션1. SQL 쿼리문을 작성하시오
    query = """
    SELECT users.Name, stores.Name, orders.OrderAt
    FROM users
    JOIN orders ON users.Id = orders.UserId
    JOIN stores ON stores.Id = orders.StoreId
    WHERE users.Name = "윤수빈"
    """

    # 미션2. SQLAlchemy 문법으로 작성하시오.
    users_order_stores = db.session.query(User, Order, Store) \
        .join(Order, User.Id == Order.UserId) \
        .join(Store, Store.Id == Order.StoreId) \
        .filter(User.Name == "윤수빈").all()
    print(users_order_stores)

    # 미션3. 역참조를 이용해 store 접근하시오.
    user = User.query.filter_by(Name="윤수빈").first()
    order_by_user = user.orderR
    for order in order_by_user :
        store = order.stores
        print(f"윤수빈이 방문한 상점은 {store.Name}, 시간은 {order.OrderAt}")
    
    return 'hello'

@app.route('/view')
def view():
    users = User.query.all()
    return render_template('view.html', data=users)
    
if __name__ == "__main__" :
    with app.app_context():
        db.create_all()
    app.run()