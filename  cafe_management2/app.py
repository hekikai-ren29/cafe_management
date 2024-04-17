from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# データベースに接続
def connect_db():
    return sqlite3.connect('cafe_management.db')

# 商品一覧表示
@app.route('/')
def show_products():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Products')
    products = cur.fetchall()
    conn.close()
    return render_template('index.html', products=products)

# 商品追加
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['product_name']
        category = request.form['category']
        price = request.form['price']
        stock_quantity = request.form['stock_quantity']

        conn = connect_db()
        cur = conn.cursor()
        cur.execute('INSERT INTO Products (ProductName, Category, Price, StockQuantity) VALUES (?, ?, ?, ?)',
                    (product_name, category, price, stock_quantity))
        conn.commit()
        conn.close()
        return redirect(url_for('show_products'))
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)
