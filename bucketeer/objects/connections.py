
from bucketeer.objects.key import Key


class Connection:
    """ Base object to be inherited for custom connections """
    
    def _add_counter_to_key(self, key: str, service: str) -> bool:
        raise NotImplemented

    def _remove_counter_to_key(self, key:str, service: str) -> bool:
        raise NotImplemented 

    def get_lowest_used_key(self, service: str) -> dict:
        raise NotImplemented