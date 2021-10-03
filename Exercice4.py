import pymongo
import requests
import json
import re


"""
Debut
"""
print("!!! Debut !!!")
print("")
print("")

station_name = "porte" #Entrer ici ce que vous recherchez


station_name = "(?i)"+station_name #Ajout de REGEX pou ne pas prendre en compte les MAJjuscules et MINuscules

"""
Connexion a mongoDB
"""
#client = pymongo.MongoClient("mongodb+srv://lawaj:<PASSWORD>@isen-mongo-tp.1lwab.mongodb.net/ISEN-MONGO-TP?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['ISEN-MONGO-TP']

col_stations = db['stations']
col_infostations = db['infostations']

resultat = col_infostations.find({'nom': re.compile(station_name)}, {'_id': 0, 'maj': 0, 'velosdispo': 0, 'placesdispo': 0, 'adresse': 0})

print("Resultat 1 :")
for data in resultat:
    print(data)

print("")
print("")
print("")

filtertest = {'nom': re.compile(station_name), 'velosdispo': {'$gte': 5}, 'placesdispo': {'$gte': 10}} #Test de filtre pour ne ressortir que les stations ayant au moins 5 Velos de dispo et 10 places de dispo, toujour contenant 'station_name' dnas leurs noms

resultbis = col_infostations.find(filtertest, {'_id': 0, 'maj': 0})

print("Resultat 2 :")
for databis in resultbis: {print(databis)}

"""
FIN
"""
print("")
print("")
print("!!! Fin !!!")

"""
Affiche toutes les stations contenant 'station_name' dans leurs noms, puis test des filtres $lte (lower or equal) et $gte (greater or equal).
"""
