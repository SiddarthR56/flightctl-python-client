# coding: utf-8

"""
    Flight Control API

    [Flight Control](https://flightctl.io) is a service for declarative management of fleets of edge devices and their workloads. 

    The version of the OpenAPI document: v1alpha1
    Contact: team@flightctl.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.devices_summary import DevicesSummary

class TestDevicesSummary(unittest.TestCase):
    """DevicesSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DevicesSummary:
        """Test DevicesSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DevicesSummary`
        """
        model = DevicesSummary()
        if include_optional:
            return DevicesSummary(
                total = 56,
                application_status = {
                    'key' : 56
                    },
                summary_status = {
                    'key' : 56
                    },
                update_status = {
                    'key' : 56
                    }
            )
        else:
            return DevicesSummary(
                total = 56,
                application_status = {
                    'key' : 56
                    },
                summary_status = {
                    'key' : 56
                    },
                update_status = {
                    'key' : 56
                    },
        )
        """

    def testDevicesSummary(self):
        """Test DevicesSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
