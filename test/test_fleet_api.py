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

from flightctl.api.fleet_api import FleetApi


class TestFleetApi(unittest.TestCase):
    """FleetApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FleetApi()

    def tearDown(self) -> None:
        pass

    def test_create_fleet(self) -> None:
        """Test case for create_fleet

        """
        pass

    def test_delete_fleet(self) -> None:
        """Test case for delete_fleet

        """
        pass

    def test_delete_fleets(self) -> None:
        """Test case for delete_fleets

        """
        pass

    def test_delete_template_version(self) -> None:
        """Test case for delete_template_version

        """
        pass

    def test_delete_template_versions(self) -> None:
        """Test case for delete_template_versions

        """
        pass

    def test_list_fleets(self) -> None:
        """Test case for list_fleets

        """
        pass

    def test_list_template_versions(self) -> None:
        """Test case for list_template_versions

        """
        pass

    def test_patch_fleet(self) -> None:
        """Test case for patch_fleet

        """
        pass

    def test_patch_fleet_status(self) -> None:
        """Test case for patch_fleet_status

        """
        pass

    def test_read_fleet(self) -> None:
        """Test case for read_fleet

        """
        pass

    def test_read_fleet_status(self) -> None:
        """Test case for read_fleet_status

        """
        pass

    def test_read_template_version(self) -> None:
        """Test case for read_template_version

        """
        pass

    def test_replace_fleet(self) -> None:
        """Test case for replace_fleet

        """
        pass

    def test_replace_fleet_status(self) -> None:
        """Test case for replace_fleet_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
