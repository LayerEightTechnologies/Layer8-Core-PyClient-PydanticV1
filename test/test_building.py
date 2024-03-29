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

from openapi_client.models.building import Building  # noqa: E501

class TestBuilding(unittest.TestCase):
    """Building unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Building:
        """Test Building
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Building`
        """
        model = Building()  # noqa: E501
        if include_optional:
            return Building(
                id = 56,
                building_name = '',
                building_code = '',
                postcode = '',
                building_operator = 56,
                account_manager = '',
                coordinate = openapi_client.models.building_coordinate.building_coordinate(
                    type = '', 
                    coordinates = [
                        1.337
                        ], ),
                home_account = '',
                wifi_id = '',
                created_at = '',
                last_updated = '',
                rooms_count = 56,
                live_tenancies_count = 56
            )
        else:
            return Building(
                building_name = '',
                building_code = '',
                building_operator = 56,
        )
        """

    def testBuilding(self):
        """Test Building"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
