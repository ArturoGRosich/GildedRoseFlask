from flask_restful import Resource
from services.filters import Filters
class GetBySellIn(Resource):
    def get(self, sell_in):
        return Filters.getByQuality(sell_in)