CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT,
    productid TEXT,
    photo TEXT,
    submit TEXT
    )
"""



INSERT_store_QUERY = """
    INSERT INTO store (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""



CREATE_TABLE_products_details = """
    CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    category TEXT,
    info_product TEXT
    )
"""


INSERT_products_details_QUERY = """
INSERT INTO products_details (product_id, category, info_product)
VALUES (?, ?, ?)
"""


CREATE_TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    collection TEXT
    )
"""

INSERT_collection_products_QUERY = """
INSERT INTO collection_products (product_id, collection)
VALUES (?, ?)
"""

