# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cpu_resource_monitor_spec import CPUResourceMonitorSpec

class TestCPUResourceMonitorSpec(unittest.TestCase):
    """CPUResourceMonitorSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CPUResourceMonitorSpec:
        """Test CPUResourceMonitorSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CPUResourceMonitorSpec`
        """
        model = CPUResourceMonitorSpec()
        if include_optional:
            return CPUResourceMonitorSpec(
                monitor_type = '',
                alert_rules = [
                    openapi_client.models.resource_alert_rule.ResourceAlertRule(
                        severity = 'Warning', 
                        duration = '4s', 
                        percentage = 1.337, 
                        description = '', )
                    ],
                sampling_interval = '68072888001528021798096225500h'
            )
        else:
            return CPUResourceMonitorSpec(
                monitor_type = '',
                alert_rules = [
                    openapi_client.models.resource_alert_rule.ResourceAlertRule(
                        severity = 'Warning', 
                        duration = '4s', 
                        percentage = 1.337, 
                        description = '', )
                    ],
                sampling_interval = '68072888001528021798096225500h',
        )
        """

    def testCPUResourceMonitorSpec(self):
        """Test CPUResourceMonitorSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
