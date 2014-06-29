#!/usr/bin/python

from flask import json, jsonify
from pymongo import MongoClient
from key import api_key
import requests


client = MongoClient()
db = client['yo']
hackathons = db['hackathons']

def yo_all(token):
    requests.post("http://api.justyo.co/yoall/", 
                  data={'api_token': token})

def update_events():
    r = requests.get(
        "http://hackerleague.org/api/v1/hackathons.json")
    for event in r.json():
        if event.get('location').get('state') == "New York":
            update_collection(event)

def update_collection(event):
    entry = hackathons.find_one({"name": event['name']})
    if entry is None:
        hackathons.insert({"name" : event['name']})
        yo_all(api_key)

update_events()
