# coding: utf-8

"""
    Flight Control API

    [Flight Control](https://flightctl.io) is a service for declarative management of fleets of edge devices and their workloads. 

    The version of the OpenAPI document: v1alpha1
    Contact: team@flightctl.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flightctl.models.condition import Condition
from flightctl.models.enrollment_request_approval_status import EnrollmentRequestApprovalStatus
from typing import Optional, Set
from typing_extensions import Self

class EnrollmentRequestStatus(BaseModel):
    """
    EnrollmentRequestStatus represents information about the status of a EnrollmentRequest.
    """ # noqa: E501
    certificate: Optional[StrictStr] = Field(default=None, description="The PEM-encoded signed certificate.")
    conditions: List[Condition] = Field(description="Current state of the EnrollmentRequest.")
    approval: Optional[EnrollmentRequestApprovalStatus] = None
    __properties: ClassVar[List[str]] = ["certificate", "conditions", "approval"]

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
        """Create an instance of EnrollmentRequestStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict['conditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of approval
        if self.approval:
            _dict['approval'] = self.approval.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnrollmentRequestStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certificate": obj.get("certificate"),
            "conditions": [Condition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None,
            "approval": EnrollmentRequestApprovalStatus.from_dict(obj["approval"]) if obj.get("approval") is not None else None
        })
        return _obj


