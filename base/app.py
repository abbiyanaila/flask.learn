from flask import Flask, jsonify, request, render_template #add some library from flask


app = Flask(__name__) #objec of flask with unique name


stores = [ # JSON dictionary
    {
        'name': 'My wonderful Store',
        'items': [
            {
             'name': 'My Item',
             'price': 19.00
            }
        ]
    }
]


@app.route('/') # create route as decorator
def home(): #method
    return render_template('index.html')


# POST -used to receive data
# GET -used to send data back only


# POST /store data: {name:}
@app.route('/store', methods=['POST']) #decorator
def create_store(): #fyction
    request_data = request.get_json() #create request with send json data
    new_store = { #create new store, which is gonna be dictionary
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store) #convert the stores variable into  json


#GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/store_name'
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'massage': 'store not found'}) #convert the stores variable into  json


#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) #convert the stores variable into json: and take json from stores


#POST /store/<string:name>/item {name:, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'massage': 'store not found'}) #convert the stores variable into  json


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'massage': 'store not found'}) #convert the stores variable into  json


app.run(port=8400) #run the app with specific port