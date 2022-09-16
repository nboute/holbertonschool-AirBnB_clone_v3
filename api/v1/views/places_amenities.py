#!/usr/bin/python3
"""places amenities file"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.place import Place
from models.amenity import Amenity
from models import storage, storage_t

@app_views.route("places/<place_id>/amenities", methods=['GET'],
                 strict_slashes=False)
def allAmenities(place_id):
    """list all amenities of a place"""
    amenity_list=[]
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    for amenity in place.amenities:
        amenity_list.append(amenity.to_dict())
    return jsonify(amenity_list)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=['DELETE'], strict_slashes=False)
def amenity_delete(place_id, amenity_id):
    """Delete a amenity object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if storage_t == "db":
        if amenity not in place.amenities:
            abort(404)
        amenity.delete()
    else:
        if amenity.id not in place.amenity_ids:
            abort(404)
        place.amenity_ids.remove(amenity.id)
    storage.save()
    return {}, 200


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=['POST'], strict_slashes=False)
def amenity_post(place_id, amenity_id):
    """list of all amenity objects"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if storage_t == "db":
        if amenity in place.amenities:
            return amenity, 200
    else:
        if amenity.id in place.amenity_ids:
            return amenity, 200
