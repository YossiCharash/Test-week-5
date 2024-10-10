from datetime import datetime
from repositorys.result_repo import accidents_by_beats,data_by_dates


def sum_accidents_by_beats(beat):
    result = len(accidents_by_beats(str(beat)))
    print(result)
    return result




def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)



# def sum_accidents_by_beat_and_date(start,end,beat):
#     n_start =  parse_date(date)
#     n_end = parse_date(date)
#     domoy()
#     result = data_by_dates(n_date,beat)
#     print(len(result))
#     return len(result)
#
# sum_accidents_by_beat_and_date("09/20/2022 18:00","225")
# sum_accidents_by_beats("225")
