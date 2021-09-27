import pymongo
import requests
import json


"""
Debut
"""
print("!!! Debut !!!")



#Entrez votre Latitude (ex : 48.201)"
lattt = 48.015
#Entrez votre Longitude (ex : 2.165)"
longgg = 1.684



"""
Connexion a mongoDB
"""
client = pymongo.MongoClient("mongodb+srv://lawaj:P*123456789p@isen-mongo-tp.1lwab.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['ISEN-MONGO-TP']

col_stations = db['stations']
col_infostations = db['infostations']

col_stations.create_index([('geoloc', '2dsphere')])

resultat = col_stations.find({"geoloc":{"$near":{"$geometry":{"type":"Point", "coordinates":[ lattt, longgg ]}}}})

for data in resultat:
    print(data)

"""
FIN
"""
print("!!! Fin !!!")

"""
Nous avons donc les stations classées de la plus proche à la plus loin, par manque de temps,
nous n'avons pas eu le temps de comparer les noms de stations avec la deuxieme collection (col_infostations),
pour resortir le nombre de vélos et de stands disponnibles
"""