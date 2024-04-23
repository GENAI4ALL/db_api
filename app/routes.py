from flask import Blueprint, request, jsonify
from .models import BoroughCount

main = Blueprint('main', __name__)

@main.route('/boroughs')
def boroughs():
    boro_list = BoroughCount.query.all()
    boros = []
    for boro in boro_list:
        boros.append({"borough": boro.borough, "total": boro.total})
    return jsonify(boros)
