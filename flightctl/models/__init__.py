# coding: utf-8

# flake8: noqa
"""
    Flight Control API

    [Flight Control](https://github.com/flightctl/flightctl) is a service for declarative management of fleets of edge devices and their workloads. 

    The version of the OpenAPI document: v1alpha1
    Contact: team@flightctl.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from flightctl.models.application_env_vars import ApplicationEnvVars
from flightctl.models.application_spec import ApplicationSpec
from flightctl.models.application_status_type import ApplicationStatusType
from flightctl.models.applications_summary_status_type import ApplicationsSummaryStatusType
from flightctl.models.auth_config import AuthConfig
from flightctl.models.batch import Batch
from flightctl.models.batch_limit import BatchLimit
from flightctl.models.batch_sequence import BatchSequence
from flightctl.models.cpu_resource_monitor_spec import CPUResourceMonitorSpec
from flightctl.models.certificate_signing_request import CertificateSigningRequest
from flightctl.models.certificate_signing_request_list import CertificateSigningRequestList
from flightctl.models.certificate_signing_request_spec import CertificateSigningRequestSpec
from flightctl.models.certificate_signing_request_status import CertificateSigningRequestStatus
from flightctl.models.condition import Condition
from flightctl.models.condition_status import ConditionStatus
from flightctl.models.condition_type import ConditionType
from flightctl.models.config_provider_spec import ConfigProviderSpec
from flightctl.models.custom_resource_monitor_spec import CustomResourceMonitorSpec
from flightctl.models.device import Device
from flightctl.models.device_application_status import DeviceApplicationStatus
from flightctl.models.device_applications_summary_status import DeviceApplicationsSummaryStatus
from flightctl.models.device_config_status import DeviceConfigStatus
from flightctl.models.device_console import DeviceConsole
from flightctl.models.device_decommission import DeviceDecommission
from flightctl.models.device_decommission_target_type import DeviceDecommissionTargetType
from flightctl.models.device_integrity_status import DeviceIntegrityStatus
from flightctl.models.device_integrity_status_summary import DeviceIntegrityStatusSummary
from flightctl.models.device_integrity_status_summary_type import DeviceIntegrityStatusSummaryType
from flightctl.models.device_lifecycle_hook_type import DeviceLifecycleHookType
from flightctl.models.device_lifecycle_status import DeviceLifecycleStatus
from flightctl.models.device_lifecycle_status_type import DeviceLifecycleStatusType
from flightctl.models.device_list import DeviceList
from flightctl.models.device_os_spec import DeviceOSSpec
from flightctl.models.device_os_status import DeviceOSStatus
from flightctl.models.device_resource_status import DeviceResourceStatus
from flightctl.models.device_resource_status_type import DeviceResourceStatusType
from flightctl.models.device_spec import DeviceSpec
from flightctl.models.device_spec_systemd import DeviceSpecSystemd
from flightctl.models.device_status import DeviceStatus
from flightctl.models.device_summary_status import DeviceSummaryStatus
from flightctl.models.device_summary_status_type import DeviceSummaryStatusType
from flightctl.models.device_system_info import DeviceSystemInfo
from flightctl.models.device_update_policy_spec import DeviceUpdatePolicySpec
from flightctl.models.device_updated_status import DeviceUpdatedStatus
from flightctl.models.device_updated_status_type import DeviceUpdatedStatusType
from flightctl.models.devices_summary import DevicesSummary
from flightctl.models.disk_resource_monitor_spec import DiskResourceMonitorSpec
from flightctl.models.disruption_allowance import DisruptionAllowance
from flightctl.models.enrollment_config import EnrollmentConfig
from flightctl.models.enrollment_request import EnrollmentRequest
from flightctl.models.enrollment_request_approval import EnrollmentRequestApproval
from flightctl.models.enrollment_request_list import EnrollmentRequestList
from flightctl.models.enrollment_request_spec import EnrollmentRequestSpec
from flightctl.models.enrollment_request_status import EnrollmentRequestStatus
from flightctl.models.enrollment_service import EnrollmentService
from flightctl.models.enrollment_service_auth import EnrollmentServiceAuth
from flightctl.models.enrollment_service_service import EnrollmentServiceService
from flightctl.models.error import Error
from flightctl.models.file_operation import FileOperation
from flightctl.models.file_spec import FileSpec
from flightctl.models.fleet import Fleet
from flightctl.models.fleet_list import FleetList
from flightctl.models.fleet_rollout_status import FleetRolloutStatus
from flightctl.models.fleet_spec import FleetSpec
from flightctl.models.fleet_spec_template import FleetSpecTemplate
from flightctl.models.fleet_status import FleetStatus
from flightctl.models.generic_repo_spec import GenericRepoSpec
from flightctl.models.git_config_provider_spec import GitConfigProviderSpec
from flightctl.models.git_config_provider_spec_git_ref import GitConfigProviderSpecGitRef
from flightctl.models.hook_action import HookAction
from flightctl.models.hook_action_run import HookActionRun
from flightctl.models.hook_condition import HookCondition
from flightctl.models.hook_condition_path_op import HookConditionPathOp
from flightctl.models.http_config import HttpConfig
from flightctl.models.http_config_provider_spec import HttpConfigProviderSpec
from flightctl.models.http_config_provider_spec_http_ref import HttpConfigProviderSpecHttpRef
from flightctl.models.http_repo_spec import HttpRepoSpec
from flightctl.models.image_application_provider import ImageApplicationProvider
from flightctl.models.inline_config_provider_spec import InlineConfigProviderSpec
from flightctl.models.kubernetes_secret_provider_spec import KubernetesSecretProviderSpec
from flightctl.models.kubernetes_secret_provider_spec_secret_ref import KubernetesSecretProviderSpecSecretRef
from flightctl.models.label_selector import LabelSelector
from flightctl.models.list_meta import ListMeta
from flightctl.models.match_expression import MatchExpression
from flightctl.models.memory_resource_monitor_spec import MemoryResourceMonitorSpec
from flightctl.models.object_meta import ObjectMeta
from flightctl.models.patch_request_inner import PatchRequestInner
from flightctl.models.rendered_application_spec import RenderedApplicationSpec
from flightctl.models.rendered_device_spec import RenderedDeviceSpec
from flightctl.models.rendered_device_spec_systemd import RenderedDeviceSpecSystemd
from flightctl.models.repo_spec_type import RepoSpecType
from flightctl.models.repository import Repository
from flightctl.models.repository_list import RepositoryList
from flightctl.models.repository_spec import RepositorySpec
from flightctl.models.repository_status import RepositoryStatus
from flightctl.models.resource_alert_rule import ResourceAlertRule
from flightctl.models.resource_alert_severity_type import ResourceAlertSeverityType
from flightctl.models.resource_monitor import ResourceMonitor
from flightctl.models.resource_monitor_spec import ResourceMonitorSpec
from flightctl.models.resource_sync import ResourceSync
from flightctl.models.resource_sync_list import ResourceSyncList
from flightctl.models.resource_sync_spec import ResourceSyncSpec
from flightctl.models.resource_sync_status import ResourceSyncStatus
from flightctl.models.rollout_device_selection import RolloutDeviceSelection
from flightctl.models.rollout_policy import RolloutPolicy
from flightctl.models.ssh_config import SshConfig
from flightctl.models.ssh_repo_spec import SshRepoSpec
from flightctl.models.status import Status
from flightctl.models.template_version import TemplateVersion
from flightctl.models.template_version_list import TemplateVersionList
from flightctl.models.template_version_spec import TemplateVersionSpec
from flightctl.models.template_version_status import TemplateVersionStatus
from flightctl.models.update_schedule import UpdateSchedule
