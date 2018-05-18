from mongoengine import StringField, IntField,Document, EmbeddedDocument,ListField, EmbeddedDocumentField,FloatField,DateTimeField
from datetime import datetime
class Group(EmbeddedDocument):
    id = IntField()
    name = StringField()
    lat = FloatField()
    lon = FloatField()
    def __init__(self, id, name,lat,lon,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.name = name
        self.lat = lat
        self.lon = lon

class Venue(EmbeddedDocument):
    id = IntField()
    name = StringField()
    lat = FloatField()
    address_1 = StringField()
    lon = FloatField()
    address= StringField()

    def __init__(self, id, name,lat,lon,address_1,address=" ", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.name = name
        self.lat = lat
        self.lon = lon
        self.address_1= address_1
        self.address = address

class Event(EmbeddedDocument):
    id = IntField()
    event_name = StringField()
    local_time = DateTimeField()
    venue = EmbeddedDocumentField(Venue)
    group = EmbeddedDocumentField(Group)
    link = StringField()
    description = StringField()


    def __init__(self, id, event_name,local_time,venue,group,link,description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.event_name = event_name
        self.local_time = local_time
        self.venue = venue
        self.group = group
        self.link= link
        self.description= description


class EventAddress(Document):
    event_list = ListField()

    def __init__(self, event_list , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_list = event_list