# En caso de un SO Windows hay que importar el certifi
from pymongo import MongoClient
import certifi
mongo_db_url = "mongodb+srv://devops:devops@gilded.gk2qp.mongodb.net/?retryWrites=true&w=majority"
# Función para conectarnos con nuestra BBDD
def conector_cluster(mongo_db_url):

        # Importante tener en cuenta para Windows el 'ce = certifi.where()'

        # Al final del enlace, para sistemas windows, hay que agregar 'tlsCAFile=ca'
    client = MongoClient(mongo_db_url, tlsCAFile = certifi.where())

    return client 
    
def acceder_BBDD(client):
    
    base_de_datos = client.Rose.Items.find()
    Items = []
    for item in base_de_datos:
        Items.append(item)
        continue
    print("all files imported")
    return Items


a = conector_cluster(mongo_db_url)
acceder_BBDD(a)