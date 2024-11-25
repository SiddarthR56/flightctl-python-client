# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.hook_action_systemd_spec import HookActionSystemdSpec

class TestHookActionSystemdSpec(unittest.TestCase):
    """HookActionSystemdSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HookActionSystemdSpec:
        """Test HookActionSystemdSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HookActionSystemdSpec`
        """
        model = HookActionSystemdSpec()
        if include_optional:
            return HookActionSystemdSpec(
                timeout = '68072888001528021798096225500h',
                unit = openapi_client.models.hook_action_systemd_unit.HookActionSystemdUnit(
                    name = '', 
                    operations = [
                        'Enable'
                        ], 
                    work_dir = '', )
            )
        else:
            return HookActionSystemdSpec(
                unit = openapi_client.models.hook_action_systemd_unit.HookActionSystemdUnit(
                    name = '', 
                    operations = [
                        'Enable'
                        ], 
                    work_dir = '', ),
        )
        """

    def testHookActionSystemdSpec(self):
        """Test HookActionSystemdSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
