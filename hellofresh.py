from flask import Flask, jsonify, request
import json
from flatten_json import flatten
app = Flask(__name__)

input_metadata = [
		{
    "metadata": {
      "allergens": {
        "eggs": "true", 
        "nuts": "true", 
        "seafood": "true"
      }, 
      "calories": 230, 
      "carbohydrates": {
        "dietary-fiber": "4g", 
        "sugars": "1g"
      }, 
      "fats": {
        "saturated-fat": "0g", 
        "trans-fat": "1g"
      }
    }, 
    "name": "burger-nutrition-1"
  },{
    "metadata": {
      "allergens": {
        "eggs": "true", 
        "nuts": "true", 
        "seafood": "true"
      }, 
      "calories": 230, 
      "carbohydrates": {
        "dietary-fiber": "4g", 
        "sugars": "1g"
      }, 
      "fats": {
        "saturated-fat": "0g", 
        "trans-fat": "1g"
      }
    }, 
    "name": "pizza-nutrition-1"
  }
]

@app.route('/', methods=['GET'])
def welcome():
    return '<h1>Tariq Devops Test: Building a CRUD Api<h1>'

@app.route('/configs', methods=['GET'])
def get_config():
    return jsonify(input_metadata)

@app.route('/configs/<string:name>', methods=['GET'])
def get_single_config(name):
    metadata = [metadata for metadata in input_metadata if metadata['name'] == name]
    return jsonify(metadata)

@app.route('/configs', methods=['POST'])
def create_config():
    conf = request.json
    input_metadata.append(conf)
    return jsonify(conf), 201

@app.route('/configs/<string:name>', methods=['PUT'])
def update_config(name):
    metadata = [metadata for metadata in input_metadata if metadata['name'] == name]
    if metadata is not None:
    	metadata[0]['name'] = request.json.get('name', metadata[0]['name'])
    	metadata[0]['metadata'] = request.json.get('metadata', metadata[0]['metadata'])
    return jsonify(metadata), 201

@app.route('/configs/<string:name>', methods=['DELETE'])
def delete_config(name):
   # metadata = [metadata for metadata in input_metadata || [] if metadata['name'] == name]
    metadata = []
    for i in input_metadata or []:
	    if i['name'] == name:
		    metadata.append(i)
		    print(i['name'])
    input_metadata.remove(metadata[0])
    return jsonify({'deleted': True}), 200


@app.route('/search')
def search_query():
    args = request.args
    print(args)
    output = []
    for i in input_metadata:
        f = flatten(i, '.')
        key = args.keys()[0]
        value = args[key]
        
        if f.has_key(key) and f[key] == value:
            output.append(i)   
    return jsonify(output)
    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
