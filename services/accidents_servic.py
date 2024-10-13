from datetime import datetime
from repositorys.result_repo import accidents_by_beats


def sum_accidents_by_beats(beat):
    result = len(accidents_by_beats(beat))
    print(beat," ", result)
    return result
sum_accidents_by_beats("255")






