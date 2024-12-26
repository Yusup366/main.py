import sqlite3
from db import queries


db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def DataBase_creatr():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_products_details)
    cursor.execute(queries.CREATE_TABLE_collection_products)



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
        product_id, collection ))

    db.commit()



def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * from store s
    INNER JOIN products_details  sd ON s.product_id = sd.product_id
    INNER JOIN collection_products cl ON cl.product_id = s.product_id
    """).fetchall()
    conn.close()
    return products

#Delete

def delete_product(product_id):
    conn = get_db_connection()

    conn.execute('DELETE FROM store WHERE product_id = ?', (product_id,))

    conn.commit()
    conn.close()


def update_product_field(product_id, field_name, new_value):
    store_table = ['name_product', 'size', 'price',' product_id', 'photo']
    store_details_table = ['category', 'product_id', 'info_product']
    collection_table = ['product_id','collection']

    conn = get_db_connection()

    try:
        if field_name in store_table:
            query = f'UPDATE store SET {field_name} = ? WHERE product_id = ?'
        elif field_name in store_details_table:
            query = f'UPDATE products_details SET {field_name} = ? WHERE product_id = ?'
        elif field_name in collection_table:
            query = f'UPDATE collection SET {field_name} = ? WHERE product_id = ?'

        else:
            raise ValueError(f'Нет такого поля {field_name}')

        conn.execute(query, (new_value, product_id))
        conn.commit()

    except sqlite3.OperationalError as error:
         print(f'Ошибка {error}')

    finally:
        conn.close()


