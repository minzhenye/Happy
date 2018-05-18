import csv,sys
from mongoengine import connect
from models import *
from pymongo import MongoClient
import datetime
from flask_pymongo import PyMongo
import requests


def save_information(data,attr):
    connect(host='mongodb://admin:admin@ds119650.mlab.com:19650/ass3db')
    event_list = []
    for item in data[attr]:
        if "venue" in item.keys():
            url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(item["venue"]["lat"]) + "," + str(
                item["venue"][
                    "lon"]) + "&sensor=false&key=AIzaSyAGfS3UBjayITaJnnusH1N-_csWV8c3FrA&result_type=street_address"
            data_address = requests.get(url).json()
            # print(url)
            if (len(data_address["results"]) != 0):
                data_event_address = data_address["results"][0]["formatted_address"]
            if "local_date" in item.keys():
                if "description" in item.keys():

                    if attr=="events":
                        event_list.append(Event(item["id"], item["name"], item["local_date"] + " " + item["local_time"],
                                                Venue(item["venue"]["id"], item["venue"]["name"], item["venue"]["lat"],
                                                      item["venue"]["lon"], item["venue"]["address_1"],data_event_address), \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["lat"],
                                                      item["group"]["lon"]), item["link"], item["description"]))
                    else:
                        event_list.append(Event(item["id"], item["name"], item["local_date"] + " " + item["local_time"],
                                                Venue(item["venue"]["id"], item["venue"]["name"], item["venue"]["lat"],
                                                      item["venue"]["lon"], item["venue"]["address_1"],data_event_address), \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["group_lat"],
                                                      item["group"]["group_lon"]), item["event_url"], item["description"]))
                else:
                    if attr == "events":
                        event_list.append(Event(item["id"], item["name"], item["local_date"] + " " + item["local_time"],
                                                Venue(item["venue"]["id"], item["venue"]["name"], item["venue"]["lat"],
                                                      item["venue"]["lon"], item["venue"]["address_1"],data_event_address), \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["lat"],
                                                      item["group"]["lon"]), item["link"], None))
                    else:
                        event_list.append(Event(item["id"], item["name"], item["local_date"] + " " + item["local_time"],
                                                Venue(item["venue"]["id"], item["venue"]["name"], item["venue"]["lat"],
                                                      item["venue"]["lon"], item["venue"]["address_1"],data_event_address), \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["group_lat"],
                                                      item["group"]["group_lon"]), item["event_url"], item["description"]))

            else:
                if "description" in item.keys():
                    if attr == "events":
                        event_list.append(Event(item["id"], item["name"], " ",
                                                Venue(item["venue"]["id"], item["venue"]["name"], item["venue"]["lat"],
                                                      item["venue"]["lon"], item["venue"]["address_1"],data_event_address), \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["lat"],
                                                      item["group"]["lon"]), item["link"], item["description"]))
                    else:
                        event_list.append(Event(item["id"], item["name"], " ",
                                                Venue(item["venue"]["id"], item["venue"]["name"], item["venue"]["lat"],
                                                      item["venue"]["lon"], item["venue"]["address_1"],data_event_address), \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["group_lat"],
                                                      item["group"]["group_lon"]), item["event_url"], item["description"]))
                else:
                    if attr == "events":
                        event_list.append(Event(item["id"], item["name"], " ",
                                                Venue(item["venue"]["id"], item["venue"]["name"], item["venue"]["lat"],
                                                      item["venue"]["lon"], item["venue"]["address_1"],data_event_address), \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["lat"],
                                                      item["group"]["lon"]), item["link"], None))
                    else:
                        event_list.append(Event(item["id"], item["name"], " ",
                                                Venue(item["venue"]["id"], item["venue"]["name"], item["venue"]["lat"],
                                                      item["venue"]["lon"], item["venue"]["address_1"],data_event_address), \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["group_lat"],
                                                      item["group"]["group_lon"]), item["event_url"], None))

        else:
            if "local_date" in item.keys():
                if "description" in item.keys():
                    if attr == "events":
                        event_list.append(Event(item["id"], item["name"], item["local_date"] + " " + item["local_time"],
                                                None, \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["lat"],
                                                      item["group"]["lon"]), item["link"], item["description"]))
                    else:
                        event_list.append(Event(item["id"], item["name"], item["local_date"] + " " + item["local_time"],
                                                None, \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["group_lat"],
                                                      item["group"]["group_lon"]), item["event_url"], item["description"]))
                else:
                    if attr == "events":
                        event_list.append(Event(item["id"], item["name"], item["local_date"] + " " + item["local_time"],
                                                None, \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["lat"],
                                                      item["group"]["lon"]), item["link"], None))
                    else:
                        event_list.append(Event(item["id"], item["name"], item["local_date"] + " " + item["local_time"],
                                                None, \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["group_lat"],
                                                      item["group"]["group_lon"]), item["event_url"], None))
            else:
                if "description" in item.keys():
                    if attr == "events":
                        event_list.append(Event(item["id"], item["name"], None,
                                                None, \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["lat"],
                                                      item["group"]["lon"]), item["link"], item["description"]))
                    else:
                        event_list.append(Event(item["id"], item["name"], None,
                                                None, \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["group_lat"],
                                                      item["group"]["group_lon"]), item["event_url"], item["description"]))
                else:
                    if attr == "events":
                        event_list.append(Event(item["id"], item["name"], None,
                                                None, \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["lat"],
                                                      item["group"]["lon"]), item["link"], None))
                    else:
                        event_list.append(Event(item["id"], item["name"], None,
                                                None, \
                                                Group(item["group"]["id"], item["group"]["name"], item["group"]["group_lat"],
                                                      item["group"]["group_lon"]), item["event_url"], None))
    e = EventAddress(event_list)
    e.save()