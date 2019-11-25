import datetime
import os
import firebase_admin
from firebase_admin import db

def add_update_request(data):
    return UPDATE_REQUEST.push(data).key

try:
  cred = firebase_admin.credentials.Certificate("./firebaseServiceAccountKey.json")
  firebase_admin.initialize_app(cred, options={
    'databaseURL': 'https://kunit-backend.firebaseio.com/',
  })
  UPDATE_REQUEST = db.reference('update_requests')

except:
  print("Get environ key ERROR")
