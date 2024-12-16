import sqlite3
from db import queries


db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def DataBase_creatr():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_products_details)



async def sql_insert_store(modelname, Size, Price, Photo):
    cursor.execute(queries.INSERT_store_QUERY,(
        modelname, Size, Price, Photo
    ))

async def sql_insert_product(productid, category, infoproduct):
    cursor.execute(queries.INSERT_products_details_QUERY, (
        productid, category, infoproduct))

    db.commit()
