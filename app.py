from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Product catalog
products = {
    'Apple': {'price': 0.5, 'image': 'apple.png'},
    'Banana': {'price': 0.3, 'image': 'banana.png'},
    'Orange': {'price': 0.4, 'image': 'orange.png'}
}

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product = request.form['product']
    quantity = int(request.form['quantity'])
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append({'product': product, 'quantity': quantity})
    session.modified = True
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(products[item['product']]['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart=cart_items, products=products, total=total)

if __name__ == '__main__':
    app.run(debug=True)
