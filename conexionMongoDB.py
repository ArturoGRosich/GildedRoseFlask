from repository.conexionMongoDB import conector_cluster

a = conector_cluster()
a = a.Rose.Items.get()

a.insert_one()