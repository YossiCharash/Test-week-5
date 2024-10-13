import pytest
from pymongo import MongoClient
from pymongo.synchronous.collection import Collection
from repositorys.result_repo import prim_contributory_cause


@pytest.fixture
def init_db():
    client = MongoClient('localhost', 27017)
    chicago_car_accidents = client['Chicago-Car-Accidents']
    yield chicago_car_accidents



@pytest.fixture
def accidents_db(init_db):
    return init_db['accidents']

@pytest.fixture
def inJuries_db(init_db):
    return init_db['inJuries']




def test_accidents(accidents_db: Collection):
    res = list(accidents_db.find({}))
    assert len(res) == 20000

def test_inJuries(inJuries_db: Collection):
    res = list(inJuries_db.find({}))
    assert len(res) == 20000

def test_prim(accidents_db: Collection):
    res = list(accidents_db.find({"PRIM":"FAILING TO REDUCE SPEED TO AVOID CRASH"}))
    assert len(res) == 795

def test_prim_contributory_cause():
    result = prim_contributory_cause('225', 'UNABLE TO DETERMINE')
    assert result == 96
