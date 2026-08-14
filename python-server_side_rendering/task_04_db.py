#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite using Flask."""

import csv
import json
import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)


def read_json():
    """Read and return product data from a JSON file."""
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Read and return product data from a CSV file."""
    products = []

    with open('products.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


def read_sql():
    """Read and return product data from a SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT id, name, category, price FROM Products'
    )

    rows = cursor.fetchall()
    conn.close()

    products = []

    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })

    return products


@app.route('/products')
def products():
    """Display products from the requested data source."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None

    try:
        if source == 'json':
            product_list = read_json()
        elif source == 'csv':
            product_list = read_csv()
        elif source == 'sql':
            product_list = read_sql()
        else:
            return render_template(
                'product_display.html',
                products=[],
                error='Wrong source'
            )
    except sqlite3.Error:
        return render_template(
            'product_display.html',
            products=[],
            error='Database error'
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

        product_list = [
            product for product in product_list
            if product['id'] == product_id
        ]

        if not product_list:
            error = 'Product not found'

    return render_template(
        'product_display.html',
        products=product_list,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)