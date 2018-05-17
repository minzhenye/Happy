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

# Insert the dictionary into Mongo
@app.route('/',methods=['GET'])
def storeCsv():

        getResponseCode("https://api.meetup.com/2/cities?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","cities")
        getResponseCode("https://api.meetup.com/2/categories?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","categories")
        getResponseCode("https://api.meetup.com/2/groups?sign=true&photo-host=public&country=au&key=37357c27353310f2d4f417f855721&city=Sydney","groups")
        getResponseCode("https://api.meetup.com/find/upcoming_events?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&lon=151.2100067138672&lat=-33.869998931884766","events")
        '''
        for item in mongo.db.cities.find()[0]["results"]:
            getResponseCode("https://api.meetup.com/2/groups?sign=true&photo-host=public&country=au&key=37357c27353310f2d4f417f855721&lon="+str(item["lon"])+"&lat="+str(item["lat"]), "groups")
        
        for item in mongo.db.cities.find()[0]["results"]:
            getResponseCode("https://api.meetup.com/find/upcoming_events?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&lon="+str(item["lon"])+"&lat="+str(item["lat"]),"events")
        '''
        getResponseCode("https://api.meetup.com/topics?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721","topics")


        for item in mongo.db.groups.find()[0]["results"]:
            #for item_per_country in item["results"]:
            getResponseCode("https://api.meetup.com/2/members?sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&group_id="+str(item["id"]),"members")
        getResponseCode("https://api.meetup.com/find/venues?&sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&text=Australia&location=Sydney", "venues")
        '''
        for item in mongo.db.cities.find()[0]["results"]:
                getResponseCode("https://api.meetup.com/find/venues?&sign=true&photo-host=public&key=37357c27353310f2d4f417f855721&text=Australia&location="+item["city"],"venues")
        '''
        return "hhd"

#https://api.meetup.com/2/events?key=37357c27353310f2d4f417f855721&group_urlname=ny-tech&sign=true
#https://api.meetup.com/2/categories?sign=true&photo-host=public&fields=2&page=20&key=37357c27353310f2d4f417f855721&group_urlname=ny-tech&sign=true
def getResponseCode(url,collection_name):

    try:
        data = requests.get(url).json()
    except:
        return

    with app.app_context():
        if collection_name not in mongo.db.collection_names():
            collection = mongo.db.create_collection(collection_name)
            if(data != []):
                collection.insert(data)
                #print(data)
                if collection_name=="cities":
                    f=csv.writer(open('./data/cities.csv', 'w'))

                    f.writerow(["zip", "country", "localized_country_name", "distance", "city","lon","ranking","id","member_count","lat"])
                    for x in mongo.db.cities.find()[0]["results"]:
                        f.writerow([x["zip"],x["country"],x["localized_country_name"],x["distance"],x["city"],x["lon"],x["ranking"],x["id"],x["member_count"],x["lat"]])
                    '''
                    f.writerow(["zip", "country", "localized_country_name", "distance", "city","lon","ranking","id","member_count","lat"])
                    for x in mongo.db.cities.find()[0]["results"]:
                        f.writerow([x["zip"],x["country"],x["localized_country_name"],x["distance"],x["city"],x["lon"],x["ranking"],x["id"],x["member_count"],x["lat"]])
                    '''

        else:
            if(data!=[]):
                mongo.db[collection_name].insert(data)
                #print(data)
                if collection_name == "cities":
                    f=csv.writer(open('./data/cities.csv', 'w'))
                    for i,v in enumerate(data['results']):
                        #print(i,v)
                        key = v.keys()
                        value = v.values()
                        if i == 0:
                            f.writerow(key)
                        f.writerow(value)


    return 1

if __name__ == "__main__":

    app.run(debug=True, use_reloader=False)
