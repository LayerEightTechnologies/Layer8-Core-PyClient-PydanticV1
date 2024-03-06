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

from openapi_client.models.put_building_request import PutBuildingRequest  # noqa: E501

class TestPutBuildingRequest(unittest.TestCase):
    """PutBuildingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PutBuildingRequest:
        """Test PutBuildingRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PutBuildingRequest`
        """
        model = PutBuildingRequest()  # noqa: E501
        if include_optional:
            return PutBuildingRequest(
                id = 56,
                building_name = '',
                building_code = '',
                building_operator = 56,
                postcode = '',
                home_account = '',
                account_manager = '',
                wifi_id = '',
                status = '',
                description = '',
                go_live_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                address_1 = ''
            )
        else:
            return PutBuildingRequest(
                id = 56,
                building_code = '',
                building_operator = 56,
                postcode = '',
                home_account = '',
                account_manager = '',
                wifi_id = '',
                status = '',
                description = '',
                go_live_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                address_1 = '',
        )
        """

    def testPutBuildingRequest(self):
        """Test PutBuildingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()