
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


@server.route('/events/bus',methods=['GET'])
def get_stops():
    parser = reqparse.RequestParser()
    parser.add_argument('lat',type=str)
    parser.add_argument('lon',type=str)
    args = parser.parse_args()
    lat = args.get('lat')
    lon = args.get('lon')
    bus =mongo.db.bus.find()
    for b in bus:

        bus_lat = b['lat']
        bus_lon = b['lon']
        if lat == bus_lat and lon == bus_lon:
            return jsonify(b["busInfo_list"])
    return "No Bus station Around"

