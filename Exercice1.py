import pymongo
import requests
import json


def get_lille():

    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=2000&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion&refine.commune=LILLE"
    response = requests.get(url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

def get_paris():
    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=2000&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&refine.nom_arrondissement_communes=Paris"
    response = requests.get(url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

def get_lyon():
    url = "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json?maxfeatures=-1&start=1"
    response = requests.get(url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("values", [])

def get_rennes():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel&q=&rows=2000&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet=nombrevelosdisponibles"
    response = requests.get(url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

def update_lille():

    jsonload = get_lille()

    for i in range (0,len(jsonload)):

        jsonloadbis = jsonload[i].get("fields")
        jsonville = jsonloadbis.get("commune")
        jsonnom = jsonloadbis.get("nom")
        jsonadresse = jsonloadbis.get("adresse")
        jsonetat = jsonloadbis.get("etat")
        jsontpe = jsonloadbis.get("type")
        jsongeo = jsonloadbis.get("geo")

        dictionnaire_stations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "etat": jsonetat, "tpe": jsontpe, "geoloc": jsongeo }
        col_stations.update_one({ "adresse": jsonadresse }, {"$set": dictionnaire_stations}, upsert=True)

        jsonvelodispo = jsonloadbis.get("nbvelosdispo")
        jsonplacedispo = jsonloadbis.get("nbplacesdispo")
        jsonmaj = jsonloadbis.get("datemiseajour")

        dictionnaire_infostations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "velosdispo": jsonvelodispo, "placesdispo": jsonplacedispo, "maj": jsonmaj }
        col_infostations.update_one({ "adresse": jsonadresse }, {"$set": dictionnaire_infostations}, upsert=True)

def update_paris():

    jsonload = get_paris()

    for i in range (0,len(jsonload)):

        jsonloadbis = jsonload[i].get("fields")
        jsonville = jsonloadbis.get("nom_arrondissement_communes")
        jsonnom = jsonloadbis.get("name")
        jsonadresse = "UNKNOWN"
        jsonetat = jsonloadbis.get("is_renting")
        jsontpe = "UNKNOWN"
        jsongeo = jsonloadbis.get("coordonnees_geo")

        dictionnaire_stations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "etat": jsonetat, "tpe": jsontpe, "geoloc": jsongeo }
        col_stations.update_one({ "nom": jsonnom }, {"$set": dictionnaire_stations}, upsert=True)

        jsonvelodispo = jsonloadbis.get("numbikesavailable")
        jsonplacedispo = jsonloadbis.get("numdocksavailable")
        jsonmaj = jsonload[i].get("record_timestamp")

        dictionnaire_infostations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "velosdispo": jsonvelodispo, "placesdispo": jsonplacedispo, "maj": jsonmaj }
        col_infostations.update_one({ "nom": jsonnom }, {"$set": dictionnaire_infostations}, upsert=True)

def update_lyon():

    jsonload = get_lyon()

    for i in range (0,len(jsonload)):

        jsonloadbis = jsonload[i]
        jsonville = jsonloadbis.get("commune")
        jsonnom = jsonloadbis.get("address2")
        jsonadresse = jsonloadbis.get("address")
        jsonetat = jsonloadbis.get("status")
        jsontpe = jsonloadbis.get("banking")
        jsongeo = [jsonloadbis.get("lat"), jsonloadbis.get("lon")]

        dictionnaire_stations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "etat": jsonetat, "tpe": jsontpe, "geoloc": jsongeo }
        col_stations.update_one({ "adresse": jsonadresse }, {"$set": dictionnaire_stations}, upsert=True)

        jsonvelodispo = jsonloadbis.get("available_bikes")
        jsonplacedispo = jsonloadbis.get("available_bike_stands")
        jsonmaj = jsonloadbis.get("last_update")

        dictionnaire_infostations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "velosdispo": jsonvelodispo, "placesdispo": jsonplacedispo, "maj": jsonmaj }
        col_infostations.update_one({ "adresse": jsonadresse }, {"$set": dictionnaire_infostations}, upsert=True)

def update_rennes():

    jsonload = get_rennes()

    for i in range (0,len(jsonload)):

        jsonloadbis = jsonload[i].get("fields")
        jsonville = "Rennes"
        jsonnom = jsonloadbis.get("nom")
        jsonadresse = "UNKNOWN"
        jsonetat = jsonloadbis.get("etat")
        jsontpe = "UNKNOWN"
        jsongeo = jsonloadbis.get("coordonnees")

        dictionnaire_stations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "etat": jsonetat, "tpe": jsontpe, "geoloc": jsongeo }
        col_stations.update_one({ "nom": jsonnom }, {"$set": dictionnaire_stations}, upsert=True)

        jsonvelodispo = jsonloadbis.get("nombrevelosdisponibles")
        jsonplacedispo = jsonloadbis.get("nombreemplacementsdisponibles")
        jsonmaj = jsonloadbis.get("lastupdate")

        dictionnaire_infostations = { "ville": jsonville, "nom": jsonnom, "adresse": jsonadresse, "velosdispo": jsonvelodispo, "placesdispo": jsonplacedispo, "maj": jsonmaj }
        col_infostations.update_one({ "nom": jsonnom }, {"$set": dictionnaire_infostations}, upsert=True)


"""
Debut
"""
print("!!! Debut !!!")


"""
Connexion a mongoDB et creation de la base de donnee si celle ci n'existe pas :
"""
#client = pymongo.MongoClient("mongodb+srv://lawaj:<PASSWORD>@isen-mongo-tp.1lwab.mongodb.net/ISEN-MONGO-TP?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["ISEN-MONGO-TP"]

col_stations = db["stations"]
col_infostations = db["infostations"]


"""
Remplissage ou Mise a jour de la DB
"""

update_lille()  # 110  Stations
update_paris()  # 1004 Stations
update_lyon()   # 429  Stations (5 Stations ne s'ajoutent pas)
update_rennes() # 57 Stations


"""
FIN
"""
print("!!! Fin !!!")