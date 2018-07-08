from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Product(Resource):

    def get(self):
        return {
            "products": [
                "Automate the Boring Stuff with Python",
                "Learn Python the Hard Way",
                "Fluent Python",
                "Think Python",
                "Python Cookbook"
            ]
        }

api.add_resource(Product, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
