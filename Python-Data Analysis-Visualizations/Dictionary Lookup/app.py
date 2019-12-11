from flask import Flask,request,jsonify
import json
from difflib import get_close_matches

app=Flask(__name__)

#@app.route('/getwordmeaning/<string:word>')
@app.route('/getwordmeaning')
def get_meaning():
    word=input('enter word')
    data=json.load(open('data.json'))
    word=word.lower()
    if word in data:
        return jsonify({'meaning':data[word]})
    else:
        similar=get_close_matches(word,data.keys)
        if len(similar)>0:
            response=input('did u mean {}'.format(similar[0]))
            if response=='y':
                return jsonify({'meaning':data[similar[0]]})
            else:
                return jsonify({'msg':'word not found'})
app.run(port=5000)













