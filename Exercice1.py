import pymongo
import requests
import json


def get_vlille():

    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=1000&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion&refine.commune=LILLE"
    response = requests.get(url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

client = pymongo.MongoClient("mongodb+srv://lawaj:P*123456789p@isen-mongo-tp.1lwab.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["ISEN-MONGO-TP"]

col_stations = db["stations"]
col_infostations = db["infostations"]

jsonload = get_vlille()

for i in range (0,len(jsonload)):

    jsonloadbis = jsonload[i].get("fields")
    jsonville = jsonloadbis.get("commune")
    jsonnom = jsonloadbis.get("nom")
    jsonadresse = jsonloadbis.get("adresse")
    jsonetat = jsonloadbis.get("etat")
    jsontpe = jsonloadbis.get("type")
    jsongeo = jsonloadbis.get("geo")

    dictionnaire_stations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "etat": jsonetat, "tpe": jsontpe, "geoloc": jsongeo }
    col_stations.insert_one(dictionnaire_stations)
    
    #dictionnaire_infostations = { "ville": "", "nom": "", "taille": "", "dispo": "", "indispo": "", "maj": "" }



"""
["ville"]
["geolocation"]
["size"]
["name"]
["tpe"]
["available"]
"""
