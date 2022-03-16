from flask_restful import Resource, reqparse
from services.services import Services

class UpdateStock(Resource):
    def get(self):
        return Services.updateStock()