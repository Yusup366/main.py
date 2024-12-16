from tkinter.constants import INSERT

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelname TEXT,
    Size TEXT,
    Price TEXT,
    Photo TEXT,
    Submit TEXT
    )
"""



INSERT_store_QUERY = """
    INSERT INTO store (modelname, Size, Price, Photo)
    VALUES (?, ?, ?, ?)
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


