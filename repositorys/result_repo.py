from datetime import datetime, timedelta

from bson import ObjectId

from database.connect import accidents

# accidents = "accidents"
# inJuries = 'inJuries'



def accidents_by_beats(beat):
    # client,db = get_db()
    accidents_beat = list(accidents.find({'BEAT_OF_OCCURRENCE':beat},{'_id': 0}))
    print(accidents_beat)
    return accidents_beat

print(accidents_by_beats("255"))

def data_by_dates(start,end,beat):
    n_st = start.strftime('%Y-%m-%d')
    n_ed = end.strftime('%Y-%m-%d')
    accidents_by_beat = list(accidents.find({"BEAT_OF_OCCURRENCE":beat},{'date': {'gte': n_st, 'lt': n_ed}}))
    return accidents_by_beat




def prim_contributory_cause(beat,prim):
    try:
        accidents_by_prim = accidents.count_documents({'PRIM': prim, "BEAT_OF_OCCURRENCE": str(beat)})
        return accidents_by_prim
    except Exception as e:
        return e




def fetch_crash_data_by_period(area, date, range_search):
    time_periods = {
        "day": 1,
        "week": 7,
        "month": 30
    }

    add_date = time_periods[range_search]
    print(add_date)

    start_date = datetime.strptime(date, '%m-%d-%Y')
    end_date = start_date + timedelta(days=add_date)

    sum_crash = accidents.count_documents(
        {'BEAT_OF_OCCURRENCE': area,
         "CRASH_DATE": {"$gte": start_date, "$lt": end_date}})
    print(sum_crash)
    result = {
        "start_date": start_date,
        "end_date": end_date,
        "area": area,
        "range_search": range_search,
        "total_crashes": sum_crash
    }
    return result


