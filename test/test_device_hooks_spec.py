# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.device_hooks_spec import DeviceHooksSpec

class TestDeviceHooksSpec(unittest.TestCase):
    """DeviceHooksSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceHooksSpec:
        """Test DeviceHooksSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceHooksSpec`
        """
        model = DeviceHooksSpec()
        if include_optional:
            return DeviceHooksSpec(
                before_updating = [
                    openapi_client.models.device_update_hook_spec.DeviceUpdateHookSpec(
                        name = '', 
                        description = '', 
                        actions = [
                            openapi_client.models.hook_action.HookAction()
                            ], 
                        on_file = [
                            'Create'
                            ], 
                        path = '', )
                    ],
                after_updating = [
                    openapi_client.models.device_update_hook_spec.DeviceUpdateHookSpec(
                        name = '', 
                        description = '', 
                        actions = [
                            openapi_client.models.hook_action.HookAction()
                            ], 
                        on_file = [
                            'Create'
                            ], 
                        path = '', )
                    ],
                before_rebooting = [
                    openapi_client.models.device_reboot_hook_spec.DeviceRebootHookSpec(
                        name = '', 
                        description = '', 
                        actions = [
                            openapi_client.models.hook_action.HookAction()
                            ], )
                    ],
                after_rebooting = [
                    openapi_client.models.device_reboot_hook_spec.DeviceRebootHookSpec(
                        name = '', 
                        description = '', 
                        actions = [
                            openapi_client.models.hook_action.HookAction()
                            ], )
                    ]
            )
        else:
            return DeviceHooksSpec(
        )
        """

    def testDeviceHooksSpec(self):
        """Test DeviceHooksSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
