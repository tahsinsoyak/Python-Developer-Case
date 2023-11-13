from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime
from flask_restful import Resource, Api



app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure and random value.
api = Api(app)

import sqlite3



def get_products_from_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('trendyol_products.db')
    cursor = conn.cursor()

    # Sample SQL query: Fetch all products
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # Close the connection
    conn.close()

    return products

def get_product_by_id(product_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('trendyol_products.db')
    cursor = conn.cursor()

    # Sample SQL query: Fetch a specific product
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    product = cursor.fetchone()

    # Close the connection
    conn.close()

    return product

def get_viewed_products_from_database():
    # SQLite veritabanına bağlanın
    conn = sqlite3.connect('trendyol_products.db')  # 'your_database.db' kısmını kendi veritabanı dosyanızın adıyla değiştirin.
    cursor = conn.cursor()

    # Örnek SQL sorgusu: Geçmişe bakılan ürünleri çek (timestamp sütununa göre azalan sırayla)
    cursor.execute("""
        SELECT p.* 
        FROM products p
        JOIN viewed_products v ON p.id = v.product_id
        ORDER BY v.timestamp DESC
    """)
    products = cursor.fetchall()

    # Bağlantıyı kapatın
    conn.close()

    return products


# This dictionary is used to store viewed products specific to user sessions.
# Each user has a list associated with a session ID.
viewed_products_dict = {}

@app.route('/')
def index():
    # Add functionality to display products on the home page.
    # For example, assign products fetched from the database to a variable and send it to the HTML page using render_template.
    products = get_products_from_database()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Add functionality to display product details.
    # For example, fetch a specific product from the database and send it to the HTML page using render_template.
    product = get_product_by_id(product_id)

    # Add the clicked product to the database
    add_product_to_database(product_id)

    # Get product recommendations
    recommendations = get_product_recommendations(product_id)

    return render_template('product_detail.html', product=product, recommendations=recommendations)

@app.route('/add_to_history/<int:product_id>')
def add_to_history(product_id):
    # Use the session to keep track of products viewed by the user.
    # Each product view is added to a list associated with the session.
    viewed_products = session.get('viewed_products', [])
    viewed_products.append(product_id)
    session['viewed_products'] = viewed_products

    # Add the clicked product to the database
    add_product_to_database(product_id)

    return redirect(url_for('product_detail', product_id=product_id))

def add_product_to_database(product_id):
    # Use this function to add the clicked product to the database.
    conn = sqlite3.connect('trendyol_products.db')
    cursor = conn.cursor()

    # Sample SQL query: Insert into viewed_products table with timestamp
    cursor.execute("INSERT INTO viewed_products (product_id, timestamp) VALUES (?, ?)",
                   (product_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

@app.route('/history')
def history():
    # Add functionality to fetch previously viewed products from the database.
    viewed_products = get_viewed_products_from_database()
    return render_template('history.html', viewed_products=viewed_products)

from machinelearning import get_recommendations, get_recommendations_json

def get_product_name_from_database(product_id):
    conn = sqlite3.connect('trendyol_products.db')
    cursor = conn.cursor()

    # Sample SQL query: Fetch a specific product
    cursor.execute("SELECT name FROM products WHERE id=?", (product_id,))

    # Fetch the result once and check if it's not None
    result = cursor.fetchone()
    product_name = result[0] if result else None

    # Close the connection
    conn.close()

    return product_name
@app.route('/product_recommendations/<int:product_id>')
def get_product_recommendations(product_id):
    product_name = get_product_name_from_database(product_id)
    product_name_str = str(product_name)
    recommendations = get_recommendations(product_name_str)
    return render_template('recommendations.html', product_name=product_name, recommendations=recommendations)


class GetRecommendationsResource(Resource):
    def get(self, product_id):
        product_name = get_product_name_from_database(product_id)
        product_name_str = str(product_name)
        recommendations = get_recommendations_json(product_name_str)
        return {'recommendations': recommendations}

api.add_resource(GetRecommendationsResource, '/api/get_recommendations/<int:product_id>')


if __name__ == '__main__':
    app.run(debug=True)
