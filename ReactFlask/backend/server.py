import os
import uuid

import constants
import flask
import sample_data

app = flask.Flask(__name__, static_folder="build")

# MasterDetail Page Endpoint
@app.route(constants.ENDPOINT_MASTER_DETAIL)
def get_master_detail():
    return flask.jsonify(sample_data.sample_orders)


# List Endpoints
@app.route(constants.ENDPOINT_LIST)
def get_list():
    return flask.jsonify(sample_data.sample_list)


@app.route(constants.ENDPOINT_LIST, methods=["POST"])
def add_list_item():
    data = flask.request.get_json()
    list_item = {"id": str(uuid.uuid4()), "text": data["text"]}
    sample_data.sample_list.insert(0, list_item)
    json_response = flask.jsonify(list_item)
    return flask.make_response(json_response, constants.HTTP_STATUS_201_CREATED)


@app.route(constants.ENDPOINT_LIST + "/<string:item_id>", methods=["DELETE"])
def delete_list_item(item_id):
    item_to_remove = next(
        (item for item in sample_data.sample_list if item["id"] == item_id),
        None,
    )
    if item_to_remove is None:
        json_response = flask.jsonify(
            {"error": "Could not find an item with the given id"}
        )
        return flask.make_response(json_response, constants.HTTP_STATUS_404_NOT_FOUND)
    sample_data.sample_list.remove(item_to_remove)
    return flask.jsonify({"id": item_id, "text": "This comment was deleted"})


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
