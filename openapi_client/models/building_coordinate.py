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


from typing import List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, conlist

class BuildingCoordinate(BaseModel):
    """
    BuildingCoordinate
    """
    type: Optional[StrictStr] = None
    coordinates: Optional[conlist(Union[StrictFloat, StrictInt])] = None
    __properties = ["type", "coordinates"]

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
    def from_json(cls, json_str: str) -> BuildingCoordinate:
        """Create an instance of BuildingCoordinate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BuildingCoordinate:
        """Create an instance of BuildingCoordinate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BuildingCoordinate.parse_obj(obj)

        _obj = BuildingCoordinate.parse_obj({
            "type": obj.get("type"),
            "coordinates": obj.get("coordinates")
        })
        return _obj

