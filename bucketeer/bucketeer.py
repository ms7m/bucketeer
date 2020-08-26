
from bucketeer.objects import key
from bucketeer.objects import service
import typing
from loguru import logger

from bucketeer.objects.connections import Connection
from bucketeer.objects.returned_key import ReturnedKey



class Bucketeer(object):
    def __init__(self, initialized_connection: typing.Type[Connection]):
        assert isinstance(initialized_connection, Connection), f"Invalid object passed as initalized connection."

        self._initalized_connection = initialized_connection
        
    @property
    def passed_object(self) -> Connection:
        return self._initalized_connection


class BucketeerContext(object):
    def __init__(self, bucketeer_object: Bucketeer, service_needed: str):
        assert isinstance(bucketeer_object, Bucketeer), "A valid bucketeer object is required."
        self._object = bucketeer_object
        self._selected_service = service_needed

        self._current_key = None

    def __enter__(self):
        try:
            try_latest_key_from_obj =  self._object.passed_object.get_lowest_used_key(service=self._selected_service)
            if try_latest_key_from_obj == False:
                logger.error("Unable to retireve latest key..")
                return None
        
            self._current_key = try_latest_key_from_obj
            return ReturnedKey(
                key_value=try_latest_key_from_obj['_key'],
                key_watcher_amount=try_latest_key_from_obj['_amt'],
                service=try_latest_key_from_obj['_ser']
            )
        except Exception:
            logger.exception("Unable to grab latest key due to unhandled error.")
            return None
    
    def __exit__(self, type, value, traceback):
        attempt_removal = self._object.passed_object._remove_counter_to_key(key=self._current_key, service=self._selected_service)
        #logger.info(f"Removal: {attempt_removal}")
        



