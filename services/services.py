from repository.conexionMongoDB import conector_cluster
from flask import g
from repository.itemFactory import ItemFactory

class Services():
    
    @staticmethod
    def getStock(args = {}):
        items = conector_cluster().Rose.Items.find(args,{"_id":False})
        stock = []
        for item in items:
            stock.append(item)
        return stock

    

    def postItem(args):
        conector_cluster().Rose.Items.insert_one(args)

    def deleteItem(args):
        conector_cluster().Rose.Items.delete_one(args)
    
    def updateStock():
        for item in Services.getStock():
            itemObject = ItemFactory.CreateItem(item)
            itemObject.updateQuality()
            conector_cluster().Rose.Items.update_one(item,{"$set": itemObject.toJSON()})
        return Services.getStock()
            