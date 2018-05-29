from flask import Flask,request
from flask_pymongo import PyMongo
import sys,json
import requests
import urllib
import csv
from models import *
from mongoengine import connect
from storeEventsAddress import *
import re
app = Flask(__name__)


app.config["MONGO_DBNAME"] = "ass3db"
app.config["MONGO_URI"] = "mongodb://admin:admin@ds119650.mlab.com:19650/ass3db"
mongo = PyMongo(app)

#Store information about australia using meetup api
@app.route('/meetup/',methods=['GET'])
def storeMeetup():
    print("???????")
    '''
    storeToMongodb("https://api.meetup.com/2/cities?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","cities")
    storeToMongodb("https://api.meetup.com/2/categories?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","categories")
    storeToMongodb("https://api.meetup.com/2/groups?sign=true&photo-host=public&country=au&key=37357c27353310f2d4f417f855721&city=Sydney","groups")
    storeToMongodb("https://api.meetup.com/find/upcoming_events?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&lon=151.2100067138672&lat=-33.869998931884766","events")

    storeToMongodb("https://api.meetup.com/topics?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","topics")


    for item in mongo.db.groups.find()[0]["results"]:
        #for item_per_country in item["results"]:
        storeToMongodb("https://api.meetup.com/2/members?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&group_id="+str(item["id"]),"members")
    storeToMongodb("https://api.meetup.com/find/venues?&sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&text=Australia&location=Sydney", "venues")


    storeToMongodb(
        "https://api.meetup.com/2/open_events?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&lon=151.2100067138672&lat=-33.869998931884766",
        "open_events")

    '''


    return "hhd"

#Store information about australia's bus stop using https://opendata.transport.nsw.gov.au/node/
@app.route('/bus/',methods=['GET'])
def storeBusInfo():
    '''
    for item in mongo.db.venues.find():
        #url="https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord=151.209778%3A-33.871082%3AEPSG%3A4326&coordOutputFormat=EPSG%3A4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&PoisOnMapMacro=true&version=10.2.1.42"

        lat = item["lat"]
        lon = item["lon"]
        url = "https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord="+str(item["lon"])+"%3A"+str(item["lat"])+"%3AEPSG%3A4326&coordOutputFormat=EPSG%3A4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&PoisOnMapMacro=true&version=10.2.1.42"

        #storeToMongodb(url,"busInfo")
        storeBusMongodb(url,lat,lon)
    '''
    for item in mongo.db.event_address.find()[2]["event_list"]:
        #url="https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord=151.209778%3A-33.871082%3AEPSG%3A4326&coordOutputFormat=EPSG%3A4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&PoisOnMapMacro=true&version=10.2.1.42"
        if "venue" in item.keys():
            lat = item["venue"]["lat"]
            lon = item["venue"]["lon"]
            print(lat,lon)
            url = "https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord="+str(item["venue"]["lon"])+"%3A"+str(item["venue"]["lat"])+"%3AEPSG%3A4326&coordOutputFormat=EPSG%3A4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&PoisOnMapMacro=true&version=10.2.1.42"

        #storeToMongodb(url,"busInfo")
            storeBusMongodb(url,lat,lon)

    return "hhd"

def storeBusMongodb(url, lat,lon):
    data = requests.get(url, headers={"Authorization": "apikey 5KkTkqJFDX4PARiheh73aiEEQ7LyrJxyURVV"}).json()
    data.update({"lat":lat})
    data.update({"lon": lon})

    collection_name="bus"
    if collection_name not in mongo.db.collection_names():
        collection = mongo.db.create_collection(collection_name)
        if (data != []):
            collection.insert(data)
    else:
        if (data != []):
            mongo.db[collection_name].insert(data)
    

    #save_Bus(data,lat,lon)

    return

# store the data to mongodb
def storeToMongodb(url,collection_name):

    try:
        data = requests.get(url).json()
    except:
        return

    if collection_name == "events" or collection_name == "open_events":
        if collection_name=="events":

            save_information(data,"events")
        else:
            mongo.db["open_events"].insert(data)

            for item in data["results"]:
                #print(item.keys())
                if "description" in item.keys():
                    item["description"] = item["description"].replace("<p>", "").replace("</p>", ".").replace("<br/>","").replace("</a>", "").replace("&amp;","&").replace("</a>","").replace("&gt;",">").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "")

                    if "<a" in item["description"]:
                        subresult = re.findall('<a.*?>',item["description"])

                        for subitem in subresult:
                            item["description"] = item["description"].replace(subitem, " ")
                    if "<img" in item["description"]:

                        subresult = re.findall('<img.*?/>',item["description"])
                        for subitem in subresult:
                            item["description"] = item["description"].replace(subitem, " ")
                else:
                    print("-----------------------------------------")

            save_information(data, "results")
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
