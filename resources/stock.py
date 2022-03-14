from flask_restful import Resource
from services.filters import Filters
from json import JSONEncoder
class Stock(Resource):
    def get(self):
        items = Filters.getStock()
        stock = []
        for item in items:
            stock.append(item)
        return stock
    