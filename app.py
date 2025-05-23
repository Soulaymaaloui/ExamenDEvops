from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Product catalog with numeric codes
products = {
    1: {'description': 'Apple', 'price': 0.5, 'image': 'apple.png'},
    2: {'description': 'Banana', 'price': 0.3, 'image': 'banana.png'},
    3: {'description': 'Orange', 'price': 0.4, 'image': 'orange.png'},
    4: {'description': 'Mango', 'price': 1.0, 'image': 'mango.png'}
}

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_code = int(request.form['product'])
    quantity = int(request.form['quantity'])
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append({'code': product_code, 'quantity': quantity})
    session.modified = True
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(products[item['code']]['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart=cart_items, products=products, total=total)

if __name__ == '__main__':
    app.run(debug=True)
