from flask_restful import Resource
from resources.stock import stock

class index(Resource):

    def get(self):
        return stock