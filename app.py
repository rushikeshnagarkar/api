from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the database
@app.route('/')
def index():
    return "<h1 style= 'color:red'>Product test sql k bye </h1>"

# Define the endpoints
@app.route('/products', methods=['GET'])
def get_products():

    with sqlite3.connect('data.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Products")  
        products = c.fetchall()
        

    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    with sqlite3.connect('data.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        if product_id is None:
            return jsonify({"error": "Product not found"})
        product_detail = c.fetchall()
    return jsonify(product_detail)

@app.route('/product/product_id', methods=['POST'])
def create_product(): 
     with sqlite3.connect('data.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Products (id, Product) VALUES (1245, 'Sipper');")
     return jsonify({"message": "Product created successfully"})

@app.route('/products/update', methods=['PUT'])
def update_product():
     with sqlite3.connect('data.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE Products SET Product = 'Airpods' WHERE id = 1239;")
     return jsonify({"message": "Product updated successfully"})

@app.route('/products/delete', methods=['DELETE'])
def delete_product():
    with sqlite3.connect('data.db') as conn:
        c = conn.cursor()
        c.execute("DELETE FROM products WHERE id = 1245")
    return jsonify({"message": "Product deleted successfully"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)