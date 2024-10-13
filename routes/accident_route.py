from datetime import timedelta, datetime
from flask import Blueprint, jsonify
from repositorys.csv_repo import init_chicago_car_accidents
from repositorys.result_repo import prim_contributory_cause,fetch_crash_data_by_period
from services.accidents_servic import sum_accidents_by_beats
from bson.json_util import dumps

Accidents = Blueprint('Accidents', __name__)


@Accidents.route('/', methods=['POST'])
def init():
    result = init_chicago_car_accidents('./Traffic_Crashes_-_Crashes - 20k rows.csv')
    if result:
        return jsonify("the data is created!!!"),201
    else:
        return jsonify("the data is NOT created!!!"),400


@Accidents.route('/beats/<string:beat>', methods=['GET'])
def get_accidents_by_beat(beat):
    result = sum_accidents_by_beats(str(beat))
    if result:
        return jsonify("the sum is: ",result),200
    else:
        return jsonify("the data is NOT found!!!"),404




@Accidents.route("/beat_time/<int:area>/<string:date>/<string:period>", methods=["GET"])
def get_crash_by_area_and_season(area, date,period):
    try:
        accidents = fetch_crash_data_by_period(area, date,period)
        return jsonify(accidents), 201 if accidents else 404

    except ValueError as ve:
        return jsonify({"error": f"Invalid input: {str(ve)}"}), 400



@Accidents.route('/beat/<int:beat>/<string:prim>', methods=['GET'])
def get_by_prim_contributory_cause(beat,prim):
    result = prim_contributory_cause(beat,prim)
    if type(result) is not int:
        return {"the data is NOT found!!!": str(type(result))},404

    else:
        return jsonify("the sum is: ", result), 200






