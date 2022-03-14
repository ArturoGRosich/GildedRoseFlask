from repository.conexionMongoDB import conector_cluster


class Filters():
    def getStock():
        return conector_cluster().Rose.Items.find({},{"_id":False})
