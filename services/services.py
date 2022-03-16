from repository.conexionMongoDB import conector_cluster


class Services():
    
    @staticmethod
    def getStock(args):
        items = conector_cluster().Rose.Items.find(args,{"_id":False})
        stock = []
        for item in items:
            stock.append(item)
        return stock

    

    def deleteItem(datta):
        items = conector_cluster().Rose.Items.delete_one(datta,{"_id":False})