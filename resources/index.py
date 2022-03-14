from flask_restful import Resource

class Index(Resource):
    def get(self):
        return "Bienvenido a mi tienda de objetos mágicos"