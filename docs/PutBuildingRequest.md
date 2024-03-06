# PutBuildingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**building_name** | **str** |  | [optional] 
**building_code** | **str** |  | 
**building_operator** | **int** |  | 
**postcode** | **str** |  | 
**home_account** | **str** |  | 
**account_manager** | **str** |  | 
**wifi_id** | **str** |  | 
**status** | **str** |  | 
**description** | **str** |  | 
**go_live_date** | **date** |  | 
**address_1** | **str** |  | 

## Example

```python
from openapi_client.models.put_building_request import PutBuildingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutBuildingRequest from a JSON string
put_building_request_instance = PutBuildingRequest.from_json(json)
# print the JSON string representation of the object
print PutBuildingRequest.to_json()

# convert the object into a dict
put_building_request_dict = put_building_request_instance.to_dict()
# create an instance of PutBuildingRequest from a dict
put_building_request_form_dict = put_building_request.from_dict(put_building_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


