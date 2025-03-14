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

from flightctl.models.enrollment_config import EnrollmentConfig

class TestEnrollmentConfig(unittest.TestCase):
    """EnrollmentConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnrollmentConfig:
        """Test EnrollmentConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnrollmentConfig`
        """
        model = EnrollmentConfig()
        if include_optional:
            return EnrollmentConfig(
                enrollment_service = flightctl.models.enrollment_service.EnrollmentService(
                    authentication = flightctl.models.enrollment_service_auth.EnrollmentServiceAuth(
                        client_certificate_data = '', 
                        client_key_data = '', ), 
                    service = flightctl.models.enrollment_service_service.EnrollmentServiceService(
                        certificate_authority_data = '', 
                        server = '', ), 
                    enrollment_ui_endpoint = '', )
            )
        else:
            return EnrollmentConfig(
                enrollment_service = flightctl.models.enrollment_service.EnrollmentService(
                    authentication = flightctl.models.enrollment_service_auth.EnrollmentServiceAuth(
                        client_certificate_data = '', 
                        client_key_data = '', ), 
                    service = flightctl.models.enrollment_service_service.EnrollmentServiceService(
                        certificate_authority_data = '', 
                        server = '', ), 
                    enrollment_ui_endpoint = '', ),
        )
        """

    def testEnrollmentConfig(self):
        """Test EnrollmentConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
