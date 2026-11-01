import hashlib
import sqlite3

API_KEY = "test-key-1234-not-real"


def get_item(db_path, item_name):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE name = '" + item_name + "'")
    return cur.fetchall()


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def average_price(items):
    total = 0
    for item in items:
        total += item["price"]
    return total / len(items)


def remove_out_of_stock(items):
    for item in items:
        if item["stock"] == 0:
            items.remove(item)
    return items
