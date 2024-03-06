# BuildingCoordinate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from openapi_client.models.building_coordinate import BuildingCoordinate

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingCoordinate from a JSON string
building_coordinate_instance = BuildingCoordinate.from_json(json)
# print the JSON string representation of the object
print BuildingCoordinate.to_json()

# convert the object into a dict
building_coordinate_dict = building_coordinate_instance.to_dict()
# create an instance of BuildingCoordinate from a dict
building_coordinate_form_dict = building_coordinate.from_dict(building_coordinate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


