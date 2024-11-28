from flask import Blueprint, request, jsonify
from firebase import db

history_blueprint = Blueprint('history', __name__)

@history_blueprint.route('/', methods=['GET'])
def get_history():
    audit_results = db.collection('auditResults').stream()
    results = [{**doc.to_dict(), "id": doc.id} for doc in audit_results]
    return jsonify(results), 200
