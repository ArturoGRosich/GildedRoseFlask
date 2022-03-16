from flask import Flask
from flask_restful import Api
from resources.index import Index
from resources.stock import Stock
from resources.updateStock import UpdateStock
app = Flask(__name__)
api = Api(app, catch_all_404s=True)

api.add_resource(Index, "/")
api.add_resource(Stock, "/items")
api.add_resource(UpdateStock, "/items/updateQuality")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
