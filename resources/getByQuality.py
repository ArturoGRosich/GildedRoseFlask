from flask_restful import Resource
from services.filters import Filters
class GetByQuality(Resource):
    def get(self, quality):
        return Filters.getByQuality(quality)