import pymongo
import requests
import json


"""
Variable
"""



"""
Fonctions
"""




"""
Debut
"""
print("!!! Debut !!!")


"""
Connexion a mongoDB et creation de la base de donnee si celle ci n'existe pas :
"""
client = pymongo.MongoClient("mongodb+srv://lawaj:P*123456789p@isen-mongo-tp.1lwab.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["ISEN-MONGO-TP"]

col_stations = db["stations"]
col_infostations = db["infostations"]





"""
FIN
"""
print("!!! Fin !!!")