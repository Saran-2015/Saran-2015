from flask import Flask, render_template, request, redirect, url_for, flash
from models import init_db, get_products, add_product, update_product, get_stock, add_stock, get_stock_by_id, update_stock, add_product_movement, get_product_movements, get_product_movement_by_id, update_product_movement, get_product_movements_with_names
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Product')
def product():
    products = get_products()
    return render_template('product.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product_route():
    product_name = request.form['product_name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    add_product(product_name, quantity, price)
    flash("Product added successfully!", "success")
    return redirect(url_for('product'))

@app.route('/update_product/<int:product_id>', methods=['GET', 'POST'])
def update_product_route(product_id):
    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        update_product(product_id, product_name, quantity, price)
        flash("Product updated successfully!", "success")
        return redirect(url_for('product'))

    conn = sqlite3.connect(r"C:\\Users\\Saran\\Desktop\\IMA\\database.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE product_id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    return render_template('update_product.html', product=product)

@app.route('/location')
def location():
    stocks = get_stock()
    conn = sqlite3.connect(r"C:\\Users\\Saran\\Desktop\\IMA\\database.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return render_template('location.html', stocks=stocks, products=products)

@app.route('/add_stock', methods=['POST'])
def add_stock_route():
    product_id = int(request.form['product_id'])
    location = request.form['location']
    quantity = int(request.form['quantity'])
    add_stock(product_id, location, quantity)
    flash("Stock added successfully!", "success")
    return redirect(url_for('location'))

@app.route('/edit_location/<int:stock_id>', methods=['GET', 'POST'])
def edit_location(stock_id):
    stock = get_stock_by_id(stock_id)
    conn = sqlite3.connect(r"C:\\Users\\Saran\\Desktop\\IMA\\database.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        location = request.form['location']
        quantity = int(request.form['quantity'])
        update_stock(stock_id, product_id, location, quantity)
        flash("Stock updated successfully!", "success")
        return redirect(url_for('location'))

    return render_template('edit_location.html', stock=stock, products=products)

@app.route('/product_movements')
def product_movements():
    movements = get_product_movements_with_names()
    products = get_products()
    return render_template('product_movements.html', movements=movements, products=products)

@app.route('/add_product_movement', methods=['GET', 'POST'])
def add_product_movement_route():
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        qty = int(request.form['qty'])
        add_product_movement(product_id, from_location, to_location, qty)
        flash("Product movement added successfully!", "success")
        return render_template('add_product_movement.html')

    products = get_products()  # Get all products for the form
    return render_template('add_product_movement.html', products=products)

@app.route('/edit_product_movement/<int:movement_id>', methods=['GET', 'POST'])
def edit_product_movement_route(movement_id):
    movement = get_product_movement_by_id(movement_id)
    if request.method == 'POST':
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        qty = int(request.form['qty'])
        update_product_movement(movement_id, from_location, to_location, qty)
        flash("Product movement updated successfully!", "success")

    return render_template('edit_product_movement.html', movement=movement)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
