#!/usr/bin/python3
"""index file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {Amenity: "amenities", City: "cities", Place: "places",
           Review: "reviews", State: "states", User: "users"}


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def jsonStatus():
    """json status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def count_objects():
    count_dict = {}
    for obj, value in classes.items():
        count_dict[value] = storage.count(obj)
    return jsonify(count_dict)
