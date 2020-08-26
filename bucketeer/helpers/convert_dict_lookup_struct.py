
import typing
import uuid

from bucketeer.objects.service import Service

def _convert_to_dict_lookup_structure(services_pased: typing.List[Service]):
    _FINAL_RESULT = {"services": {}}
    for service in services_pased:
        _FINAL_RESULT['services'][service.name] = {
            "lookup": {},
            "watch": {}
        }
        selected_service_edit = _FINAL_RESULT['services'][service.name]
        current_service = service
        for item in current_service.raw_key_list:
            generated_unique_id = str(uuid.uuid4())
            selected_service_edit["lookup"][generated_unique_id] = item
            selected_service_edit['watch'][generated_unique_id] = 0
    
    return _FINAL_RESULT