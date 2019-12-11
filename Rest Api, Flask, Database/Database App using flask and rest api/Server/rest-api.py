

from flask import Flask,request,jsonify
from db_functions import *

app=Flask(__name__)



@app.route('/viewusers')
def viewusers():
    l=[]
    for row in view():
        l.append(row)
    return jsonify({'msg':l})
    #return l

@app.route('/adduser',methods=['POST'])
def adduser():
    data=request.get_json()
    id=data['id']
    passw=data['passw']
    insert(id, passw)
    return jsonify({'msg':'User added'})


@app.route('/deleteuser',methods=['POST'])
def deleteuser():
    data=request.get_json()
    id=data['id']
    delete_user(id)
    return jsonify({'msg':'user deleted'})

app.run(port
        =5010)
