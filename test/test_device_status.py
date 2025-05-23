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

from flightctl.models.device_status import DeviceStatus

class TestDeviceStatus(unittest.TestCase):
    """DeviceStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceStatus:
        """Test DeviceStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceStatus`
        """
        model = DeviceStatus()
        if include_optional:
            return DeviceStatus(
                conditions = [
                    flightctl.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ],
                system_info = {
                    'key' : ''
                    },
                applications = [
                    flightctl.models.device_application_status.DeviceApplicationStatus(
                        name = '', 
                        ready = '', 
                        restarts = 56, 
                        status = 'Preparing', )
                    ],
                applications_summary = flightctl.models.device_applications_summary_status.DeviceApplicationsSummaryStatus(
                    status = 'Healthy', 
                    info = '', ),
                resources = flightctl.models.device_resource_status.DeviceResourceStatus(
                    cpu = 'Healthy', 
                    memory = 'Healthy', 
                    disk = 'Healthy', ),
                integrity = flightctl.models.device_integrity_status.DeviceIntegrityStatus(
                    status = 'Passed', 
                    info = '', ),
                config = flightctl.models.device_config_status.DeviceConfigStatus(
                    rendered_version = '', ),
                os = flightctl.models.device_os_status.DeviceOsStatus(
                    image = '', 
                    image_digest = '', ),
                updated = flightctl.models.device_updated_status.DeviceUpdatedStatus(
                    status = 'UpToDate', 
                    info = '', ),
                summary = flightctl.models.device_summary_status.DeviceSummaryStatus(
                    status = 'Online', 
                    info = '', ),
                last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                lifecycle = flightctl.models.device_lifecycle_status.DeviceLifecycleStatus(
                    status = 'Unknown', 
                    info = '', )
            )
        else:
            return DeviceStatus(
                conditions = [
                    flightctl.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ],
                system_info = {
                    'key' : ''
                    },
                applications = [
                    flightctl.models.device_application_status.DeviceApplicationStatus(
                        name = '', 
                        ready = '', 
                        restarts = 56, 
                        status = 'Preparing', )
                    ],
                applications_summary = flightctl.models.device_applications_summary_status.DeviceApplicationsSummaryStatus(
                    status = 'Healthy', 
                    info = '', ),
                resources = flightctl.models.device_resource_status.DeviceResourceStatus(
                    cpu = 'Healthy', 
                    memory = 'Healthy', 
                    disk = 'Healthy', ),
                integrity = flightctl.models.device_integrity_status.DeviceIntegrityStatus(
                    status = 'Passed', 
                    info = '', ),
                config = flightctl.models.device_config_status.DeviceConfigStatus(
                    rendered_version = '', ),
                os = flightctl.models.device_os_status.DeviceOsStatus(
                    image = '', 
                    image_digest = '', ),
                updated = flightctl.models.device_updated_status.DeviceUpdatedStatus(
                    status = 'UpToDate', 
                    info = '', ),
                summary = flightctl.models.device_summary_status.DeviceSummaryStatus(
                    status = 'Online', 
                    info = '', ),
                last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                lifecycle = flightctl.models.device_lifecycle_status.DeviceLifecycleStatus(
                    status = 'Unknown', 
                    info = '', ),
        )
        """

    def testDeviceStatus(self):
        """Test DeviceStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
