# Tenancy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**room_id** | **int** |  | 
**tenant_id** | **str** |  | 
**roomid** | **int** |  | [optional] 
**start_date** | **date** |  | 
**end_date** | **date** |  | [optional] 
**start_source** | **str** |  | 
**end_source** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenancy import Tenancy

# TODO update the JSON string below
json = "{}"
# create an instance of Tenancy from a JSON string
tenancy_instance = Tenancy.from_json(json)
# print the JSON string representation of the object
print Tenancy.to_json()

# convert the object into a dict
tenancy_dict = tenancy_instance.to_dict()
# create an instance of Tenancy from a dict
tenancy_form_dict = tenancy.from_dict(tenancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


