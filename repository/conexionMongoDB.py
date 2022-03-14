# En caso de un SO Windows hay que importar el certifi
from pymongo import MongoClient
import certifi
from repository.MongoURL import mongo_db_url

# Función para conectarnos con nuestra BBDD
def conector_cluster():

        # Importante tener en cuenta para Windows el 'ce = certifi.where()'
    ce = certifi.where()
        # Al final del enlace, para sistemas windows, hay que agregar 'tlsCAFile=ca'
    client = MongoClient(mongo_db_url, tlsCAFile = ce)

    return client 


if __name__ == "__main__":
    print(conector_cluster())
