from pymongo import MongoClient
import requests
import json

def get_vlille():

    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion&refine.commune=LILLE"
    response = requests.requests("GET", url)
    response_json = json.loads(response.text.encorede('utf8'))
    return response_json.get("records", [])

