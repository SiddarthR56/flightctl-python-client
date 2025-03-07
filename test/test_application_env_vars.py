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

from flightctl.models.application_env_vars import ApplicationEnvVars

class TestApplicationEnvVars(unittest.TestCase):
    """ApplicationEnvVars unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationEnvVars:
        """Test ApplicationEnvVars
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationEnvVars`
        """
        model = ApplicationEnvVars()
        if include_optional:
            return ApplicationEnvVars(
                env_vars = {
                    'key' : ''
                    }
            )
        else:
            return ApplicationEnvVars(
        )
        """

    def testApplicationEnvVars(self):
        """Test ApplicationEnvVars"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
