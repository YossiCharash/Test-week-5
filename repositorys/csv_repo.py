
import csv
from database.connect import accidents,inJuries


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row


def init_chicago_car_accidents(csv_path):
    accidents.drop()
    inJuries.drop()




    for row in read_csv(csv_path):

       inJurie = {
           'MOST_SEVERE_INJURY': row['MOST_SEVERE_INJURY'],
           'INJURIES_TOTAL': row['INJURIES_TOTAL'],
           'INJURIES_FATAL': row['INJURIES_FATAL'],
           "INJURIES_INCAPACITATING": row['INJURIES_INCAPACITATING'],
           'INJURIES_NON_INCAPACITATING': row['INJURIES_NON_INCAPACITATING'],
           'INJURIES_REPORTED_NOT_EVIDENT': row['INJURIES_REPORTED_NOT_EVIDENT'],
           'INJURIES_NO_INDICATION': row['INJURIES_NO_INDICATION'],
           "INJURIES_UNKNOWN": row['INJURIES_UNKNOWN'],
       }
       inJuries_id = inJuries.insert_one(inJurie).inserted_id


       accident = {
           'BEAT_OF_OCCURRENCE': row['BEAT_OF_OCCURRENCE'],
           "inJuries_id":inJuries_id,
           'CRASH_RECORD_ID': row['CRASH_RECORD_ID'],
           'CRASH_DATE_EST_I': row['CRASH_DATE_EST_I'],
           'POSTED_SPEED_LIMIT': row['POSTED_SPEED_LIMIT'],
           'TRAFFIC_CONTROL_DEVICE': row['TRAFFIC_CONTROL_DEVICE'],
           'DEVICE_CONDITION': row['DEVICE_CONDITION'],
           'WEATHER_CONDITION': row['WEATHER_CONDITION'],
           'LIGHTING_CONDITION': row['LIGHTING_CONDITION'],
           'FIRST_CRASH_TYPE': row['FIRST_CRASH_TYPE'],
           'TRAFFICWAY_TYPE': row['TRAFFICWAY_TYPE'],
           'LANE_CNT': row['LANE_CNT'],
           'ALIGNMENT': row['ALIGNMENT'],
           'ROAD_DEFECT': row['ROAD_DEFECT'],
           'REPORT_TYPE': row['REPORT_TYPE'],
           'ROADWAY_SURFACE_COND': row['ROADWAY_SURFACE_COND'],
           'CRASH_TYPE': row['CRASH_TYPE'],
           'INTERSECTION_RELATED_I': row['INTERSECTION_RELATED_I'],
           'NOT_RIGHT_OF_WAY_I': row['NOT_RIGHT_OF_WAY_I'],
           'HIT_AND_RUN_I': row['HIT_AND_RUN_I'],
           'DAMAGE': row['DAMAGE'],
           'DATE_POLICE_NOTIFIED': row['DATE_POLICE_NOTIFIED'],
           'PRIM_CONTRIBUTORY_CAUSE': row['PRIM_CONTRIBUTORY_CAUSE'],
           'SEC_CONTRIBUTORY_CAUSE': row['SEC_CONTRIBUTORY_CAUSE'],
           'CRASH_DATE': row['CRASH_DATE']
       }

       accidents.insert_one(accident)
    accidents.create_index('BEAT_OF_OCCURRENCE')
    accidents.create_index('inJuries_id')
    accidents.create_index('CRASH_DATE')

    return True











