# Building


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**building_name** | **str** |  | 
**building_code** | **str** |  | 
**postcode** | **str** |  | [optional] 
**building_operator** | **int** |  | 
**account_manager** | **str** |  | [optional] 
**coordinate** | [**BuildingCoordinate**](BuildingCoordinate.md) |  | [optional] 
**home_account** | **str** |  | [optional] 
**wifi_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**rooms_count** | **int** |  | [optional] 
**live_tenancies_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.building import Building

# TODO update the JSON string below
json = "{}"
# create an instance of Building from a JSON string
building_instance = Building.from_json(json)
# print the JSON string representation of the object
print Building.to_json()

# convert the object into a dict
building_dict = building_instance.to_dict()
# create an instance of Building from a dict
building_form_dict = building.from_dict(building_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


