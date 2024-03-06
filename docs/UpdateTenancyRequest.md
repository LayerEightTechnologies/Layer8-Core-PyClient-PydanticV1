# UpdateTenancyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**tenant_id** | **str** |  | 
**room_id** | **int** |  | 
**start_date** | **date** |  | 
**end_date** | **date** |  | 
**start_source** | **str** |  | 
**end_source** | **str** |  | 

## Example

```python
from openapi_client.models.update_tenancy_request import UpdateTenancyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenancyRequest from a JSON string
update_tenancy_request_instance = UpdateTenancyRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTenancyRequest.to_json()

# convert the object into a dict
update_tenancy_request_dict = update_tenancy_request_instance.to_dict()
# create an instance of UpdateTenancyRequest from a dict
update_tenancy_request_form_dict = update_tenancy_request.from_dict(update_tenancy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


