from datetime import datetime

from database.connect import accidents




def accidents_by_beats(beat):
    accidents_by_beat = list(accidents.find({'BEAT_OF_OCCURRENCE':str(beat)}))
    return accidents_by_beat


def data_by_dates(start,end,beat):
    n_st = start.strftime('%Y-%m-%d')
    n_ed = end.strftime('%Y-%m-%d')
    accidents_by_beat = list(accidents.find({"BEAT_OF_OCCURRENCE":beat},{'date': {'gte': n_st, 'lt': n_ed}}))
    return accidents_by_beat




def prim_contributory_cause(prim,beat):
    try:
        accidents_by_prim = list(accidents.find({'PRIM_CONTRIBUTORY_CAUSE':prim,"BEAT_OF_OCCURRENCE":str(beat)}))
        print(accidents_by_prim)
        return accidents_by_prim
    except Exception as e:
        return e

def aaa(area,start_date,end_date):
    accidents.crashes.count_documents({
        "BEAT_OF_OCCURRENCE": area,
        "DATE": {"$gte": start_date, "$lt": end_date}
    })


prim_contributory_cause("FAILING TO REDUCE SPEED TO AVOID CRASH","225")