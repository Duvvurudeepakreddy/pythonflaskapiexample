import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from crudoperations import *
app = Flask(__name__)
port = int(os.getenv('PORT', 8081))
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@cross_origin
@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    print(data)
    d = {}
    d['status'] = insertintotable(data)
    return jsonify(d)

@cross_origin
@app.route('/update', methods=['POST'])
def update():
    d = {}
    d = request.args.to_dict()
    print(d)
    type = request.args.get('type')
    id = request.args.get('id')
    data = request.get_json()
    print(data)
    msg=deletefromtable(type,id)
    d = {}
    if msg!="success":
        d['status']="failure"
        return jsonify(d)
    d['status'] = insertintotable(data)
    return jsonify(d)

@cross_origin
@app.route('/delete', methods=['GET'])
def delete():
    d = {}
    d = request.args.to_dict()
    print(d)
    type = request.args.get('type')
    id= request.args.get('id')
    d = {}
    d['status'] = deletefromtable(type,id)
    return jsonify(d)

@cross_origin
@app.route('/getsongs', methods=['GET'])
def getsongs():
    print(request.args)
    d={}
    d=request.args.to_dict()
    print(d)
    type = request.args.get('type')
    if "id" in d.keys():
        id=d['id']
        return jsonify(selectdatabytypeandid(type,id))
    return jsonify(selectdatabytypeandid(type))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)