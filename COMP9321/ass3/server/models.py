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

'''
class Properties(EmbeddedDocument):
    distance = IntField()
    STOP_POINT_REFERED_NAME = StringField()
    STOP_POINT_REFERED_NAMEWITHPLACE = StringField()
    STOP_AREA_NAME = StringField()
    STOPPOINT_GLOBAL_ID = StringField()
    IDENTIFIER = StringField()


    def __init__(self, distance,STOP_POINT_REFERED_NAME,STOP_POINT_REFERED_NAMEWITHPLACE,STOP_AREA_NAME,STOPPOINT_GLOBAL_ID,IDENTIFIER,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.distance = distance
        self.STOP_POINT_REFERED_NAME= STOP_POINT_REFERED_NAME
        self.STOP_POINT_REFERED_NAMEWITHPLACE  = STOP_POINT_REFERED_NAMEWITHPLACE
        self.STOP_AREA_NAME = STOP_AREA_NAME
        self.STOPPOINT_GLOBAL_ID= STOPPOINT_GLOBAL_ID
        self.IDENTIFIER  = IDENTIFIER


class SubParent(EmbeddedDocument):
    name = StringField()
    id = StringField()
    type = StringField()

    def __init__(self,id,name,type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.name = name
        self.type = type

class ParentStop(EmbeddedDocument):
    disassembledName = StringField()
    name = StringField()
    id = StringField()
    isGlobalId = StringField()
    type = StringField()
    parent = EmbeddedDocumentField(SubParent)

    def __init__(self, disassembledName,name,id,isGlobalId,type,parent,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.disassembledName = disassembledName
        self.name = name
        self.type = type
        self.isGlobalId = isGlobalId
        self.parent = parent


class BusInfo(EmbeddedDocument):
    id = StringField()
    name = StringField()
    type = StringField()
    coord = ListField()
    parent = EmbeddedDocumentField(ParentStop)
    properties = EmbeddedDocumentField(Properties)

    def __init__(self, id, name,type,coord,parent,properties, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.coord = coord
        self.parent = parent
        self.properties= properties

class Bus(Document):
    lat = FloatField()
    lon = FloatField()
    busInfo_list = ListField()

    def __init__(self, lat,lon,busInfo_list , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lat = lat
        self.lon= lon
        self.busInfo_list = busInfo_list
'''