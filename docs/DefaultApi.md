# openapi_client.DefaultApi

All URIs are relative to *http://localhost:3000/v2.5.6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_buildings**](DefaultApi.md#bulk_create_buildings) | **POST** /buildings/bulk | 
[**bulk_create_rooms**](DefaultApi.md#bulk_create_rooms) | **POST** /rooms/bulk | 
[**create_building**](DefaultApi.md#create_building) | **POST** /buildings | 
[**create_building_operator**](DefaultApi.md#create_building_operator) | **POST** /operators | 
[**create_room**](DefaultApi.md#create_room) | **POST** /rooms | 
[**create_tenancy**](DefaultApi.md#create_tenancy) | **POST** /tenancies | 
[**delete_building**](DefaultApi.md#delete_building) | **DELETE** /buildings/{id} | 
[**delete_building_operator**](DefaultApi.md#delete_building_operator) | **DELETE** /operators/{id} | 
[**delete_room**](DefaultApi.md#delete_room) | **DELETE** /rooms/{id} | 
[**delete_tenancy**](DefaultApi.md#delete_tenancy) | **DELETE** /tenancies/{id} | 
[**get_building_by_id**](DefaultApi.md#get_building_by_id) | **GET** /buildings/{id} | 
[**get_building_operator_by_id**](DefaultApi.md#get_building_operator_by_id) | **GET** /operators/{id} | 
[**get_building_operator_with_buildings**](DefaultApi.md#get_building_operator_with_buildings) | **GET** /operators/{id}/withbuildings | 
[**get_building_operators**](DefaultApi.md#get_building_operators) | **GET** /operators | 
[**get_building_operators_with_buildings**](DefaultApi.md#get_building_operators_with_buildings) | **GET** /operators/withbuildings | 
[**get_building_with_associations**](DefaultApi.md#get_building_with_associations) | **GET** /buildings/{id}/withassociations | 
[**get_building_with_operator**](DefaultApi.md#get_building_with_operator) | **GET** /buildings/{id}/withoperator | 
[**get_building_with_rooms**](DefaultApi.md#get_building_with_rooms) | **GET** /buildings/{id}/withrooms | 
[**get_buildings**](DefaultApi.md#get_buildings) | **GET** /buildings | 
[**get_buildings_tenancy_history**](DefaultApi.md#get_buildings_tenancy_history) | **GET** /buildings/{id}/history | 
[**get_buildings_with_associations**](DefaultApi.md#get_buildings_with_associations) | **GET** /buildings/withassociations | 
[**get_buildings_with_operator**](DefaultApi.md#get_buildings_with_operator) | **GET** /buildings/withoperator | 
[**get_buildings_with_rooms**](DefaultApi.md#get_buildings_with_rooms) | **GET** /buildings/withrooms | 
[**get_room_by_id**](DefaultApi.md#get_room_by_id) | **GET** /rooms/{id} | 
[**get_room_with_associations**](DefaultApi.md#get_room_with_associations) | **GET** /rooms/{id}/withassociations | 
[**get_room_with_tenancies**](DefaultApi.md#get_room_with_tenancies) | **GET** /rooms/{id}/withtenancies | 
[**get_rooms**](DefaultApi.md#get_rooms) | **GET** /rooms | 
[**get_rooms_with_associations**](DefaultApi.md#get_rooms_with_associations) | **GET** /rooms/withassociations | 
[**get_rooms_with_building**](DefaultApi.md#get_rooms_with_building) | **GET** /rooms/withbuilding | 
[**get_rooms_with_building_0**](DefaultApi.md#get_rooms_with_building_0) | **GET** /rooms/{id}/withbuilding | 
[**get_rooms_with_tenancies**](DefaultApi.md#get_rooms_with_tenancies) | **GET** /rooms/withtenancies | 
[**get_tenancies**](DefaultApi.md#get_tenancies) | **GET** /tenancies | 
[**get_tenancies_with_associations**](DefaultApi.md#get_tenancies_with_associations) | **GET** /tenancies/withassociations | 
[**get_tenancies_with_room**](DefaultApi.md#get_tenancies_with_room) | **GET** /tenancies/withroom | 
[**get_tenancy_by_id**](DefaultApi.md#get_tenancy_by_id) | **GET** /tenancies/{id} | 
[**get_tenancy_with_associations**](DefaultApi.md#get_tenancy_with_associations) | **GET** /tenancies/{id}/withassociations | 
[**get_tenancy_with_room**](DefaultApi.md#get_tenancy_with_room) | **GET** /tenancies/{id}/withroom | 
[**put_building**](DefaultApi.md#put_building) | **PUT** /buildings/{id} | 
[**put_building_operator**](DefaultApi.md#put_building_operator) | **PUT** /operators/{id} | 
[**put_room**](DefaultApi.md#put_room) | **PUT** /rooms/{id} | 
[**update_building**](DefaultApi.md#update_building) | **PATCH** /buildings/{id} | 
[**update_building_operator**](DefaultApi.md#update_building_operator) | **PATCH** /operators/{id} | 
[**update_room**](DefaultApi.md#update_room) | **PATCH** /rooms/{id} | 
[**update_tenancy**](DefaultApi.md#update_tenancy) | **PUT** /tenancies/{id} | 
[**update_tenancy_0**](DefaultApi.md#update_tenancy_0) | **PATCH** /tenancies/{id} | 


# **bulk_create_buildings**
> object bulk_create_buildings(building)



Create buildings in bulk

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.building import Building
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    building = [{"building_name":"Cadburys Factory","building_code":"FWEF","postcode":"LN2 4GW","building_operator":4,"account_manager":"John Doe","coordinate":{"type":"Point","coordinates":[40.717274,74.0089606]},"home_account":"BYA","wifi_id":"GR1"},{"building_name":"Carters Hall","building_code":"TRSE","postcode":"CT40 3RE","building_operator":3,"account_manager":"John Doe","coordinate":{"type":"Point","coordinates":[15.4332522,20.4958329]},"home_account":"REAE","wifi_id":"RE22"}] # Building | 

    try:
        api_response = api_instance.bulk_create_buildings(building)
        print("The response of DefaultApi->bulk_create_buildings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_create_buildings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building** | [**Building**](Building.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully bulk created buildings |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_rooms**
> object bulk_create_rooms(room)



Creates rooms in bulk

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.room import Room
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    room = [{"building_id":9,"room_number":"AT.C01","area_squarefeet":5353},{"building_id":9,"room_number":"AT.C01","area_squarefeet":1240}] # Room | 

    try:
        api_response = api_instance.bulk_create_rooms(room)
        print("The response of DefaultApi->bulk_create_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_create_rooms: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room** | [**Room**](Room.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully bulk created rooms |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_building**
> object create_building(building)



Create a single Building

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.building import Building
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    building = {"building_name":"Redkiln House","building_code":"EGH33","building_operator":23,"postcode":"RE22 3FE","go_live_date":"2023-12-14","account_manager":"John Doe","coordinate":{"type":"Point","coordinates":[15.4332522,20.4958329]},"home_account":"DE11","wifi_id":"VRRE2"} # Building | 

    try:
        api_response = api_instance.create_building(building)
        print("The response of DefaultApi->create_building:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_building: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building** | [**Building**](Building.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_building_operator**
> object create_building_operator(building_operator)



Create a new building operator

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.building_operator import BuildingOperator
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    building_operator = {"operator_name":"Workspace Group","operator_description":"Office space landlord","operator_code":"owg","customer_type_id":[123,1234,12356]} # BuildingOperator | 

    try:
        api_response = api_instance.create_building_operator(building_operator)
        print("The response of DefaultApi->create_building_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_building_operator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_operator** | [**BuildingOperator**](BuildingOperator.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a building operator |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room**
> object create_room(room)



Create a new room

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.room import Room
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    room = {"building_id":9,"room_number":"AT.C01","area_squarefeet":1240} # Room | 

    try:
        api_response = api_instance.create_room(room)
        print("The response of DefaultApi->create_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room** | [**Room**](Room.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a room |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenancy**
> object create_tenancy(tenancy)



Create a new Tenancy

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tenancy import Tenancy
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenancy = {"room_id":1,"tenant_id":"EET2","start_date":"2021-12-10","end_date":"2022-01-04","start_source":"API","end_source":"API"} # Tenancy | 

    try:
        api_response = api_instance.create_tenancy(tenancy)
        print("The response of DefaultApi->create_tenancy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_tenancy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenancy** | [**Tenancy**](Tenancy.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a tenancy |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_building**
> object delete_building(id)



Delete a single Building

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.delete_building(id)
        print("The response of DefaultApi->delete_building:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_building: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted a building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_building_operator**
> object delete_building_operator(id)



Delete a building operator

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.delete_building_operator(id)
        print("The response of DefaultApi->delete_building_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_building_operator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted a building operator |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room**
> object delete_room(id)



Delete a single Room

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.delete_room(id)
        print("The response of DefaultApi->delete_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted a room |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenancy**
> object delete_tenancy(id)



Delete a single tenancy

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.delete_tenancy(id)
        print("The response of DefaultApi->delete_tenancy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_tenancy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted a tenancy |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_by_id**
> object get_building_by_id(id, fields=fields)



View a single building by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    fields = 'field_name1, field_name2' # str | List which fields names are to be included in the response (comma seperated) (optional) (default to 'field_name1, field_name2')

    try:
        api_response = api_instance.get_building_by_id(id, fields=fields)
        print("The response of DefaultApi->get_building_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_building_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **fields** | **str**| List which fields names are to be included in the response (comma seperated) | [optional] [default to &#39;field_name1, field_name2&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_operator_by_id**
> object get_building_operator_by_id(id, fields=fields)



View a single Building Operator by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    fields = 'field_name1, field_name2' # str | List which fields names are to be included in the response (comma seperated) (optional) (default to 'field_name1, field_name2')

    try:
        api_response = api_instance.get_building_operator_by_id(id, fields=fields)
        print("The response of DefaultApi->get_building_operator_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_building_operator_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **fields** | **str**| List which fields names are to be included in the response (comma seperated) | [optional] [default to &#39;field_name1, field_name2&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a building operator |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_operator_with_buildings**
> object get_building_operator_with_buildings(id)



View an operator with its associated buildings

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.get_building_operator_with_buildings(id)
        print("The response of DefaultApi->get_building_operator_with_buildings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_building_operator_with_buildings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an operator with its associated buildings |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_operators**
> object get_building_operators(page_size=page_size, page=page, order_by=order_by, fields=fields, search_all_fields=search_all_fields, id=id, operator_name=operator_name, operator_code=operator_code, operator_description=operator_description, customer_type_id=customer_type_id, last_updated=last_updated)



Returns a list of building operators

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    fields = 'field_name1, field_name2' # str | List which fields names are to be included in the response (comma seperated) (optional) (default to 'field_name1, field_name2')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    operator_name = 'Workspace' # str | Enter a full or portion of an operator name (optional) (default to 'Workspace')
    operator_code = 'ong' # str | Enter a full or portion of an operator code (optional) (default to 'ong')
    operator_description = 'operator_description_example' # str | Enter a full or portion of an operator description (optional)
    customer_type_id = 1 # int | Enter an integer to filter operators by their customer_type_id (optional) (default to 1)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_building_operators(page_size=page_size, page=page, order_by=order_by, fields=fields, search_all_fields=search_all_fields, id=id, operator_name=operator_name, operator_code=operator_code, operator_description=operator_description, customer_type_id=customer_type_id, last_updated=last_updated)
        print("The response of DefaultApi->get_building_operators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_building_operators: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **fields** | **str**| List which fields names are to be included in the response (comma seperated) | [optional] [default to &#39;field_name1, field_name2&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **operator_name** | **str**| Enter a full or portion of an operator name | [optional] [default to &#39;Workspace&#39;]
 **operator_code** | **str**| Enter a full or portion of an operator code | [optional] [default to &#39;ong&#39;]
 **operator_description** | **str**| Enter a full or portion of an operator description | [optional] 
 **customer_type_id** | **int**| Enter an integer to filter operators by their customer_type_id | [optional] [default to 1]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of building operators |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_operators_with_buildings**
> object get_building_operators_with_buildings(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, operator_name=operator_name, operator_code=operator_code, operator_description=operator_description, customer_type_id=customer_type_id, last_updated=last_updated)



View all building operators with their associated buildings

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    operator_name = 'Workspace' # str | Enter a full or portion of an operator name (optional) (default to 'Workspace')
    operator_code = 'ong' # str | Enter a full or portion of an operator code (optional) (default to 'ong')
    operator_description = 'operator_description_example' # str | Enter a full or portion of an operator description (optional)
    customer_type_id = 1 # int | Enter an integer to filter operators by their customer_type_id (optional) (default to 1)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_building_operators_with_buildings(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, operator_name=operator_name, operator_code=operator_code, operator_description=operator_description, customer_type_id=customer_type_id, last_updated=last_updated)
        print("The response of DefaultApi->get_building_operators_with_buildings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_building_operators_with_buildings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **operator_name** | **str**| Enter a full or portion of an operator name | [optional] [default to &#39;Workspace&#39;]
 **operator_code** | **str**| Enter a full or portion of an operator code | [optional] [default to &#39;ong&#39;]
 **operator_description** | **str**| Enter a full or portion of an operator description | [optional] 
 **customer_type_id** | **int**| Enter an integer to filter operators by their customer_type_id | [optional] [default to 1]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of operators with their associated buildings |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_with_associations**
> object get_building_with_associations(id)



View a building with its associated operator and rooms

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.get_building_with_associations(id)
        print("The response of DefaultApi->get_building_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_building_with_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a building with associated operator and rooms |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_with_operator**
> object get_building_with_operator(id)



View a building with its associated operator

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.get_building_with_operator(id)
        print("The response of DefaultApi->get_building_with_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_building_with_operator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a building with its associated operator |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  * X-Powered-By -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Etag -  <br>  * Date -  <br>  * Connection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_with_rooms**
> object get_building_with_rooms(id)



View a building with its associated rooms

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.get_building_with_rooms(id)
        print("The response of DefaultApi->get_building_with_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_building_with_rooms: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a building with its associated rooms |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buildings**
> object get_buildings(page_size=page_size, page=page, order_by=order_by, fields=fields, search_all_fields=search_all_fields, id=id, building_name=building_name, building_code=building_code, building_operator=building_operator, wifi_id=wifi_id, postcode=postcode, status=status, description=description, go_live_date=go_live_date, address_1=address_1, home_account=home_account, account_manager=account_manager, created_at=created_at, last_updated=last_updated)



View all buildings

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    fields = 'field_name1, field_name2' # str | List which fields names are to be included in the response (comma seperated) (optional) (default to 'field_name1, field_name2')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    building_name = 'Street' # str | Enter a full or portion of a building name (optional) (default to 'Street')
    building_code = 'FS' # str | Enter a full or portion of a building code (optional) (default to 'FS')
    building_operator = 3 # int | Enter a building operator id (optional) (default to 3)
    wifi_id = 'ownE' # str | Enter a wifi_id (optional) (default to 'ownE')
    postcode = 'SE1' # str | Enter a full or portion of a postcode (optional) (default to 'SE1')
    status = 'Live Building' # str | Enter a full or portion of a status (optional) (default to 'Live Building')
    description = 'description_example' # str | Enter a full or portion of a description (optional)
    go_live_date = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results to match a go live date (optional)
    address_1 = 'London Road' # str | Enter a full or portion of the address (optional) (default to 'London Road')
    home_account = 'home_account_example' # str | Enter a full or portion of a home account (optional)
    account_manager = 'account_manager_example' # str | Enter a full or portion of a account manager (optional)
    created_at = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by created_at value (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_buildings(page_size=page_size, page=page, order_by=order_by, fields=fields, search_all_fields=search_all_fields, id=id, building_name=building_name, building_code=building_code, building_operator=building_operator, wifi_id=wifi_id, postcode=postcode, status=status, description=description, go_live_date=go_live_date, address_1=address_1, home_account=home_account, account_manager=account_manager, created_at=created_at, last_updated=last_updated)
        print("The response of DefaultApi->get_buildings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_buildings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **fields** | **str**| List which fields names are to be included in the response (comma seperated) | [optional] [default to &#39;field_name1, field_name2&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **building_name** | **str**| Enter a full or portion of a building name | [optional] [default to &#39;Street&#39;]
 **building_code** | **str**| Enter a full or portion of a building code | [optional] [default to &#39;FS&#39;]
 **building_operator** | **int**| Enter a building operator id | [optional] [default to 3]
 **wifi_id** | **str**| Enter a wifi_id | [optional] [default to &#39;ownE&#39;]
 **postcode** | **str**| Enter a full or portion of a postcode | [optional] [default to &#39;SE1&#39;]
 **status** | **str**| Enter a full or portion of a status | [optional] [default to &#39;Live Building&#39;]
 **description** | **str**| Enter a full or portion of a description | [optional] 
 **go_live_date** | **date**| Enter a ISO8601 formatted date to filter results to match a go live date | [optional] 
 **address_1** | **str**| Enter a full or portion of the address | [optional] [default to &#39;London Road&#39;]
 **home_account** | **str**| Enter a full or portion of a home account | [optional] 
 **account_manager** | **str**| Enter a full or portion of a account manager | [optional] 
 **created_at** | **datetime**| Enter a ISO8601 DateTime to filter by created_at value | [optional] 
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of buildings |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buildings_tenancy_history**
> object get_buildings_tenancy_history(id, active_tenancies=active_tenancies)



View a building and its associated rooms and tenancies

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    active_tenancies = True # bool | Filter tenancies to either active or inactive (optional) (default to True)

    try:
        api_response = api_instance.get_buildings_tenancy_history(id, active_tenancies=active_tenancies)
        print("The response of DefaultApi->get_buildings_tenancy_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_buildings_tenancy_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **active_tenancies** | **bool**| Filter tenancies to either active or inactive | [optional] [default to True]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a building with its rooms and tenancy history |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buildings_with_associations**
> object get_buildings_with_associations(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_name=building_name, building_code=building_code, building_operator=building_operator, wifi_id=wifi_id, postcode=postcode, status=status, description=description, go_live_date=go_live_date, address_1=address_1, account_manager=account_manager, home_account=home_account, created_at=created_at, last_updated=last_updated)



View all buildings with their associated operator and rooms

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    building_name = 'Street' # str | Enter a full or portion of a building name (optional) (default to 'Street')
    building_code = 'FS' # str | Enter a full or portion of a building code (optional) (default to 'FS')
    building_operator = 3 # int | Enter a building operator id (optional) (default to 3)
    wifi_id = 'ownE' # str | Enter a wifi_id (optional) (default to 'ownE')
    postcode = 'SE1' # str | Enter a full or portion of a postcode (optional) (default to 'SE1')
    status = 'Live Building' # str | Enter a full or portion of a status (optional) (default to 'Live Building')
    description = 'description_example' # str | Enter a full or portion of a description (optional)
    go_live_date = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results to match a go live date (optional)
    address_1 = 'London Road' # str | Enter a full or portion of the address (optional) (default to 'London Road')
    account_manager = 'account_manager_example' # str | Enter a full or portion of a account manager (optional)
    home_account = 'home_account_example' # str | Enter a full or portion of a home account (optional)
    created_at = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by created_at value (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_buildings_with_associations(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_name=building_name, building_code=building_code, building_operator=building_operator, wifi_id=wifi_id, postcode=postcode, status=status, description=description, go_live_date=go_live_date, address_1=address_1, account_manager=account_manager, home_account=home_account, created_at=created_at, last_updated=last_updated)
        print("The response of DefaultApi->get_buildings_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_buildings_with_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **building_name** | **str**| Enter a full or portion of a building name | [optional] [default to &#39;Street&#39;]
 **building_code** | **str**| Enter a full or portion of a building code | [optional] [default to &#39;FS&#39;]
 **building_operator** | **int**| Enter a building operator id | [optional] [default to 3]
 **wifi_id** | **str**| Enter a wifi_id | [optional] [default to &#39;ownE&#39;]
 **postcode** | **str**| Enter a full or portion of a postcode | [optional] [default to &#39;SE1&#39;]
 **status** | **str**| Enter a full or portion of a status | [optional] [default to &#39;Live Building&#39;]
 **description** | **str**| Enter a full or portion of a description | [optional] 
 **go_live_date** | **date**| Enter a ISO8601 formatted date to filter results to match a go live date | [optional] 
 **address_1** | **str**| Enter a full or portion of the address | [optional] [default to &#39;London Road&#39;]
 **account_manager** | **str**| Enter a full or portion of a account manager | [optional] 
 **home_account** | **str**| Enter a full or portion of a home account | [optional] 
 **created_at** | **datetime**| Enter a ISO8601 DateTime to filter by created_at value | [optional] 
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned buildings with associated operator and rooms |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buildings_with_operator**
> object get_buildings_with_operator(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_name=building_name, building_code=building_code, building_operator=building_operator, wifi_id=wifi_id, postcode=postcode, status=status, description=description, go_live_date=go_live_date, address_1=address_1, home_account=home_account, account_manager=account_manager, created_at=created_at, last_updated=last_updated)



View all buildings with their associated operator

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    building_name = 'Street' # str | Enter a full or portion of a building name (optional) (default to 'Street')
    building_code = 'FS' # str | Enter a full or portion of a building code (optional) (default to 'FS')
    building_operator = 3 # int | Enter a building operator id (optional) (default to 3)
    wifi_id = 'ownE' # str | Enter a wifi_id (optional) (default to 'ownE')
    postcode = 'SE1' # str | Enter a full or portion of a postcode (optional) (default to 'SE1')
    status = 'Live Building' # str | Enter a full or portion of a status (optional) (default to 'Live Building')
    description = 'description_example' # str | Enter a full or portion of a description (optional)
    go_live_date = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results to match a go live date (optional)
    address_1 = 'London Road' # str | Enter a full or portion of the address (optional) (default to 'London Road')
    home_account = 'home_account_example' # str | Enter a full or portion of a home account (optional)
    account_manager = 'account_manager_example' # str | Enter a full or portion of a account manager (optional)
    created_at = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by created_at value (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_buildings_with_operator(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_name=building_name, building_code=building_code, building_operator=building_operator, wifi_id=wifi_id, postcode=postcode, status=status, description=description, go_live_date=go_live_date, address_1=address_1, home_account=home_account, account_manager=account_manager, created_at=created_at, last_updated=last_updated)
        print("The response of DefaultApi->get_buildings_with_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_buildings_with_operator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **building_name** | **str**| Enter a full or portion of a building name | [optional] [default to &#39;Street&#39;]
 **building_code** | **str**| Enter a full or portion of a building code | [optional] [default to &#39;FS&#39;]
 **building_operator** | **int**| Enter a building operator id | [optional] [default to 3]
 **wifi_id** | **str**| Enter a wifi_id | [optional] [default to &#39;ownE&#39;]
 **postcode** | **str**| Enter a full or portion of a postcode | [optional] [default to &#39;SE1&#39;]
 **status** | **str**| Enter a full or portion of a status | [optional] [default to &#39;Live Building&#39;]
 **description** | **str**| Enter a full or portion of a description | [optional] 
 **go_live_date** | **date**| Enter a ISO8601 formatted date to filter results to match a go live date | [optional] 
 **address_1** | **str**| Enter a full or portion of the address | [optional] [default to &#39;London Road&#39;]
 **home_account** | **str**| Enter a full or portion of a home account | [optional] 
 **account_manager** | **str**| Enter a full or portion of a account manager | [optional] 
 **created_at** | **datetime**| Enter a ISO8601 DateTime to filter by created_at value | [optional] 
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buildings_with_rooms**
> object get_buildings_with_rooms(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_name=building_name, building_code=building_code, building_operator=building_operator, wifi_id=wifi_id, postcode=postcode, status=status, description=description, go_live_date=go_live_date, address_1=address_1, home_account=home_account, account_manager=account_manager, created_at=created_at, last_updated=last_updated)



View buildings with their associated rooms

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    building_name = 'Street' # str | Enter a full or portion of a building name (optional) (default to 'Street')
    building_code = 'FS' # str | Enter a full or portion of a building code (optional) (default to 'FS')
    building_operator = 3 # int | Enter a building operator id (optional) (default to 3)
    wifi_id = 'ownE' # str | Enter a wifi_id (optional) (default to 'ownE')
    postcode = 'SE1' # str | Enter a full or portion of a postcode (optional) (default to 'SE1')
    status = 'Live Building' # str | Enter a full or portion of a status (optional) (default to 'Live Building')
    description = 'description_example' # str | Enter a full or portion of a description (optional)
    go_live_date = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results to match a go live date (optional)
    address_1 = 'London Road' # str | Enter a full or portion of the address (optional) (default to 'London Road')
    home_account = 'home_account_example' # str | Enter a full or portion of a home account (optional)
    account_manager = 'account_manager_example' # str | Enter a full or portion of a account manager (optional)
    created_at = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by created_at value (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_buildings_with_rooms(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_name=building_name, building_code=building_code, building_operator=building_operator, wifi_id=wifi_id, postcode=postcode, status=status, description=description, go_live_date=go_live_date, address_1=address_1, home_account=home_account, account_manager=account_manager, created_at=created_at, last_updated=last_updated)
        print("The response of DefaultApi->get_buildings_with_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_buildings_with_rooms: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **building_name** | **str**| Enter a full or portion of a building name | [optional] [default to &#39;Street&#39;]
 **building_code** | **str**| Enter a full or portion of a building code | [optional] [default to &#39;FS&#39;]
 **building_operator** | **int**| Enter a building operator id | [optional] [default to 3]
 **wifi_id** | **str**| Enter a wifi_id | [optional] [default to &#39;ownE&#39;]
 **postcode** | **str**| Enter a full or portion of a postcode | [optional] [default to &#39;SE1&#39;]
 **status** | **str**| Enter a full or portion of a status | [optional] [default to &#39;Live Building&#39;]
 **description** | **str**| Enter a full or portion of a description | [optional] 
 **go_live_date** | **date**| Enter a ISO8601 formatted date to filter results to match a go live date | [optional] 
 **address_1** | **str**| Enter a full or portion of the address | [optional] [default to &#39;London Road&#39;]
 **home_account** | **str**| Enter a full or portion of a home account | [optional] 
 **account_manager** | **str**| Enter a full or portion of a account manager | [optional] 
 **created_at** | **datetime**| Enter a ISO8601 DateTime to filter by created_at value | [optional] 
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned buildings with their associated rooms |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_by_id**
> object get_room_by_id(id, fields=fields)



View a single room by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    fields = 'field_name1, field_name2' # str | List which fields names are to be included in the response (comma seperated) (optional) (default to 'field_name1, field_name2')

    try:
        api_response = api_instance.get_room_by_id(id, fields=fields)
        print("The response of DefaultApi->get_room_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_room_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **fields** | **str**| List which fields names are to be included in the response (comma seperated) | [optional] [default to &#39;field_name1, field_name2&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a room |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_with_associations**
> object get_room_with_associations(id, active_tenancies=active_tenancies)



View a room with its associated building and tenancies

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    active_tenancies = True # bool | Filter tenancies to either active or inactive (optional) (default to True)

    try:
        api_response = api_instance.get_room_with_associations(id, active_tenancies=active_tenancies)
        print("The response of DefaultApi->get_room_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_room_with_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **active_tenancies** | **bool**| Filter tenancies to either active or inactive | [optional] [default to True]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a room with its associated building and tenancies |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_with_tenancies**
> object get_room_with_tenancies(id, active_tenancies=active_tenancies)



View a room with its associated tenancies

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    active_tenancies = True # bool | Filter tenancies to either active or inactive (optional) (default to True)

    try:
        api_response = api_instance.get_room_with_tenancies(id, active_tenancies=active_tenancies)
        print("The response of DefaultApi->get_room_with_tenancies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_room_with_tenancies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **active_tenancies** | **bool**| Filter tenancies to either active or inactive | [optional] [default to True]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a room with its associated tenancies |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms**
> object get_rooms(page_size=page_size, page=page, order_by=order_by, fields=fields, search_all_fields=search_all_fields, id=id, building_id=building_id, room_number=room_number, default_vlan=default_vlan, current_vlan=current_vlan, is_active=is_active, is_virtual=is_virtual, last_updated=last_updated)



View all rooms

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    fields = 'field_name1, field_name2' # str | List which fields names are to be included in the response (comma seperated) (optional) (default to 'field_name1, field_name2')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    building_id = 3 # int | Enter a building id (optional) (default to 3)
    room_number = 'AE' # str | Enter a room number (optional) (default to 'AE')
    default_vlan = 500 # int | Enter a default vlan (optional) (default to 500)
    current_vlan = 12 # int | Enter a current vlan (optional) (default to 12)
    is_active = True # bool | Search for active or inactive rooms (optional) (default to True)
    is_virtual = False # bool | Search for standard or virtual rooms (optional) (default to False)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_rooms(page_size=page_size, page=page, order_by=order_by, fields=fields, search_all_fields=search_all_fields, id=id, building_id=building_id, room_number=room_number, default_vlan=default_vlan, current_vlan=current_vlan, is_active=is_active, is_virtual=is_virtual, last_updated=last_updated)
        print("The response of DefaultApi->get_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_rooms: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **fields** | **str**| List which fields names are to be included in the response (comma seperated) | [optional] [default to &#39;field_name1, field_name2&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **building_id** | **int**| Enter a building id | [optional] [default to 3]
 **room_number** | **str**| Enter a room number | [optional] [default to &#39;AE&#39;]
 **default_vlan** | **int**| Enter a default vlan | [optional] [default to 500]
 **current_vlan** | **int**| Enter a current vlan | [optional] [default to 12]
 **is_active** | **bool**| Search for active or inactive rooms | [optional] [default to True]
 **is_virtual** | **bool**| Search for standard or virtual rooms | [optional] [default to False]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of rooms |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_with_associations**
> object get_rooms_with_associations(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_id=building_id, room_number=room_number, default_vlan=default_vlan, current_vlan=current_vlan, is_active=is_active, is_virtual=is_virtual, active_tenancies=active_tenancies, last_updated=last_updated)



View all rooms with their associated building and tenancies

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    building_id = 3 # int | Enter a building id (optional) (default to 3)
    room_number = 'AE' # str | Enter a room number (optional) (default to 'AE')
    default_vlan = 500 # int | Enter a default vlan (optional) (default to 500)
    current_vlan = 12 # int | Enter a current vlan (optional) (default to 12)
    is_active = True # bool | Search for active or inactive rooms (optional) (default to True)
    is_virtual = False # bool | Search for standard or virtual rooms (optional) (default to False)
    active_tenancies = True # bool | Filter tenancies to either active or inactive (optional) (default to True)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_rooms_with_associations(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_id=building_id, room_number=room_number, default_vlan=default_vlan, current_vlan=current_vlan, is_active=is_active, is_virtual=is_virtual, active_tenancies=active_tenancies, last_updated=last_updated)
        print("The response of DefaultApi->get_rooms_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_rooms_with_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **building_id** | **int**| Enter a building id | [optional] [default to 3]
 **room_number** | **str**| Enter a room number | [optional] [default to &#39;AE&#39;]
 **default_vlan** | **int**| Enter a default vlan | [optional] [default to 500]
 **current_vlan** | **int**| Enter a current vlan | [optional] [default to 12]
 **is_active** | **bool**| Search for active or inactive rooms | [optional] [default to True]
 **is_virtual** | **bool**| Search for standard or virtual rooms | [optional] [default to False]
 **active_tenancies** | **bool**| Filter tenancies to either active or inactive | [optional] [default to True]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of rooms with their associated building and tenancies |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_with_building**
> object get_rooms_with_building(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, building_id=building_id, room_number=room_number, default_vlan=default_vlan, current_vlan=current_vlan, is_active=is_active, is_virtual=is_virtual, last_updated=last_updated)



View all rooms with their associated building

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    building_id = 3 # int | Enter a building id (optional) (default to 3)
    room_number = 'AE' # str | Enter a room number (optional) (default to 'AE')
    default_vlan = 500 # int | Enter a default vlan (optional) (default to 500)
    current_vlan = 12 # int | Enter a current vlan (optional) (default to 12)
    is_active = True # bool | Search for active or inactive rooms (optional) (default to True)
    is_virtual = False # bool | Search for standard or virtual rooms (optional) (default to False)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_rooms_with_building(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, building_id=building_id, room_number=room_number, default_vlan=default_vlan, current_vlan=current_vlan, is_active=is_active, is_virtual=is_virtual, last_updated=last_updated)
        print("The response of DefaultApi->get_rooms_with_building:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_rooms_with_building: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **building_id** | **int**| Enter a building id | [optional] [default to 3]
 **room_number** | **str**| Enter a room number | [optional] [default to &#39;AE&#39;]
 **default_vlan** | **int**| Enter a default vlan | [optional] [default to 500]
 **current_vlan** | **int**| Enter a current vlan | [optional] [default to 12]
 **is_active** | **bool**| Search for active or inactive rooms | [optional] [default to True]
 **is_virtual** | **bool**| Search for standard or virtual rooms | [optional] [default to False]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned rooms with associated building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_with_building_0**
> object get_rooms_with_building_0(id)



View a room with its associated building

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.get_rooms_with_building_0(id)
        print("The response of DefaultApi->get_rooms_with_building_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_rooms_with_building_0: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a room with its associated building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_with_tenancies**
> object get_rooms_with_tenancies(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_id=building_id, room_number=room_number, default_vlan=default_vlan, current_vlan=current_vlan, is_active=is_active, is_virtual=is_virtual, active_tenancies=active_tenancies, last_updated=last_updated)



View all rooms with their associated tenancies

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    building_id = 3 # int | Enter a building id (optional) (default to 3)
    room_number = 'AE' # str | Enter a room number (optional) (default to 'AE')
    default_vlan = 500 # int | Enter a default vlan (optional) (default to 500)
    current_vlan = 12 # int | Enter a current vlan (optional) (default to 12)
    is_active = True # bool | Search for active or inactive rooms (optional) (default to True)
    is_virtual = False # bool | Search for standard or virtual rooms (optional) (default to False)
    active_tenancies = True # bool | Filter tenancies to either active or inactive (optional) (default to True)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_rooms_with_tenancies(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, building_id=building_id, room_number=room_number, default_vlan=default_vlan, current_vlan=current_vlan, is_active=is_active, is_virtual=is_virtual, active_tenancies=active_tenancies, last_updated=last_updated)
        print("The response of DefaultApi->get_rooms_with_tenancies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_rooms_with_tenancies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **building_id** | **int**| Enter a building id | [optional] [default to 3]
 **room_number** | **str**| Enter a room number | [optional] [default to &#39;AE&#39;]
 **default_vlan** | **int**| Enter a default vlan | [optional] [default to 500]
 **current_vlan** | **int**| Enter a current vlan | [optional] [default to 12]
 **is_active** | **bool**| Search for active or inactive rooms | [optional] [default to True]
 **is_virtual** | **bool**| Search for standard or virtual rooms | [optional] [default to False]
 **active_tenancies** | **bool**| Filter tenancies to either active or inactive | [optional] [default to True]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned rooms with their associated tenancies |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenancies**
> object get_tenancies(page_size=page_size, page=page, order_by=order_by, fields=fields, search_all_fields=search_all_fields, id=id, room_id=room_id, start_date=start_date, end_date=end_date, tenant_id=tenant_id, start_source=start_source, start_date_from=start_date_from, start_date_to=start_date_to, end_source=end_source, end_date_from=end_date_from, end_date_to=end_date_to, active_tenancies=active_tenancies, last_updated=last_updated)



View all tenancies

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    fields = 'field_name1, field_name2' # str | List which fields names are to be included in the response (comma seperated) (optional) (default to 'field_name1, field_name2')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    room_id = 11 # int | Enter a room id (optional) (default to 11)
    start_date = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results to match a start date (optional)
    end_date = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results to match a end date (optional)
    tenant_id = 'EEEE' # str | Enter a tenant id (optional) (default to 'EEEE')
    start_source = 'start_source_example' # str | Enter a string to filter results by a specific value (optional)
    start_date_from = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a start date value on or after the specified date (optional)
    start_date_to = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a start date value on or before the specified date (optional)
    end_source = 'end_source_example' # str | Enter a string to filter results by a specific value (optional)
    end_date_from = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a end date value on or after the specified date (optional)
    end_date_to = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a end date value on or before the specified date (optional)
    active_tenancies = True # bool | Filter tenancies to either active or inactive (optional) (default to True)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_tenancies(page_size=page_size, page=page, order_by=order_by, fields=fields, search_all_fields=search_all_fields, id=id, room_id=room_id, start_date=start_date, end_date=end_date, tenant_id=tenant_id, start_source=start_source, start_date_from=start_date_from, start_date_to=start_date_to, end_source=end_source, end_date_from=end_date_from, end_date_to=end_date_to, active_tenancies=active_tenancies, last_updated=last_updated)
        print("The response of DefaultApi->get_tenancies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tenancies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **fields** | **str**| List which fields names are to be included in the response (comma seperated) | [optional] [default to &#39;field_name1, field_name2&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **room_id** | **int**| Enter a room id | [optional] [default to 11]
 **start_date** | **date**| Enter a ISO8601 formatted date to filter results to match a start date | [optional] 
 **end_date** | **date**| Enter a ISO8601 formatted date to filter results to match a end date | [optional] 
 **tenant_id** | **str**| Enter a tenant id | [optional] [default to &#39;EEEE&#39;]
 **start_source** | **str**| Enter a string to filter results by a specific value | [optional] 
 **start_date_from** | **date**| Enter a ISO8601 formatted date to filter results that have a start date value on or after the specified date | [optional] 
 **start_date_to** | **date**| Enter a ISO8601 formatted date to filter results that have a start date value on or before the specified date | [optional] 
 **end_source** | **str**| Enter a string to filter results by a specific value | [optional] 
 **end_date_from** | **date**| Enter a ISO8601 formatted date to filter results that have a end date value on or after the specified date | [optional] 
 **end_date_to** | **date**| Enter a ISO8601 formatted date to filter results that have a end date value on or before the specified date | [optional] 
 **active_tenancies** | **bool**| Filter tenancies to either active or inactive | [optional] [default to True]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of tenancies |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenancies_with_associations**
> object get_tenancies_with_associations(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, room_id=room_id, tenant_id=tenant_id, building_id=building_id, start_source=start_source, start_date_from=start_date_from, start_date_to=start_date_to, end_source=end_source, end_date_from=end_date_from, end_date_to=end_date_to, active_tenancies=active_tenancies, last_updated=last_updated)



View all tenancies with their associated room and building

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    room_id = 11 # int | Enter a room id (optional) (default to 11)
    tenant_id = 'EEEE' # str | Enter a tenant id (optional) (default to 'EEEE')
    building_id = 3 # int | Enter a building id (optional) (default to 3)
    start_source = 'start_source_example' # str | Enter a string to filter results by a specific value (optional)
    start_date_from = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a start date value on or after the specified date (optional)
    start_date_to = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a start date value on or before the specified date (optional)
    end_source = 'end_source_example' # str | Enter a string to filter results by a specific value (optional)
    end_date_from = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a end date value on or after the specified date (optional)
    end_date_to = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a end date value on or before the specified date (optional)
    active_tenancies = True # bool | Filter tenancies to either active or inactive (optional) (default to True)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_tenancies_with_associations(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, room_id=room_id, tenant_id=tenant_id, building_id=building_id, start_source=start_source, start_date_from=start_date_from, start_date_to=start_date_to, end_source=end_source, end_date_from=end_date_from, end_date_to=end_date_to, active_tenancies=active_tenancies, last_updated=last_updated)
        print("The response of DefaultApi->get_tenancies_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tenancies_with_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **room_id** | **int**| Enter a room id | [optional] [default to 11]
 **tenant_id** | **str**| Enter a tenant id | [optional] [default to &#39;EEEE&#39;]
 **building_id** | **int**| Enter a building id | [optional] [default to 3]
 **start_source** | **str**| Enter a string to filter results by a specific value | [optional] 
 **start_date_from** | **date**| Enter a ISO8601 formatted date to filter results that have a start date value on or after the specified date | [optional] 
 **start_date_to** | **date**| Enter a ISO8601 formatted date to filter results that have a start date value on or before the specified date | [optional] 
 **end_source** | **str**| Enter a string to filter results by a specific value | [optional] 
 **end_date_from** | **date**| Enter a ISO8601 formatted date to filter results that have a end date value on or after the specified date | [optional] 
 **end_date_to** | **date**| Enter a ISO8601 formatted date to filter results that have a end date value on or before the specified date | [optional] 
 **active_tenancies** | **bool**| Filter tenancies to either active or inactive | [optional] [default to True]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of tenancies with their associated room and building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenancies_with_room**
> object get_tenancies_with_room(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, tenant_id=tenant_id, room_id=room_id, start_source=start_source, start_date_from=start_date_from, start_date_to=start_date_to, end_source=end_source, end_date_from=end_date_from, end_date_to=end_date_to, active_tenancies=active_tenancies, last_updated=last_updated)



View all tenancies with their associated room

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    page_size = 10 # int | Enter a quantity of items to a page. (optional) (default to 10)
    page = 1 # int | Enter the page number to be returned (optional) (default to 1)
    order_by = 'id ASC' # str | Enter a single field name followed by Ascending(ASC) or Descending (DESC) (optional) (default to 'id ASC')
    search_all_fields = 'search_all_fields_example' # str | Enter a string to filter results by a specific field (optional)
    id = 1 # int | Enter a specific record id for the given resource (optional) (default to 1)
    tenant_id = 'EEEE' # str | Enter a tenant id (optional) (default to 'EEEE')
    room_id = 11 # int | Enter a room id (optional) (default to 11)
    start_source = 'start_source_example' # str | Enter a string to filter results by a specific value (optional)
    start_date_from = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a start date value on or after the specified date (optional)
    start_date_to = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a start date value on or before the specified date (optional)
    end_source = 'end_source_example' # str | Enter a string to filter results by a specific value (optional)
    end_date_from = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a end date value on or after the specified date (optional)
    end_date_to = '2013-10-20' # date | Enter a ISO8601 formatted date to filter results that have a end date value on or before the specified date (optional)
    active_tenancies = True # bool | Filter tenancies to either active or inactive (optional) (default to True)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime | Enter a ISO8601 DateTime to filter by last_updated value (optional)

    try:
        api_response = api_instance.get_tenancies_with_room(page_size=page_size, page=page, order_by=order_by, search_all_fields=search_all_fields, id=id, tenant_id=tenant_id, room_id=room_id, start_source=start_source, start_date_from=start_date_from, start_date_to=start_date_to, end_source=end_source, end_date_from=end_date_from, end_date_to=end_date_to, active_tenancies=active_tenancies, last_updated=last_updated)
        print("The response of DefaultApi->get_tenancies_with_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tenancies_with_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Enter a quantity of items to a page. | [optional] [default to 10]
 **page** | **int**| Enter the page number to be returned | [optional] [default to 1]
 **order_by** | **str**| Enter a single field name followed by Ascending(ASC) or Descending (DESC) | [optional] [default to &#39;id ASC&#39;]
 **search_all_fields** | **str**| Enter a string to filter results by a specific field | [optional] 
 **id** | **int**| Enter a specific record id for the given resource | [optional] [default to 1]
 **tenant_id** | **str**| Enter a tenant id | [optional] [default to &#39;EEEE&#39;]
 **room_id** | **int**| Enter a room id | [optional] [default to 11]
 **start_source** | **str**| Enter a string to filter results by a specific value | [optional] 
 **start_date_from** | **date**| Enter a ISO8601 formatted date to filter results that have a start date value on or after the specified date | [optional] 
 **start_date_to** | **date**| Enter a ISO8601 formatted date to filter results that have a start date value on or before the specified date | [optional] 
 **end_source** | **str**| Enter a string to filter results by a specific value | [optional] 
 **end_date_from** | **date**| Enter a ISO8601 formatted date to filter results that have a end date value on or after the specified date | [optional] 
 **end_date_to** | **date**| Enter a ISO8601 formatted date to filter results that have a end date value on or before the specified date | [optional] 
 **active_tenancies** | **bool**| Filter tenancies to either active or inactive | [optional] [default to True]
 **last_updated** | **datetime**| Enter a ISO8601 DateTime to filter by last_updated value | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of tenancies with their associated room |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenancy_by_id**
> object get_tenancy_by_id(id, fields=fields)



View a single tenancy by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    fields = 'field_name1, field_name2' # str | List which fields names are to be included in the response (comma seperated) (optional) (default to 'field_name1, field_name2')

    try:
        api_response = api_instance.get_tenancy_by_id(id, fields=fields)
        print("The response of DefaultApi->get_tenancy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tenancy_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **fields** | **str**| List which fields names are to be included in the response (comma seperated) | [optional] [default to &#39;field_name1, field_name2&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a tenancy |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenancy_with_associations**
> object get_tenancy_with_associations(id)



View a tenancy with its associated room and building

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.get_tenancy_with_associations(id)
        print("The response of DefaultApi->get_tenancy_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tenancy_with_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a tenancy with its associated room and building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenancy_with_room**
> object get_tenancy_with_room(id)



View a tenancy with its associated room

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)

    try:
        api_response = api_instance.get_tenancy_with_room(id)
        print("The response of DefaultApi->get_tenancy_with_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tenancy_with_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a tenancy with its associated room |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_building**
> object put_building(id, put_building_request)



Create or update building

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.put_building_request import PutBuildingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    put_building_request = openapi_client.PutBuildingRequest() # PutBuildingRequest | 

    try:
        api_response = api_instance.put_building(id, put_building_request)
        print("The response of DefaultApi->put_building:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->put_building: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **put_building_request** | [**PutBuildingRequest**](PutBuildingRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a building |  -  |
**201** | Successfully created a building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_building_operator**
> object put_building_operator(id, put_building_operator_request)



Create or update building operator

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.put_building_operator_request import PutBuildingOperatorRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    put_building_operator_request = openapi_client.PutBuildingOperatorRequest() # PutBuildingOperatorRequest | 

    try:
        api_response = api_instance.put_building_operator(id, put_building_operator_request)
        print("The response of DefaultApi->put_building_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->put_building_operator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **put_building_operator_request** | [**PutBuildingOperatorRequest**](PutBuildingOperatorRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a building operator |  -  |
**201** | Successfully created a building operator |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_room**
> object put_room(id, put_room_request)



Create or update a room

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.put_room_request import PutRoomRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    put_room_request = openapi_client.PutRoomRequest() # PutRoomRequest | 

    try:
        api_response = api_instance.put_room(id, put_room_request)
        print("The response of DefaultApi->put_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->put_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **put_room_request** | [**PutRoomRequest**](PutRoomRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a room |  -  |
**201** | Successfully created a room |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_building**
> object update_building(id, building)



Update a single building

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.building import Building
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    building = {"building_name":"China Works","building_code":"SB","status":"Live Building"} # Building | 

    try:
        api_response = api_instance.update_building(id, building)
        print("The response of DefaultApi->update_building:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_building: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **building** | [**Building**](Building.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a building |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_building_operator**
> object update_building_operator(id, building_operator)



Update a single Building Operator

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.building_operator import BuildingOperator
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    building_operator = {"operator_code":"onw"} # BuildingOperator | 

    try:
        api_response = api_instance.update_building_operator(id, building_operator)
        print("The response of DefaultApi->update_building_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_building_operator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **building_operator** | [**BuildingOperator**](BuildingOperator.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a building operator |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_room**
> object update_room(id, room)



Updates a single Room

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.room import Room
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    room = {"current_vlan":532,"is_active":true} # Room | 

    try:
        api_response = api_instance.update_room(id, room)
        print("The response of DefaultApi->update_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **room** | [**Room**](Room.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a room |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenancy**
> object update_tenancy(id, update_tenancy_request)



Update or create a single Tenancy

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.update_tenancy_request import UpdateTenancyRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    update_tenancy_request = openapi_client.UpdateTenancyRequest() # UpdateTenancyRequest | 

    try:
        api_response = api_instance.update_tenancy(id, update_tenancy_request)
        print("The response of DefaultApi->update_tenancy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_tenancy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **update_tenancy_request** | [**UpdateTenancyRequest**](UpdateTenancyRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a tenancy |  -  |
**201** | Successfully created a new tenancy |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenancy_0**
> object update_tenancy_0(id, tenancy)



Update a single Tenancy

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tenancy import Tenancy
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/v2.5.6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000/v2.5.6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 1 # int | Enter a specific record id for the given resource (default to 1)
    tenancy = {"end_date":"2022-02-04","end_source":"NOVA"} # Tenancy | 

    try:
        api_response = api_instance.update_tenancy_0(id, tenancy)
        print("The response of DefaultApi->update_tenancy_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_tenancy_0: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enter a specific record id for the given resource | [default to 1]
 **tenancy** | [**Tenancy**](Tenancy.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a tenancy |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

