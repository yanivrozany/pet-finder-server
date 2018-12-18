from flask import jsonify
import requests
import json 
from datetime import datetime,timedelta
from pprint import pprint
class PetFinderAPI:
    def __init__(self):
        self.url =  'http://api.petfinder.com/pet.find'

    @classmethod
    def findGoldenRetriver(cls):
        dogfinderparams = {
            'key' : '4bfcf4a30bd76fd140725518ec63ba9c',
            'animal': 'dog',
            'breed': "Golden Retriever",
            'location': 'WA',
            'count': '500',
            'format': 'json',
            
            }
        updated = datetime.now()    
        req = requests.get('http://api.petfinder.com/pet.find',params=dogfinderparams)
        responseData = req.json()
        petfinderArray = responseData['petfinder']['pets']['pet']
        return (responseData['petfinder']['pets']['pet']),updated

    @classmethod
    def updateData(cls,updated):
        #since we only have 10 calls per day update is every 2.5 hours in order not to skip the limit
        currenttime =  datetime.now() - timedelta(hours = -2.5)
        return (updated and (currenttime > updated) ),updated
    
    
