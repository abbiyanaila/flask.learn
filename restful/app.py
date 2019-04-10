#import some library
from flask import Flask, request
from flask_restful import Resource, Api, reqparse #resource that thing is our API can return and create and thing
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__) #special python variable, unique name
app.secret_key = 'qwerty'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /aut   h , we send username and password, and JWT extension gets that username
# and password

items = [] #list items


class Item(Resource): #every resource has to be a class
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank !"
                        )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) #The function filter(function, list) offers an
        # elegant way to filter out all the elements of a list, for which the function function returns True.

        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {'item': item}, 200 if item else 404 #information for data was create or not

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'massage': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        # data = request.get_json() #request data with json file
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #information for data was create or not

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'massage': 'Item delete'}
    #
    def put(self, name):
        # data = request.get_json()
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>') #pengganti route pada class Item
api.add_resource(ItemList, '/items') #pengganti route pada class ItemList

app.run(port=8400, debug=True)
