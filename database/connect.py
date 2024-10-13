from pymongo import MongoClient
from pymongo import MongoClient

def get_db():
    """
    connect to local MongoDb
    :return:
    """
    client = MongoClient('localhost', 27017)
    db = client.test_week_5 # create database
    return client, db

client = MongoClient("localhost", 27017)
chicago_car_accidents = client['Chicago-Car-Accidents']

accidents = chicago_car_accidents["accidents"]
accidents_date = chicago_car_accidents['date']
inJuries = chicago_car_accidents['inJuries']
