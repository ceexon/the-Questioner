from App.api.v1.views.user_views import api_v1, time_now
from App.api.v1.models.models import Meetups
import datetime
from flask import Blueprint, request, jsonify, make_response


@api_v1.route('/meetups', methods=["POST"])
def add_meetup():
    data = request.get_json()
    try:
        if not data:
            return jsonify({"status": 204, "error": "no data found"}), 204
        if not data["topic"]:
            return jsonify({"status": 422, "error": "Topic is required"}), 422
        if not data["location"]:
            return jsonify({"status": 422, "error": "Location is required"}), 422
        if not data["happenOn"]:
            return jsonify({"status": 422, "error": "hapenOn is required"}), 422

    except:
        return jsonify({"status": 400, "error": "Some necessary field is missing in your data"}), 400

    new_meetup = {}
    for key in data:
        new_meetup[key] = data[key]

    new_meetup["createOn"] = time_now.strftime("%D")
    latest_met = Meetups[-1]
    new_id = latest_met["id"]
    new_meetup["id"] = new_id+1

    Meetups.append(new_meetup)
    return jsonify({"status": 201, "data": new_meetup}), 201


@api_v1.route('/meetups', methods=['GET'])
def get_all_meetups():
    return jsonify({"data": Meetups, "status": 200}), 200


@api_v1.route('/meetups/<meet_id>', methods=['GET'])
def get_single_meetups(meet_id):
    try:
        m_id = int(meet_id)

    except:
        return jsonify({"status": 400, "error": "invalid meetup id, use int"}), 400

    for meet in Meetups:
        if meet["id"] == m_id:
            return jsonify({"status": 200, "data": meet}), 200

    return jsonify({"status": 404, "error": "Meetup not found"}), 404
