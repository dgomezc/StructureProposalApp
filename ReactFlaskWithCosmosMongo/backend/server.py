import os

import constants
import flask
import mongo.service
import sample_data

app = flask.Flask(__name__, static_folder="build")

# List Endpoints
@app.route(constants.ENDPOINT_LIST)
def get_list():
    return flask.jsonify(mongo.service.get())


@app.route(constants.ENDPOINT_LIST, methods=["POST"])
def add_list_item():
    json_response = flask.jsonify(mongo.service.create())
    return flask.make_response(json_response, constants.HTTP_STATUS_201_CREATED)


@app.route(constants.ENDPOINT_LIST + "/<item_id>", methods=["DELETE"])
def delete_list_item(item_id):
    try:
        removed_item = flask.jsonify(mongo.service.delete(item_id))
        return removed_item
    except ValueError as ex:
        err_response = flask.jsonify({"error": str(ex)})
        return flask.make_response(err_response, constants.HTTP_STATUS_404_NOT_FOUND)


# MasterDetail Page Endpoint
@app.route(constants.ENDPOINT_MASTER_DETAIL)
def get_master_detail():
    return flask.jsonify(sample_data.sample_orders)


# Grid Page Endpoint
@app.route(constants.ENDPOINT_GRID)
def get_grid():
    return flask.jsonify(sample_data.sample_orders)


# Catching all routes
# This route is used to serve all the routes in the frontend application after deployment.
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    file_to_serve = "index.html"
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        file_to_serve = path
    return flask.send_from_directory(app.static_folder, file_to_serve)


# Error Handler
@app.errorhandler(constants.HTTP_STATUS_404_NOT_FOUND)
def page_not_found():
    json_response = flask.jsonify({"error": "Page not found"})
    return flask.make_response(json_response, constants.HTTP_STATUS_404_NOT_FOUND)


if __name__ == "__main__":
    app.run(port=constants.PORT)
