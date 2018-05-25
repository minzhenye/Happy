from flask import Blueprint,render_template,request,session,redirect,url_for,abort,flash
from event.forms import BasicEventForm, EditForm,CancelEventForm
from user.decorator import login_required
from flask_restful import reqparse
from  event.models import Event
from user.models import User
from utilities.storage import upload_image_file
import json
import bson
from application import mongo
from flask import jsonify
import math

event_page = Blueprint('event_page',__name__)

@event_page.route('/create',methods=['GET','POST'])
@login_required
def create():
  form = BasicEventForm()
  error = None
  if request.method == "POST" and form.validate():
    if form.end_datetime.data < form.start_datetime.data:
      error = "A party must end after it starts!"
    if not error:
      user = User.objects.filter(email=session.get('email')).first()
      event = Event(
        name=form.name.data,
        place=form.place.data,
        location=[form.lng.data, form.lat.data],
        start_time=form.start_datetime.data,
        end_time=form.end_datetime.data,
        description=form.description.data,
        host=user.id,
        attendees=[user]
      )
      # image_url = upload_image_file(request.files.get('photo'), 'party_photo', str(party.id))
      # if image_url:
      #   party.party_photo = image_url

      event.save() #save to mdb
      return '{} created'.format(event.name)

  return render_template('meetup/create.html', form = form)


@event_page.route('/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
  try:
    event = Event.objects.filter(id=bson.ObjectId(id)).first()
  except bson.error.InvalidId:
    abort(404)

  user = User.objects.filter(email=session.get('email')).first()
  if event and event.host == user.id: # only host(admin) can modify
    error = None
    message = None
    form = EditForm(obj=event)
    if request.method == "POST" and form.validate():
      if not error:
        form.populate_obj(event)
        if form.lng.data and form.lat.data:
          event.location = [form.lng.data, form.lat.data]
        image_url = upload_image_file(request.files.get('photo'), 'party_photo', str(event.id))
        if image_url:
          event.party_photo = image_url
        event.save()
        message = "Event updated"
    return render_template('meetup/edit.html', form=form, error=error, message=message, event=event)
  else:
    abort(404)


@event_page.route('/<id>/cancel',methods=['GET','POST'])
@login_required
def cancel(id):
  try:
    event = Event.objects.filter(id=bson.ObjectId(id)).first()
  except bson.errors.InvalidId:
    return "None"
  user = User.objects.filter(email=session.get('email')).first()
  if event and event.host == user.id and event.cancel == False:
    error = None
    form = CancelEventForm()
    if request.method=="POST" and form.validate():
      if form.confirm.data == 'yes':
        event.cancel = True
        event.save()
        return redirect(url_for('event_page.edit',id=event.id))
      else:
        error = "Say yes if you want to cancel"
    return render_template("meetup/cancel.html",form=form,error=error,event=event)
  else:
    return "None"


@event_page.route('/<id>',methods=['GET'])
def public(id):
    event  = mongo.db.event_address.find()[2]
    print(id)
    return_list =[]
    for e in event['event_list']:
        if str(e['id']) == id:
            return_list.append(e)
    print("here")
    print(return_list)
    if len(return_list) != 0:

        return render_template('meetup/public.html',event = return_list)


  # try:
  #   event = Event.objects.filter(id=bson.ObjectId(id)).first()
  # except bson.errors.InvalidId:
  #   return "None"
  # if event:
  #   host = User.objects.filter(id=event.host).first()
  #   user = User.objects.filter(email=session.get('email')).first()
  #   return render_template('meetup/public.html',event=event,host=host,user=user)
  # else:
  #   abort(404)



@event_page.route('/explore/<int:page>', methods=['GET'])
@event_page.route('/explore', methods=['GET'])
def explore(page=1):

  a =request.args
  print(a)
  # location = request.args.get('place').lower() #encoding error
  location = request.args.get('location','').lower()
  # place = request.args.get('place','').lower()
  # if place :
  #     location = place
  # location = request.form['place']
  # lng = float(request.args.get('lng')) # can not be empty
  # lat = float(request.args.get('lat'))
  #display_party = Event.objects(cancel=False).order_by('-start_time').paginate(page=page, per_page=4)

  # events = Event.objects(cancel=False).order_by('-start_time').paginate(page=page, per_page=4)

  event = mongo.db.event_address.find()[2]

  return_list = []
  # print(place)
  print(location)
  if not location :
      return render_template("meetup/explore.html",party_json= json.dumps(return_list),display_party = return_list)

  for e in event['event_list']:
      if "venue" in e.keys():
          address = e["venue"]["address"].lower()
          if location in address:
              return_list.append(e)
  if len(return_list) != 0:
      print(return_list)
      # i =  5
      # list = return_list[i,i+5]
      # pagination = Pagination(page=page, per_page=5, total=len(return_list),  record_name='List')
      # return_list = str(return_list)
      return render_template("meetup/explore.html", party_json= json.dumps(return_list),display_party = return_list)
  return "No Event In That Location"

def rad(x):
    return x * math.pi / 180;

def getDistance(p1lat,p1lng,p2lat,p2lng):
    R = 6378137
    dLat = rad(p2lat - p1lat)
    dLong = rad(p2lng - p1lng)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) +\
        math.cos(rad(p1lat)) * math.cos(rad(p2lat)) *\
        math.sin(dLong / 2) * math.sin(dLong / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d


@event_page.route('/explore/bus',methods=['POST'])
def get_stops():
    parser = reqparse.RequestParser()
    parser.add_argument('latlng',type=dict)
    # parser.add_argument('lon',type=str)
    args = parser.parse_args()
    latlng = args.get('latlng')
    print(type(latlng))


    lat = latlng['lat']
    lng = latlng['lng']

    bus = mongo.db.busStop.find()
    print(bus)
    buses=[]
    for b in bus:

        bus_lat = b['lat']
        # print(bus_lat)
        bus_lng = b['lon']
        distance = getDistance(lat,lng,bus_lat,bus_lng)
        print(distance)
        if distance <= 5000:
            # buses.append(b)
            print(b["locations"])
            return jsonify(location=b["locations"])

    return "No Bus station Around"

