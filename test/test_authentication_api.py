# coding: utf-8

"""
    Flight Control API

    [Flight Control](https://github.com/flightctl/flightctl) is a service for declarative management of fleets of edge devices and their workloads. 

    The version of the OpenAPI document: v1alpha1
    Contact: team@flightctl.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.api.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthenticationApi()

    def tearDown(self) -> None:
        pass

    def test_auth_config(self) -> None:
        """Test case for auth_config

        """
        pass

    def test_auth_validate(self) -> None:
        """Test case for auth_validate

        """
        pass


if __name__ == '__main__':
    unittest.main()
