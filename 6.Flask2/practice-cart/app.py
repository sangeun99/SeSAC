from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)

app.secret_key = 'my-secret-key'

items = {
    'item1' : {'name' : '상품1', 'price' : 5000},
    'item2' : {'name' : '상품2', 'price' : 2000},
    'item3' : {'name' : '상품3', 'price' : 3000}
}

@app.route('/')
def main():
    return render_template('index.html', items=items)

@app.route('/add_to_cart')
def add_to_cart():
    itemname = request.args.get('itemname')
    if 'cart' not in session :
        session['cart'] = {}
    
    # 1. 카트에 물건 담기
    # 2. 담은 이후 액션
    if itemname in session['cart'] :
        session['cart'][itemname] += 1
    else :
        session['cart'][itemname] = 1

    # 세션 데이터가 수정되었음을 Flask에 알린다
    session.modified = True

    return redirect(url_for('main'))

@app.route('/delete_from_cart')
def delete_from_cart():
    itemname = request.args.get('itemname')
    session['cart'].pop(itemname)
    session.modified = True
    return redirect(url_for('view_cart'))

@app.route('/view_cart')
def view_cart():
    cart_item = {}
    for item_name, quantity in session.get('cart', {}).items():
        item = items.get(item_name)
        if item :
            cart_item[item_name] = {'name' : item['name'], 'quantity' : quantity, 'price' : item['price']}

    # price 계산하기
    price = 0
    for item_name, item_info in cart_item.items() :
        price += item_info['price'] * item_info['quantity']

    return render_template('cart.html', cart=cart_item, total_price=price)

if __name__ == "__main__" :
    app.run(debug=True)