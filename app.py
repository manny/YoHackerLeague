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
yo_all(api_key)
