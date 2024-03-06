# coding: utf-8

"""
    Wavenet Connected API

    Provides a primary resource for buildings, room tenancies for Wavenet connected customers, includes other information such as VLAN information and addresses

    The version of the OpenAPI document: 2.5.x
    Contact: development@wavenetuk.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class PutBuildingOperatorRequest(BaseModel):
    """
    PutBuildingOperatorRequest
    """
    id: StrictInt = Field(...)
    operator_name: StrictStr = Field(...)
    operator_description: StrictStr = Field(...)
    operator_code: StrictStr = Field(...)
    customer_type_id: conlist(StrictInt) = Field(...)
    __properties = ["id", "operator_name", "operator_description", "operator_code", "customer_type_id"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PutBuildingOperatorRequest:
        """Create an instance of PutBuildingOperatorRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PutBuildingOperatorRequest:
        """Create an instance of PutBuildingOperatorRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PutBuildingOperatorRequest.parse_obj(obj)

        _obj = PutBuildingOperatorRequest.parse_obj({
            "id": obj.get("id"),
            "operator_name": obj.get("operator_name"),
            "operator_description": obj.get("operator_description"),
            "operator_code": obj.get("operator_code"),
            "customer_type_id": obj.get("customer_type_id")
        })
        return _obj

