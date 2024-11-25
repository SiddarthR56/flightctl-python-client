# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from flightctl.models.resource_alert_rule import ResourceAlertRule
from typing import Optional, Set
from typing_extensions import Self

class CPUResourceMonitorSpec(BaseModel):
    """
    CPUResourceMonitorSpec
    """ # noqa: E501
    monitor_type: StrictStr = Field(alias="monitorType")
    alert_rules: List[ResourceAlertRule] = Field(description="Array of alert rules. Only one alert per severity is allowed.", alias="alertRules")
    sampling_interval: Annotated[str, Field(strict=True)] = Field(description="Duration between monitor samples. Format: positive integer followed by 's' for seconds, 'm' for minutes, 'h' for hours.", alias="samplingInterval")
    __properties: ClassVar[List[str]] = ["monitorType", "alertRules", "samplingInterval"]

    @field_validator('sampling_interval')
    def sampling_interval_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[1-9]\d*[smh]$", value):
            raise ValueError(r"must validate the regular expression /^[1-9]\d*[smh]$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CPUResourceMonitorSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in alert_rules (list)
        _items = []
        if self.alert_rules:
            for _item_alert_rules in self.alert_rules:
                if _item_alert_rules:
                    _items.append(_item_alert_rules.to_dict())
            _dict['alertRules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CPUResourceMonitorSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "monitorType": obj.get("monitorType"),
            "alertRules": [ResourceAlertRule.from_dict(_item) for _item in obj["alertRules"]] if obj.get("alertRules") is not None else None,
            "samplingInterval": obj.get("samplingInterval")
        })
        return _obj


