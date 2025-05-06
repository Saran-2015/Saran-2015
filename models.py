import sqlite3

DB_path = r"C:\\Users\\Saran\\Desktop\\IMA\\database.db"

def init_db():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    
    # Creating products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Creating stock table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock (
            stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            location TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )
    ''')
    
    # Creating product movement table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ProductMovement (
            movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            from_location TEXT NOT NULL,
            to_location TEXT,
            product_id INTEGER,
            qty INTEGER NOT NULL,
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )
    ''')

    conn.commit()
    conn.close()

# Product-related functions
def get_products():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def add_product(product_name, quantity, price):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (product_name, quantity, price) VALUES (?, ?, ?)',
                   (product_name, quantity, price))
    conn.commit()
    conn.close()

def update_product(product_id, product_name, quantity, price):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET product_name = ?, quantity = ?, price = ? WHERE product_id = ?',
                   (product_name, quantity, price, product_id))
    conn.commit()
    conn.close()

# Stock-related functions
def get_stock():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT stock.stock_id, products.product_name, stock.location, stock.quantity, stock.product_id
        FROM stock
        JOIN products ON stock.product_id = products.product_id
    ''')
    stock = cursor.fetchall()
    conn.close()
    return stock

def add_stock(product_id, location, quantity):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO stock (product_id, location, quantity) VALUES (?, ?, ?)',
                   (product_id, location, quantity))
    conn.commit()
    conn.close()

def get_stock_by_id(stock_id):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stock WHERE stock_id = ?', (stock_id,))
    stock = cursor.fetchone()
    conn.close()
    return stock

def update_stock(stock_id, product_id, location, quantity):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE stock SET product_id = ?, location = ?, quantity = ? WHERE stock_id = ?',
                   (product_id, location, quantity, stock_id))
    conn.commit()
    conn.close()

# Product Movement functions

def add_product_movement(product_id, from_location, to_location, qty):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ProductMovement (product_id, from_location, to_location, qty)
        VALUES (?, ?, ?, ?)
    ''', (product_id, from_location, to_location, qty))
    conn.commit()
    conn.close()

def get_product_movements():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ProductMovement')
    movements = cursor.fetchall()
    conn.close()
    return movements

def get_product_movement_by_id(movement_id):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ProductMovement WHERE movement_id = ?', (movement_id,))
    movement = cursor.fetchone()
    conn.close()
    return movement

def update_product_movement(movement_id, from_location, to_location, qty):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE ProductMovement
        SET from_location = ?, to_location = ?, qty = ?
        WHERE movement_id = ?
    ''', (from_location, to_location, qty, movement_id))
    conn.commit()
    conn.close()

def get_product_movements_with_names():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT pm.movement_id, pm.timestamp, p.product_name, 
               pm.from_location, pm.to_location, pm.qty
        FROM ProductMovement pm
        LEFT JOIN products p ON pm.product_id = p.product_id
        ORDER BY pm.timestamp DESC
    ''')
    movements = cursor.fetchall()
    conn.close()
    return movements