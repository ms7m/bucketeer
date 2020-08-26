
from bucketeer.objects.key import Key
from bucketeer.objects.service import Service

def test_weight_generation():
    _EXPECTED = [
        "Key1",
        "Key1",
        "Key1",
        "Key2"
    ]

    _counted = 0
    _generate_key = Key("Key1", weight=3)
    
    assert Service("TestService", [_generate_key, Key("Key2", 1)]).raw_key_list == _EXPECTED
