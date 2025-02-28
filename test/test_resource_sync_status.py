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

from flightctl.models.resource_sync_status import ResourceSyncStatus

class TestResourceSyncStatus(unittest.TestCase):
    """ResourceSyncStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceSyncStatus:
        """Test ResourceSyncStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceSyncStatus`
        """
        model = ResourceSyncStatus()
        if include_optional:
            return ResourceSyncStatus(
                observed_commit = '',
                observed_generation = 56,
                conditions = [
                    flightctl.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ]
            )
        else:
            return ResourceSyncStatus(
                conditions = [
                    flightctl.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ],
        )
        """

    def testResourceSyncStatus(self):
        """Test ResourceSyncStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
