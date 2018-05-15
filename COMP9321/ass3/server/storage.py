import csv,sys
from mongoengine import connect
from models import *
from pymongo import MongoClient
import datetime
from flask_pymongo import PyMongo



def save_information(filename):
    connect(host='mongodb://admin:admin@ds119650.mlab.com:19650/ass3db')

    with open(filename, 'r') as f:
        file = csv.reader(f)
        if("categories" in filename):
            category_list = []

            for index,row in enumerate(file):
                if(index>0):
                    category_list.append(category(row[0],row[1],row[2],row[3]))
            categories(category_list).save()
        elif("cities" in filename):
            city_list = []
            for index,row in enumerate(file):
                if(index>0):
                    city_list.append(city(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
            cities(city_list).save()
        elif("topics" in filename):
            topic_list = []
            for index,row in enumerate(file):
                if(index>0):
                    topic_list.append(topic(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            topics(topic_list).save()
        elif():
            group_id = []
            category_id = []
            category_name = []
            category_shortname = []
            city_id = []
            city = []
            country = []
            created = []
            description = []
            group_photo_base_url = []
            group_photo_highres_link = []
            group_photo_photo_id = []
            group_photo_photo_link = []
            group_photo_thumb_link = []
            group_photo_type = []
            join_mode = []
            lat = []
            link = []
            lon = []
            members =[]
            group_name = []
            organizer_member_id = []
            organizer_name = []
            organizer_photo_base_url = []
            organizer_photo_highres_link = []
            organizer_photo_photo_id = []
            organizer_photo_photo_link = []
            organizer_photo_thumb_link = []
            organizer_photo_type = []
            rating = []
            state = []
            timezone = []
            urlname = []
            utc_offset = []
            visibility = []
            who = []
            for index, row in enumerate(file):
                if (index > 0):
                    group_id.append(row[0])
                    category_id.append(row[1])
                    category.name.append(row[2])
                    category.shortname.append(row[3])
                    city_id.append(row[4])
                    city.append(row[5])
                    country.append(row[6])
                    created.append(row[7])
                    description.append(row[8])
                    group_photo.base_url.append(row[9])
                    group_photo.highres_link.append(row[10])
                    group_photo.photo_id.append(row[11])
                    group_photo.photo_link.append(row[12])
                    group_photo.thumb_link.append(row[13])
                    group_photo.type.append(row[14])
                    join_mode.append(row[15])
                    lat.append(row[16])
                    link.append(row[17])
                    lon.append(row[18])
                    members.append(row[19])
                    group_name.append(row[20])
                    organizer.member_id.append(row[21])
                    organizer.name.append(row[22])
                    organizer.photo.base_url.append(row[23])
                    organizer.photo.highres_link.append(row[24])
                    organizer.photo.photo_id.append(row[25])
                    organizer.photo.photo_link.append(row[26])
                    organizer.photo.thumb_link.append(row[27])
                    organizer.photo.type.append(row[28])
                    rating.append(row[29])
                    state.append(row[30])
                    timezone.append(row[31])
                    urlname.append(row[32])
                    utc_offset.append(row[33])
                    visibility.append(row[34])
                    who.append(row[35])

            groups(group_id , category_id,category_name,category_shortname,city_id,city,country, \
                created,description,group_photo_base_url,group_photo_highres_link,group_photo_photo_id, \
                group_photo_photo_link, group_photo_thumb_link,group_photo_type, \
                join_mode,lat,link,lon,members,group_name,organizer_member_id,organizer_name, \
                organizer_photo_base_url,organizer_photo_highres_link,organizer_photo_photo_id, \
                organizer_photo_photo_link,organizer_photo_thumb_link,organizer_photo_type, \
                rating,state,timezone,urlname,utc_offset,visibility).save()


        else:
            pass

    return "hh"

