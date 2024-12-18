CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelname TEXT,
    Size TEXT,
    Price TEXT,
    productid TEXT,
    Photo TEXT,
    Submit TEXT
    )
"""



INSERT_store_QUERY = """
    INSERT INTO store (modelname, Size, Price, productid, Photo)
    VALUES (?, ?, ?, ?, ?)
"""



CREATE_TABLE_products_details = """
    CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    category TEXT,
    infoproduct TEXT
    )
"""


INSERT_products_details_QUERY = """
INSERT INTO products_details (productid, category, infoproduct)
VALUES (?, ?, ?)
"""


CREATE_TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    collection TEXT
    )
"""

INSERT_collection_products_QUERY = """
INSERT INTO collection_products (productid, collection)
VALUES (?, ?)
"""

