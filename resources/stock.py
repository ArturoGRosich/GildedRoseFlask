from aiohttp import request
from flask_restful import Resource, reqparse
from services.services import Services


class Stock(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('quality', type=int)
        self.parser.add_argument('sellIn', type=int)
    
    def get(self):
        args = dict(self.parser.parse_args())
        args = self.limpiarArgs(args)
        return Services.getStock(args)
    
    @staticmethod
    def limpiarArgs(args):
        newArgs = args.copy()
        for element in args:
            if args[element] == None:
                del newArgs[element]
        return newArgs