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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class BuildingOperator(BaseModel):
    """
    NOTE --- The values provided in the customer_type_id array OVERWRITE and do not merge with existing values ---  # noqa: E501
    """
    id: Optional[StrictInt] = Field(None, alias="Id")
    operator_name: StrictStr = Field(...)
    operator_description: Optional[StrictStr] = None
    operator_code: StrictStr = Field(...)
    customer_type_id: Optional[conlist(StrictInt)] = None
    created_at: Optional[StrictStr] = None
    last_updated: Optional[StrictStr] = None
    __properties = ["Id", "operator_name", "operator_description", "operator_code", "customer_type_id", "created_at", "last_updated"]

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
    def from_json(cls, json_str: str) -> BuildingOperator:
        """Create an instance of BuildingOperator from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BuildingOperator:
        """Create an instance of BuildingOperator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BuildingOperator.parse_obj(obj)

        _obj = BuildingOperator.parse_obj({
            "id": obj.get("Id"),
            "operator_name": obj.get("operator_name"),
            "operator_description": obj.get("operator_description"),
            "operator_code": obj.get("operator_code"),
            "customer_type_id": obj.get("customer_type_id"),
            "created_at": obj.get("created_at"),
            "last_updated": obj.get("last_updated")
        })
        return _obj

