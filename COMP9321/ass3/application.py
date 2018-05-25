from flask import Flask
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

db = MongoEngine()
mongo = PyMongo()
def create_app(config= None):
    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)
    app.config['MONGO_DBNAME'] = "ass3db"
    app.config['MONGO_URI'] = 'mongodb://admin:admin@ds119650.mlab.com:19650/ass3db'
    mongo.init_app(app)
    db.init_app(app)

    # db.init_app(app)

    @app.route("/")
    def hello():
        return "home"

    from user.view import user_page
    app.register_blueprint(user_page,url_prefix ="/user")

    from event.views import event_page
    app.register_blueprint(event_page, url_prefix="/event")

    return app