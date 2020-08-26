

from typing import Counter
from bucketeer.objects.key import Key
from bucketeer.objects.service import Service
from bucketeer.helpers.convert_dict_lookup_struct import _convert_to_dict_lookup_structure


def test_convert_to_dict_lookup_structure():
    sample =  [
        Service("test", [
            Key(
                "test1",
            ),
            Key(
                "test2",
                3
            )
        ])
    ]
    

    expected_test_1_key_count = 1
    expected_test_2_key_count = 3

    run_function = _convert_to_dict_lookup_structure(sample)
    

    _counter = {}

    for item in list(run_function['services']["test"]['lookup'].keys()):
        selected_item = run_function['services']['test']['lookup'][item]
        if selected_item in _counter:
            _counter[selected_item] += 1
        else:
            _counter[selected_item] = 1
    
    assert _counter["test1"] == expected_test_1_key_count
    assert _counter['test2'] == expected_test_2_key_count
        