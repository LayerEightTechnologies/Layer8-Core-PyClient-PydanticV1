# PutBuildingOperatorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**operator_name** | **str** |  | 
**operator_description** | **str** |  | 
**operator_code** | **str** |  | 
**customer_type_id** | **List[int]** |  | 

## Example

```python
from openapi_client.models.put_building_operator_request import PutBuildingOperatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutBuildingOperatorRequest from a JSON string
put_building_operator_request_instance = PutBuildingOperatorRequest.from_json(json)
# print the JSON string representation of the object
print PutBuildingOperatorRequest.to_json()

# convert the object into a dict
put_building_operator_request_dict = put_building_operator_request_instance.to_dict()
# create an instance of PutBuildingOperatorRequest from a dict
put_building_operator_request_form_dict = put_building_operator_request.from_dict(put_building_operator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


