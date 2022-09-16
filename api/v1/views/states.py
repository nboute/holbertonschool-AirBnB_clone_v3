#!/usr/bin/python3
"""states file"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.state import State
from models import storage


@app_views.route("/states", methods=['GET'], strict_slashes=False)
def allState():
    """list of all state objects"""
    my_list = []
    states = storage.all(State)
    for state in states.values():
        my_list.append(state.to_dict())
    return jsonify(my_list)


@app_views.route("/states/<state_id>", methods=['GET'], strict_slashes=False)
def state_by_id(state_id):
    """list one state object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.to_dict()


@app_views.route("/states/<state_id>", methods=['DELETE'],
                 strict_slashes=False)
def state_delete(state_id):
    """Delete a state object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        state.delete()
        storage.save()
        return {}, 200


@app_views.route("/states/", methods=['POST'], strict_slashes=False)
def state_post():
    """list of all state objects"""
    body = request.get_json()
    if body is None:
        abort(400, description="Not a JSON")
    if 'name' not in body.keys():
        abort(400, description="Missing name")
    state = State(**body)
    state.save()
    return state.to_dict(), 201


@app_views.route("/states/<state_id>", methods=['PUT'], strict_slashes=False)
def state_put(state_id):
    """list of all state objects"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    body = request.get_json()
    if body is None:
        abort(400, description="Not a JSON")
    ignored_keys = ('id', 'created_at', 'updated_at')
    for key, value in body.items():
        if key not in ignored_keys:
            setattr(state, key, value)
    storage.save()
    return state.to_dict(), 200
