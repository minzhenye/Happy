from flask import Flask,request
from flask_pymongo import PyMongo
import sys,json
import requests
import urllib
import csv

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "ass3db"
app.config["MONGO_URI"] = "mongodb://admin:admin@ds119650.mlab.com:19650/ass3db"
mongo = PyMongo(app)

#Store information about australia using meetup api
@app.route('/meetup/',methods=['GET'])
def storeMeetup():
    storeToMongodb("https://api.meetup.com/2/cities?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","cities")
    storeToMongodb("https://api.meetup.com/2/categories?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","categories")
    storeToMongodb("https://api.meetup.com/2/groups?sign=true&photo-host=public&country=au&key=37357c27353310f2d4f417f855721&city=Sydney","groups")
    storeToMongodb("https://api.meetup.com/find/upcoming_events?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&lon=151.2100067138672&lat=-33.869998931884766","events")

    storeToMongodb("https://api.meetup.com/topics?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","topics")


    for item in mongo.db.groups.find()[0]["results"]:
        #for item_per_country in item["results"]:
        storeToMongodb("https://api.meetup.com/2/members?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&group_id="+str(item["id"]),"members")
    storeToMongodb("https://api.meetup.com/find/venues?&sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&text=Australia&location=Sydney", "venues")

    return "hhd"

#Store information about australia's bus stop using https://opendata.transport.nsw.gov.au/node/
@app.route('/bus/',methods=['GET'])
def storeBusInfo():

    for item in mongo.db.venues.find():
        #url="https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord=151.209778%3A-33.871082%3AEPSG%3A4326&coordOutputFormat=EPSG%3A4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&PoisOnMapMacro=true&version=10.2.1.42"
        url = "https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord="+str(item["lon"])+"%3A"+str(item["lat"])+"%3AEPSG%3A4326&coordOutputFormat=EPSG%3A4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&PoisOnMapMacro=true&version=10.2.1.42"
        #print(url)
        #print(requests.get(url,headers={"Authorization":"apikey 5KkTkqJFDX4PARiheh73aiEEQ7LyrJxyURVV"}).json())
        storeToMongodb(url,"busInfo")

        #storeToMongodb("https://api.transport.nsw.gov.au/v1/tp/stop_finder?outputFormat=rapidJSON&type_sf=stop&coordOutputFormat=EPSG%3A4326&TfNSWSF=true&version=10.2.1.42&name_sf="+"%20".join(item["address_1"].split(" ")),"busInfo")


    return "hhd"

# store the data to mongodb
def storeToMongodb(url,collection_name):

    try:
        if collection_name=="busInfo":
            data = requests.get(url,headers={"Authorization":"apikey 5KkTkqJFDX4PARiheh73aiEEQ7LyrJxyURVV"}).json()
        else:
            data = requests.get(url).json()
    except:
        return

    with app.app_context():
        if collection_name not in mongo.db.collection_names():
            collection = mongo.db.create_collection(collection_name)
            if(data != []):
                collection.insert(data)
        else:
            if(data!=[]):
                mongo.db[collection_name].insert(data)



    return 1

if __name__ == "__main__":

    app.run(debug=True, use_reloader=False)
