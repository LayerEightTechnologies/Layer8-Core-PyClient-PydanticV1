# BuildingOperator

NOTE --- The values provided in the customer_type_id array OVERWRITE and do not merge with existing values ---

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**operator_name** | **str** |  | 
**operator_description** | **str** |  | [optional] 
**operator_code** | **str** |  | 
**customer_type_id** | **List[int]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.building_operator import BuildingOperator

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingOperator from a JSON string
building_operator_instance = BuildingOperator.from_json(json)
# print the JSON string representation of the object
print BuildingOperator.to_json()

# convert the object into a dict
building_operator_dict = building_operator_instance.to_dict()
# create an instance of BuildingOperator from a dict
building_operator_form_dict = building_operator.from_dict(building_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


