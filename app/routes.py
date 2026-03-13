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
    # Sécurité : on s'assure d'extraire une liste
    items = data.get("events", []) if isinstance(data, dict) else data
    return jsonify({
        "category": "events",
        "items": items
    }), 200

@main_blueprint.route("/api/news")
def news():
    data = content_service.get_content("news")
    return jsonify(data), 200

@main_blueprint.route("/api/faq")
def faq():
    data = content_service.get_content("faq")
    return jsonify(data), 200
