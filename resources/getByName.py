from flask_restful import Resource
from services.services import Services

class GetByName(Resource):
    def get(self, name):
        return Services.getByName(name)