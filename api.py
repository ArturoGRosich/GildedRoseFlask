from flask import Flask
from flask_restful import Api
from resources.index import index

app = Flask(__name__)
api = Api(app, catch_all_404s=True)


api.add_resource(index, "/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)