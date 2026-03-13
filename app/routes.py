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
    # Sécurité : on s'assure d'extraire une liste pour la clé 'items'
    if isinstance(data, dict):
        items = data.get("events", [])
    else:
        items = data
        
    return jsonify({
        "category": "events",
        "items": items
    }), 200
