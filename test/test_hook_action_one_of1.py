# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.hook_action_one_of1 import HookActionOneOf1

class TestHookActionOneOf1(unittest.TestCase):
    """HookActionOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HookActionOneOf1:
        """Test HookActionOneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HookActionOneOf1`
        """
        model = HookActionOneOf1()
        if include_optional:
            return HookActionOneOf1(
                systemd = None
            )
        else:
            return HookActionOneOf1(
                systemd = None,
        )
        """

    def testHookActionOneOf1(self):
        """Test HookActionOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
