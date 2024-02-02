from flask import Flask
from flask_pymongo import PyMongo
import os

app= Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://CCDP:CCDP1234@cluster0.ipybsef.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient("mongodb+srv://CCDP:CCDP1234@cluster0.7vkoanw.mongodb.net/?retryWrites=true&w=majority")
mongo = PyMongo(app)
db = mongo['cluster0']
try:
    mongo.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)