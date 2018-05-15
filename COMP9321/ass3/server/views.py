from flask import Flask,request
from flask_pymongo import PyMongo
import requests
import urllib
from models import *
from mongoengine import connect
import json
from storage import save_information

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "ass3db"
app.config["MONGO_URI"] = "mongodb://admin:admin@ds119650.mlab.com:19650/ass3db"
mongo = PyMongo(app)

@app.route("/",methods=["GET"])
def createDataEntry():

    term = save_information("../data/categories.csv")
    term=save_information("../data/cities.csv")
    term=save_information("../data/topics.csv")
    return "hh"

if __name__ == "__main__":
    #print(mongo.db.cities["results"])
    #storeCsv()
    app.run(debug=True, use_reloader=False)
