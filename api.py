from flask import Flask
from flask_restful import Api
from resources.index import Index
from resources.stock import Stock
from resources.getByName import GetByName
from resources.getByQuality import GetByQuality

from resources.getBySellIn import GetBySellIn
app = Flask(__name__)
api = Api(app, catch_all_404s=True)

api.add_resource(Index, "/")
api.add_resource(Stock, "/items")
api.add_resource(GetByName, "/items/getByName/<name>")
api.add_resource(GetByQuality, "/items/getByQuality/<quality>")
api.add_resource(GetBySellIn, "/items/getBySellIn/<sell_in>")
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)