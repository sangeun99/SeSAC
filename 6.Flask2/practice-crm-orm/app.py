from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
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
    OrderR = db.relationship('Order', backref='users') # 앞쪽 인자는 클래스명, 뒤쪽 backref는 table명

    def __repr__(self): # 파이썬 내장함수
        return f'<User {self.Id}, {self.Name}, {self.Gender}, {self.Age}, {self.Address}>'

class Store(db.Model):
    __tablename__ = 'stores'
    Id = db.Column(db.String(64), primary_key=True)
    Name = db.Column(db.String(32))
    Type = db.Column(db.String(32))
    Address = db.Column(db.String(64))
    OrderR = db.relationship('Order', backref='storesss')

    def __repr__(self):
        return f'<Store {self.Id}, {self.Name}, {self.Type}, {self.Address}>'

class Item(db.Model):
    __tablename__ = 'items'
    Id = db.Column(db.String(64), primary_key=True)
    Name = db.Column(db.String(32))
    Type = db.Column(db.String(16))
    UnitPrice = db.Column(db.Integer())
    OrderItemR = db.relationship('OrderItem', backref='items')

    def __repr__(self):
        return f'<Item {self.Id}, {self.Name}, {self.Type}, {self.UnitPrice}>'

class Order(db.Model):
    __tablename__ = 'orders'
    Id = db.Column(db.String(64), primary_key=True)
    OrderAt = db.Column(db.String(64))
    StoreId = db.Column(db.String(64), db.ForeignKey('stores.Id'))
    UserId = db.Column(db.String(64), db.ForeignKey('users.Id'))
    OrderItemR = db.relationship('OrderItem', backref="orders")

    def __repr__(self):
        return f'<Order {self.Id}, {self.OrderAt}, {self.StoreId}, {self.UserId}>'

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    Id = db.Column(db.String(64), primary_key=True)
    OrderId = db.Column(db.String(64), db.ForeignKey('orders.Id'))
    ItemId = db.Column(db.String(64), db.ForeignKey('items.Id'))

    def __repr__(self):
        return f'<OrderItem {self.Id}, {self.OrderId}, {self.ItemId}>'

@app.route('/')
def main():
    
    """SELECT S.Name
      FROM orders O
      JOIN stores S
      ON O.StoreId = S.Id
      WHERE O.UserId = 
      (SELECT U.Id
      FROM users U
      WHERE Name = "윤수빈"
      LIMIT 1);"""
    
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
    order_by_user = user.OrderR
    for order in order_by_user :
        store = order.storesss
        print(f"윤수빈이 방문한 상점은 {store.Name}, 시간은 {order.OrderAt}")
    
    return 'hello'

@app.route('/user_detail/')
def user_detail():
    user_info = User.query.filter_by(Name="윤수빈").first()
    print(user_info)
    user_purchased_info = db.session.query(User.Name, Item.Name, func.count(Order.Id)) \
        .join(Order, User.Id == Order.UserId) \
        .join(OrderItem, Order.Id == OrderItem.OrderId) \
        .join(Item, Item.Id == OrderItem.ItemId) \
        .group_by(Item.Id) \
        .order_by(func.count(Order.Id)) \
        .filter(User.Id == "9f2b5e7b-24b5-4be5-85c3-ab2645980c31") \
        .all()
    
    return render_template('user_detail.html', data=user_purchased_info)
    
if __name__ == "__main__" :
    with app.app_context():
        db.create_all()
    app.run()