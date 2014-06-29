#!/usr/bin/python

from flask import json, jsonify
from pymongo import MongoClient
import requests
import os


client = MongoClient()
db = client['yo']
hackathons = db['hackathons']

api_key = os.environ['API_KEY']

def yo_all(token):
    requests.post("http://api.justyo.co/yoall/", 
                  data={'api_token': token})

def update_events():
    r = requests.get(
        "http://hackerleague.org/api/v1/hackathons.json")
    for event in r.json():
        if event.get('location').get('state') is "New York":
            update_collection(event)
            print 

def update_collection(event):
    


yo_all(api_key)
