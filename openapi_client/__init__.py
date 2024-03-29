# coding: utf-8

# flake8: noqa

"""
    Wavenet Connected API

    Provides a primary resource for buildings, room tenancies for Wavenet connected customers, includes other information such as VLAN information and addresses

    The version of the OpenAPI document: 2.5.x
    Contact: development@wavenetuk.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.default_api import DefaultApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.building import Building
from openapi_client.models.building_coordinate import BuildingCoordinate
from openapi_client.models.building_operator import BuildingOperator
from openapi_client.models.put_building_operator_request import PutBuildingOperatorRequest
from openapi_client.models.put_building_request import PutBuildingRequest
from openapi_client.models.put_room_request import PutRoomRequest
from openapi_client.models.room import Room
from openapi_client.models.tenancy import Tenancy
from openapi_client.models.update_tenancy_request import UpdateTenancyRequest
