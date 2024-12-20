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
    db.commit()

async def sql_insert_product(productid, category, infoproduct):
    cursor.execute(queries.INSERT_products_details_QUERY, (
        productid, category, infoproduct))

    db.commit()

async def sql_insert_collection(productid, collection):
    cursor.execute(queries.INSERT_collection_products_QUERY, (
        productid,collection ))

    db.commit()
