from flask import Blueprint, jsonify
from app.utils import oldleaguemanager

# Create the blueprint
api_bp = Blueprint('api', __name__)

@api_bp.route('/team/<user>', methods=['GET'])
def get_team(user):
    return jsonify([h.__dict__ for h in oldleaguemanager.main(["--league", "1229556252934164480", "--get-players", user, "--year", "2025"])]), 200