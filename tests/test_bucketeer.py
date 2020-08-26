import pytest
from bucketeer.bucketeer import Bucketeer
from bucketeer.objects.connections import Connection


class TestConnection(Connection):
    pass

class FalseConnection:
    pass

def test_if_init_will_accept_valid_object():
    assert Bucketeer(TestConnection())

def test_if_init_will_deny_invalid_object():
    with pytest.raises(AssertionError):
        Bucketeer(FalseConnection())
