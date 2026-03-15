from flask import Blueprint, jsonify
from app.utils import oldleaguemanager

# Create the blueprint
api_bp = Blueprint('api', __name__)

@api_bp.route('/multiply/<int:num>', methods=['GET'])
def multiply_number(num):
    """
    Multiplies the provided integer by 2.
    Type hinting in the route (<int:num>) handles basic validation.
    """
    result = num * 2
    
    return jsonify({
        "input": num,
        "result": result,
        "operation": "multiplication",
        "factor": 2
    }), 200

@api_bp.route('/team/<user>', methods=['GET'])
def get_team(user):
    return jsonify(oldleaguemanager.main(["--league", "1229556252934164480", "--get-players", user, "--year", 2025])), 200