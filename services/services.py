from repository.conexionMongoDB import conector_cluster


class Services():
    
    @staticmethod
    def getStock(args):
        items = conector_cluster().Rose.Items.find(args,{"_id":False})
        stock = []
        for item in items:
            stock.append(item)
        return stock

    

    def postItem(args):
        conector_cluster().Rose.Items.insert_one(args)

    def deleteItem(args):
        conector_cluster().Rose.Items.delete_one(args)