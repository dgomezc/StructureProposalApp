from flask import Flask, jsonify, make_response, send_from_directory
import os
from os.path import exists, join

from mongo.mongo_service import get, create, delete

from constants import CONSTANTS
from sample_data import sample_data


app = Flask(__name__, static_folder='build')

# List Endpoints
@app.route(CONSTANTS['ENDPOINT']['LIST'])
def get_list():
    return jsonify(get())

@app.route(CONSTANTS['ENDPOINT']['LIST'], methods=['POST'])
def add_list_item():
    json_response = jsonify(create())
    return make_response(json_response, CONSTANTS['HTTP_STATUS']['201_CREATED'])

@app.route(CONSTANTS['ENDPOINT']['LIST'] + '/<id>', methods=['DELETE'])
def delete_list_item(id):
    try:
        removed_item = jsonify(delete(id))
        return removed_item
    except Exception as ex:
        err_response = jsonify({'error': str(ex)})
        return make_response(err_response, CONSTANTS['HTTP_STATUS']['404_NOT_FOUND'])

# MasterDetail Page Endpoint
@app.route(CONSTANTS['ENDPOINT']['MASTER_DETAIL'])
def get_master_detail():
    return jsonify(sample_data['text_assets'])

# Grid Page Endpoint
@app.route(CONSTANTS['ENDPOINT']['GRID'])
def get_grid():
    return jsonify(sample_data['text_assets'])

# Catching all routes
# This route is used to serve all the routes in the frontend application after deployment.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    file_to_serve = path if path and exists(join(app.static_folder, path)) else 'index.html'
    return send_from_directory(app.static_folder, file_to_serve)

# Error Handler
@app.errorhandler(404)
def page_not_found(error):
    json_response = jsonify({'error': 'Page not found'})
    return make_response(json_response, CONSTANTS['HTTP_STATUS']['404_NOT_FOUND'])

if __name__ == '__main__':
    app.run(port=CONSTANTS['PORT'])
