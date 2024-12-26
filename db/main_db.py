import sqlite3
from db import queries


db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def DataBase_creatr():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_products_details)



async def sql_insert_store(name_product, size, price, product_id, photo):
    cursor.execute(queries.INSERT_store_QUERY,(
        name_product, size, price, product_id, photo
    ))
    db.commit()

async def sql_insert_product(product_id, category, info_product):
    cursor.execute(queries.INSERT_products_details_QUERY, (
        product_id, category, info_product))

    db.commit()

async def sql_insert_collection(product_id, collection):
    cursor.execute(queries.INSERT_collection_products_QUERY, (
        product_id,collection ))

    db.commit()

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * from store s
    INNER JOIN store_details  sd ON s.product_id = sd.product_id
    INNER JOIN collection cl ON cl.product_id = sd.product_id
    """).fetchall()
    conn.close()
    return products

#Delete

def delete_product(product_id):
    conn = get_db_connection()

    conn.execute('DELETE FROM store WHERE product_id = ?', (product_id,))

    conn.commit()
    conn.close()




