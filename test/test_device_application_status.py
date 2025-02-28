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

from flightctl.models.device_application_status import DeviceApplicationStatus

class TestDeviceApplicationStatus(unittest.TestCase):
    """DeviceApplicationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceApplicationStatus:
        """Test DeviceApplicationStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceApplicationStatus`
        """
        model = DeviceApplicationStatus()
        if include_optional:
            return DeviceApplicationStatus(
                name = '',
                ready = '',
                restarts = 56,
                status = 'Preparing'
            )
        else:
            return DeviceApplicationStatus(
                name = '',
                ready = '',
                restarts = 56,
                status = 'Preparing',
        )
        """

    def testDeviceApplicationStatus(self):
        """Test DeviceApplicationStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
