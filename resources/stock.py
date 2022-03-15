from flask_restful import Resource
from services.filters import Filters
class Stock(Resource):
    def get(self):
        return Filters.getStock()