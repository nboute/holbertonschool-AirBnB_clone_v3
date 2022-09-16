#!/usr/bin/python3
"""Flask application"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
cors = CORS(app, resources={
    r"/*":{"origins":"0.0.0.0"}
})
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(self):
    """close the storage"""
    storage.close()


@app.errorhandler(404)
def resource_not_found(e):
    return (jsonify({"error": "Not found"})), 404


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)
