from pymongo import MongoClient


client = MongoClient("localhost", 27017)
chicago_car_accidents = client['Chicago-Car-Accidents']

accidents = chicago_car_accidents["accidents"]
accidents_date = chicago_car_accidents['date']
inJuries = chicago_car_accidents['inJuries']
