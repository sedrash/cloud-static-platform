from flask import Blueprint, jsonify, render_template
from app.services.content_service import content_service

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def home():
    return render_template("index.html")


@main_blueprint.route("/healthz")
def healthz():
    return jsonify({"status": "healthy"}), 200


@main_blueprint.route("/readyz")
def readyz():
    return jsonify({"status": "ready"}), 200


@main_blueprint.route("/api/events")
def events():
    data = content_service.get_content("events")
    # On s'assure que le JSON contient la clé 'items' pour le test
    return jsonify({
        "category": "events",
        "items": data.get("events", []) # On extrait la liste depuis 'events'
    }), 200

@main_blueprint.route("/api/news")
def news():
    return jsonify(content_service.get_content("news")), 200


@main_blueprint.route("/api/faq")
def faq():
    return jsonify(content_service.get_content("faq")), 200