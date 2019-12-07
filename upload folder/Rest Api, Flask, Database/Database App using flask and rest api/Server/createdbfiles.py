import sqlite3

connection=sqlite3.connect('data.db')

cursor=connection.cursor()

create_query='CREATE TABLE IF NOT EXISTS users(userid TEXT,password TEXT)'

cursor.execute(create_query)

#create_xy='CREATE TABLE IF NOT EXISTS xy(x TEXT,y TEXT)'
#cursor.execute(create_xy)

#insert_query='insert into xy values("a","aa")'
connection.commit()
connection.close()