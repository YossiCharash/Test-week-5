
import csv
from datetime import datetime

from database.connect import accidents,inJuries



def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)


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
           "INJURIES": row['INJURIES_UNKNOWN'],
       }
       inJuries_id = inJuries.insert_one(inJurie).inserted_id



       accident = {
           "PRIM": row['PRIM_CONTRIBUTORY_CAUSE'],
           'BEAT_OF_OCCURRENCE': row['BEAT_OF_OCCURRENCE'],
           "inJuries_id":inJuries_id,
           'CRASH_RECORD_ID': row['CRASH_RECORD_ID'],
           'CRASH_TYPE': row['CRASH_TYPE'],
           'CRASH_DATE': parse_date(row['CRASH_DATE'])
       }

       accidents.insert_one(accident)
    accidents.create_index('BEAT_OF_OCCURRENCE')
    accidents.create_index('inJuries_id')
    accidents.create_index('CRASH_DATE')

    return True











