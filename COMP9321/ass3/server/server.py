
from flask import Blueprint
from server.models import Events, Group,Venue
from server.forms import BasicPartyForm,EditForm,CancelPartyForm
from app import db
from app import mongo
from flask import jsonify
server = Blueprint('server',__name__)


# create events
@server.route('/events/<location>',methods=['GET'])
def events(location):
    location=location.lower()
    event = mongo.db.event_address.find()[0]
    return_list = []

    for e in event['event_list'] :

        if "venue" in e.keys():

            address = e["venue"]["address"].lower()

            if location in address:


                return_list.append(e)
    if len(return_list) != 0:
        return jsonify(return_list)
    return "No Event In That location"
