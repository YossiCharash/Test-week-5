from flask import Blueprint, jsonify
from repositorys import csv_repo as csv

Accidents = Blueprint('Accidents', __name__)


@Accidents.route('/', methods=['POST'])
def init():
    result = csv.init_chicago_car_accidents('./Traffic_Crashes_-_Crashes - 20k rows.csv')
    if result:
        return jsonify("the data is created!!!"),201
    else:
        return jsonify("the data is NOT created!!!"),400


