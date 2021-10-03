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
#client = pymongo.MongoClient("mongodb+srv://lawaj:<PASSWORD>@isen-mongo-tp.1lwab.mongodb.net/ISEN-MONGO-TP?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['ISEN-MONGO-TP']

col_stations = db['stations']
col_infostations = db['infostations']

col_stations.create_index([('geoloc', '2dsphere')])

resultat = col_stations.find({"geoloc":{"$near":{"$geometry":{"type":"Point", "coordinates":[ lattt, longgg ]}}}})

for data in resultat:
    print(data)

print("")
print("")
print("")
nearest = col_stations.find_one({"geoloc":{"$near":{"$geometry":{"type":"Point", "coordinates":[ lattt, longgg ]}}}})
print("La station la plus proche est : ",nearest['nom'],".")

infos = col_infostations.find_one({"nom": nearest['nom']})
print("Cette station velo dispose de '",infos['placesdispo'],"' places de libres et de '",infos['velosdispo'],"' velos !")

print("")
print("")
print("")

"""
FIN
"""
print("!!! Fin !!!")

"""
Nous avons donc les stations classées de la plus proche à la plus loin, puis les informations sur la station la plus proche.
"""
