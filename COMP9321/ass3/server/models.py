
'''
from mongoengine import StringField,Document,ListField,EmbeddedDocument,EmbeddedDocumentField,IntField


class group_topic(EmbeddedDocument):
    group_id = IntField()
    topic_id = IntField()
    topic_name = StringField()
    topic_key = StringField()


    def __init__(self, group_id, topic_id,topic_name,topic_key, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.topic_id = topic_id
        self.topic_name = topic_name
        self.topic_key = topic_key
        self.group_id = group_id

class grouptopicList(Document):
    group_name = StringField()
    grouptopicList = ListField(EmbeddedDocumentField(group_topic))
    def __init__(self, group_name, grouptopicList = [],*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = group_name
        self.grouptopicList = grouptopicList
'''

from mongoengine import StringField, IntField,Document, EmbeddedDocument,ListField, EmbeddedDocumentField,FloatField,DateTimeField
from datetime import datetime
class category(EmbeddedDocument):
    category_id = IntField()
    category_name = StringField()
    short_name = StringField()
    sort_name = StringField()

    def __init__(self, category_id, category_name,short_name,sort_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_id= category_id
        self.category_name = category_name
        self.short_name = short_name
        self.sort_name = sort_name

class categories(Document):
    category_list = ListField()

    def __init__(self, category_list , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_list = category_list

class city(EmbeddedDocument):
    city = StringField()
    city_id = IntField()
    country = StringField()
    distance = FloatField()
    latitude = FloatField()
    localized_country_name = StringField()
    longitude = FloatField()
    member_count = IntField()
    ranking = IntField()
    state = StringField()
    zip = IntField()

    def __init__(self, city, city_id,country,distance,latitude,localized_country_name,longitude, member_count,ranking,state, zip, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city= city
        self.city_id = city_id
        self.country = country
        self.distance = distance
        self.latitude= latitude
        self.localized_country_name= localized_country_name
        self.member_count = member_count
        self.ranking = ranking
        self.statet = state
        self.zip = zip

class cities(Document):
    city_list = ListField()

    def __init__(self, city_list , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_list = city_list


class topic(EmbeddedDocument):
    topic_id = IntField()
    description = StringField()
    link = StringField()
    members = IntField()
    topic_name = StringField()
    urlkey = StringField()
    main_topic_id = IntField()
    def __init__(self, topic_id, description,link,members,topic_name,urlkey,main_topic_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.topic_id = topic_id
        self.description= description
        self.link = link
        self.members = members
        self.topic_name = topic_name
        self.urlkey= urlkey
        self.main_topic_id = main_topic_id

class topics(Document):
    topic_list = ListField()

    def __init__(self, topic_list , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.topic_list = topic_list

class groups(EmbeddedDocument):
    group_id = ListField()
    category_id = ListField()
    category_name = ListField()
    category_shortname = ListField()
    city_id = ListField()
    city = ListField()
    country = ListField()
    created = ListField()
    description = ListField()
    group_photo_base_url = ListField()
    group_photo_highres_link = ListField()
    group_photo_photo_id = ListField()
    group_photo_photo_link = ListField()
    group_photo_thumb_link = ListField()
    group_photo_type = ListField()
    join_mode = ListField()
    lat = ListField()
    link = ListField()
    lon = ListField()
    members = ListField()
    group_name = ListField()
    organizer_member_id = ListField()
    organizer_name = ListField()
    organizer_photo_base_url = ListField()
    organizer_photo_highres_link = ListField()
    organizer_photo_photo_id = ListField()
    organizer_photo_photo_link = ListField()
    organizer_photo_thumb_link = ListField()
    organizer_photo_type = ListField()
    rating = ListField()
    state = ListField()
    timezone = ListField()
    urlname = ListField()
    utc_offset = ListField()
    visibility = ListField()
    who = ListField()

    def __init__(self, group_id , category_id,category_name,category_shortname,city_id,city,country, \
                created,description,group_photo_base_url,group_photo_highres_link,group_photo_photo_id, \
                group_photo_photo_link, group_photo_thumb_link,group_photo_type, \
                join_mode,lat,link,lon,members,group_name,organizer_member_id,organizer_name, \
                organizer_photo_base_url,organizer_photo_highres_link,organizer_photo_photo_id, \
                organizer_photo_photo_link,organizer_photo_thumb_link,organizer_photo_type, \
                rating,state,timezone,urlname,utc_offset,visibility,who,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.group_id = group_id


        self.category_id = category_id
        self.category.name = category.name
        self.category.shortname = category.shortname
        self.city_id = city_id
        self.city = city
        self.country = country
        self.created = created
        self.description = description
        self.group_photo_base_url = group_photo_base_url
        self.group_photo_highres_link = group_photo_highres_link
        self.group_photo_photo_id = group_photo_photo_id
        self.group_photo_photo_link = group_photo_photo_link
        self.group_photo_thumb_link = group_photo_thumb_link
        self.group_photo_type = group_photo_type
        self.join_mode = join_mode
        self.lat = lat
        self.link = link
        self.lon = lon
        self.members = members
        self.group_name = group_name
        self.organizer_member_id = organizer_member_id
        self.organizer_name = organizer_name
        self.organizer_photo_base_url = organizer_photo_base_url
        self.organizer_photo_highres_link = organizer_photo_highres_link
        self.organizer_photo_photo_id = organizer_photo_photo_id

        self.organizer_photo_photo_link = organizer_photo_photo_link
        self.organizer_photo_thumb_link = organizer_photo_thumb_link
        self.organizer_photo_type = organizer_photo_type
        self.rating = rating
        self.state = state
        self.timezone = timezone
        self.urlname = urlname
        self.utc_offset = utc_offset
        self.visibility = visibility
        self.who = who


