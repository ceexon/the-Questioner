from flask import Blueprint, request, jsonify
import datetime
from App.api.v1.models.models import User

time_now = datetime.datetime.now()

api_v1 = Blueprint('api', __name__)


@api_v1.route('/signup', methods=['POST'])
def user_signup():
    data = request.get_json()
    try:
        if not data:
            return jsonify({"status": 204, "error": "no data found"}), 204
        if not data["firstName"]:
            return jsonify({"status": 422, "error": "first name is required"}), 422
        if not data["lastName"]:
            return jsonify({"status": 422, "error": "last name is required"}), 422
        if not data["email"]:
            return jsonify({"status": 422, "error": "email is required"}), 422
        if not data["phone"]:
            return jsonify({"status": 422, "error": "phoone number is required"}), 422
        if not data["password"]:
            return jsonify({"status": 422, "error": "password is required"}), 422
        if not data["confirmPassword"]:
            return jsonify({"status": 422, "error": "Please confirm ppassword"}), 422

    except:
        return jsonify({"status": 400, "error": "Some necessary field is missing in your data"}), 400

    new_user = {}
    for key in data:
        new_user[key] = data[key]

    latest_user = User[-1]
    user_id = latest_user["id"]
    new_user["id"] = user_id + 1
    new_user["isAdmin"] = False
    new_user["regDate"] = time_now.strftime("%D")

    User.append(new_user)
    return jsonify({"status": 201, "data": [new_user]}), 201


@api_v1.route('/login', methods=["POST"])
def user_login():
    data = request.get_json()
    try:
        if not data:
            return jsonify({"status": 204, "error": "no data found"}), 204
        if not data["userlog"]:
            return jsonify({"status": 422, "error": "email is required"}), 422
        if not data["password"]:
            return jsonify({"status": 422, "error": "password is required"}), 422

    except:
        return jsonify({"status": 400, "error": "Some necessary field is missing in your data"}), 400

    users = []
    for user in User:
        users.append(user["userName"])
        users.append(user["email"])

    if data["userlog"] in users:
        return jsonify({"data": "logged in success"}), 200

    return jsonify({"error": "user not found"}), 401
