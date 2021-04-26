import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from crudoperations import *
app = Flask(__name__)
port = int(os.getenv('PORT', 8081))
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    print(data)
    d = {}
    d['status'] = insertintotable(data)
    return jsonify(d)


@app.route('/update/<type>/<id>', methods=['POST'])
def update():
    data = request.get_json()
    print(data)
    msg=deletefromtable(id)
    d = {}
    if msg!="success":
        d['status']="failure"
        return jsonify(d)
    d['status'] = insertintotable(data)
    return jsonify(d)

@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    d = {}
    d['status'] = deletefromtable(id)
    return jsonify(d)

@app.route('/getsongsbytypeandid/<type>/<id>', methods=['GET'])
def getsongsbytypeandid(type,id):
    return jsonify(selectdatabytypeandid(type,id))

@app.route('/getsongsbytype', methods=['GET'])
def getsongsbytype():
    print(request.args)
    type = request.args.get('type')
    #data = request.get_json()
    #print(data)
    return jsonify(selectdatabytype(type))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)