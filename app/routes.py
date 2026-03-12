from flask import Blueprint, jsonify

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def home():
    return "Cloud Static Platform"


@main_blueprint.route("/healthz")
def healthz():
    return jsonify({"status": "ok"})


@main_blueprint.route("/readyz")
def readyz():
    return jsonify({"status": "ready"})


@main_blueprint.route("/api/events")
def events():
    return jsonify({"events": []})


@main_blueprint.route("/api/news")
def news():
    return jsonify({"news": []})


@main_blueprint.route("/api/faq")
def faq():
    return jsonify({"faq": []})
