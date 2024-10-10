from pymongo.collection import Collection



def test_collection(accidents_db: Collection):
    res = list(accidents_db.find({}))
    assert len(res) == 20000
