import pymongo
import requests
import json


def get_vlille():

    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion&refine.commune=LILLE"
    response = requests.requests("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

#client = pymongo.MongoClient("mongodb+srv://lawaj:P*123456789p@isen-mongo-tp.1lwab.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["ISEN-MONGO-TP"]

col_stations = db["stations"]
col_infostations = db["infostations"]

"""
["ville"]
["geolocation"]
["size"]
["name"]
["tpe"]
["available"]
"""
