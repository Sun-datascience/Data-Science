import sqlite3
#from rest-apidev.app import *

def insert(id,passw):
    conn=sqlite3.connect('data.db')
    cursor=conn.cursor()

    insert_query='INSERT INTO users VALUES(?,?)'
    cursor.execute(insert_query,(id,passw))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    select_query = 'SELECT * FROM users'
    cursor.execute(select_query)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete_user(id):
    conn=sqlite3.connect('data.db')
    cursor=conn.cursor()
    delete_query="delete from users where userid='{}'".format(id)
    print(delete_query)
    cursor.execute(delete_query)
    conn.commit()
    conn.close()


