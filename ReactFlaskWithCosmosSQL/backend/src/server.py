import http
import os

import flask
import sql.service
import sample_data

PORT = os.environ.get("PORT", 3001)
ENDPOINT_MASTER_DETAIL = "/api/masterdetail"
ENDPOINT_LIST = "/api/list"
ENDPOINT_GRID = "/api/grid"

app = flask.Flask(__name__, static_folder="build")

# MasterDetail Page Endpoint
@app.route(ENDPOINT_MASTER_DETAIL)
def get_master_detail():
    return flask.jsonify(sample_data.sample_orders)


# List Endpoints
@app.route(ENDPOINT_LIST)
def get_list():
    return flask.jsonify(sql.service.get())


@app.route(ENDPOINT_LIST, methods=["POST"])
def add_list_item():
    json_response = flask.jsonify(sql.service.create())
    return flask.make_response(json_response, http.HTTPStatus.CREATED)


@app.route(ENDPOINT_LIST + "/<item_id>", methods=["DELETE"])
def delete_list_item(item_id):
    try:
        removed_item = flask.jsonify(sql.service.delete(item_id))
        return removed_item
    except ValueError as ex:
        err_response = flask.jsonify({"error": str(ex)})
        return flask.make_response(err_response, http.HTTPStatus.NOT_FOUND)


# Grid Page Endpoint
@app.route(ENDPOINT_GRID)
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
@app.errorhandler(http.HTTPStatus.NOT_FOUND.value)
def page_not_found():
    json_response = flask.jsonify({"error": "Page not found"})
    return flask.make_response(json_response, http.HTTPStatus.NOT_FOUND)


if __name__ == "__main__":
    app.run(port=PORT)
