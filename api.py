import flask
from flask import request, jsonify
import json 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


with open('students.json', encoding='utf-8') as f:
    data = json.load(f)

print(type(data))

@app.route('/', methods=['GET'])
def home():
    return jsonify(data)

@app.route('/student/<mssv>', methods=['GET'])
def api_studentId(mssv):
    for s in data['students']:
        if s['studentID'] == mssv:
            return jsonify(s)
    return jsonify()

app.run()