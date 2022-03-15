from flask_restful import Resource
from services.filters import Filters

class GetByName(Resource):
    def get(self, name):
        return Filters.getByName(name)