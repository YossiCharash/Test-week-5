from datetime import timedelta, datetime

from flask import Blueprint, jsonify
from repositorys.csv_repo import init_chicago_car_accidents
from repositorys.result_repo import prim_contributory_cause,aaa
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


@Accidents.route('/beats/<int:beat>', methods=['GET'])
def get_accidents_by_beat(beat):
    result = sum_accidents_by_beats(beat)
    if result:
        return dumps(result),200
    else:
        return jsonify("the data is NOT found!!!"),404


# @Accidents.route('/beats/<string:beat>/<string:period>/<string:date>', methods=['GET'])
# def get_sum_accidents_by_beat_and_date(beat, date,period):
#     try:
#         result = sum_accidents_by_beat_and_date(date, beat, period)
#
#         if result:
#             return dumps({'total_accidents': result}), 200
#         else:
#             return jsonify({"error": "No data found for the specified beat and date!"}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 404

@Accidents.route("/beat_time/<area>/<date>/time=<int:period>", methods=["GET"])
def sum_crash_by_area_time(area, date, period):
    try:
        area = int(area)
        time_periods = {
            "day": 1,
            "week": 7,
            "month": 30
        }

        add_date = time_periods.get(period)
        if add_date is None:
            return jsonify({"error": "Invalid time period. Use 'day', 'week', or 'month'."}), 400

        start_date = datetime.strptime(date, '%m-%d-%Y')
        end_date = start_date + timedelta(days=add_date)

        total_crashes = aaa(area, start_date, end_date)

        return jsonify({
            "start_date": start_date,
            "end_date": end_date,
            "area": area,
            "period": period,
            "total_crashes": total_crashes
        }), 200

    except ValueError as ve:
        return jsonify({"error": f"Invalid input: {str(ve)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500





@Accidents.route('/beat/<int:beat>/<string:prim>', methods=['GET'])
def get_by_prim_contributory_cause(beat,prim):
    result = prim_contributory_cause(beat,prim)
    if result:
        return dumps(result),200
    else:
        return jsonify("the data is NOT found!!!"),404





