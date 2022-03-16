from flask_restful import Resource, reqparse
from services.services import Services


class Stock(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('quality', type=int)
        self.parser.add_argument('sell_in', type=int)
        self.parser = self.limpiarArgs(dict(self.parser.parse_args()))
    
    def get(self):
        print(self.parser)
        return Services.getStock(self.parser)
    
    def post(self):
        Services.postItem(self.parser)
        return "all good"
    
    def delete(self):
        Services.deleteItem(self.parser)
        return self.parser

    @staticmethod
    def limpiarArgs(args):
        newArgs = args.copy()
        for element in args:
            if args[element] == None:
                del newArgs[element]
        return newArgs