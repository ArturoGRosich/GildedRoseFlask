from repository.conexionMongoDB import conector_cluster


class Services():
    def getStock():
        items = conector_cluster().Rose.Items.find({},{"_id":False})
        stock = []
        for item in items:
            stock.append(item)
        return stock

    def getByName(name):
        items = conector_cluster().Rose.Items.find({"name":name},{"_id":False})
        stock = []
        for item in items:
            stock.append(item)
        return stock
    
    def getByQuality(quality):
        items = conector_cluster().Rose.Items.find({"quality":int(quality)},{"_id":False})
        stock = []
        for item in items:
            stock.append(item)
        return stock
    
    def getByQuality(sell_in):
        items = conector_cluster().Rose.Items.find({"sell_in":int(sell_in)},{"_id":False})
        stock = []
        for item in items:
            stock.append(item)
        return stock