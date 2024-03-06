# PutRoomRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**room_number** | **str** |  | 
**building_id** | **int** |  | 
**area_squarefeet** | **int** |  | 
**current_vlan** | **int** |  | 
**is_active** | **bool** |  | 
**is_virtual** | **bool** |  | 

## Example

```python
from openapi_client.models.put_room_request import PutRoomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutRoomRequest from a JSON string
put_room_request_instance = PutRoomRequest.from_json(json)
# print the JSON string representation of the object
print PutRoomRequest.to_json()

# convert the object into a dict
put_room_request_dict = put_room_request_instance.to_dict()
# create an instance of PutRoomRequest from a dict
put_room_request_form_dict = put_room_request.from_dict(put_room_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


