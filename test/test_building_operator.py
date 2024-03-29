# coding: utf-8

"""
    Wavenet Connected API

    Provides a primary resource for buildings, room tenancies for Wavenet connected customers, includes other information such as VLAN information and addresses

    The version of the OpenAPI document: 2.5.x
    Contact: development@wavenetuk.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.building_operator import BuildingOperator  # noqa: E501

class TestBuildingOperator(unittest.TestCase):
    """BuildingOperator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuildingOperator:
        """Test BuildingOperator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuildingOperator`
        """
        model = BuildingOperator()  # noqa: E501
        if include_optional:
            return BuildingOperator(
                id = 56,
                operator_name = '',
                operator_description = '',
                operator_code = '',
                customer_type_id = [
                    56
                    ],
                created_at = '',
                last_updated = ''
            )
        else:
            return BuildingOperator(
                operator_name = '',
                operator_code = '',
        )
        """

    def testBuildingOperator(self):
        """Test BuildingOperator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
