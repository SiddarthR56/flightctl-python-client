# coding: utf-8

"""
    Flight Control API

    [Flight Control](https://github.com/flightctl/flightctl) is a service for declarative management of fleets of edge devices and their workloads. 

    The version of the OpenAPI document: v1alpha1
    Contact: team@flightctl.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from flightctl.models.fleet_spec_template import FleetSpecTemplate
from flightctl.models.label_selector import LabelSelector
from flightctl.models.rollout_policy import RolloutPolicy
from typing import Optional, Set
from typing_extensions import Self

class FleetSpec(BaseModel):
    """
    FleetSpec is a description of a fleet's target state.
    """ # noqa: E501
    selector: Optional[LabelSelector] = None
    rollout_policy: Optional[RolloutPolicy] = Field(default=None, alias="rolloutPolicy")
    template: FleetSpecTemplate
    __properties: ClassVar[List[str]] = ["selector", "rolloutPolicy", "template"]

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
        """Create an instance of FleetSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of selector
        if self.selector:
            _dict['selector'] = self.selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rollout_policy
        if self.rollout_policy:
            _dict['rolloutPolicy'] = self.rollout_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FleetSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "selector": LabelSelector.from_dict(obj["selector"]) if obj.get("selector") is not None else None,
            "rolloutPolicy": RolloutPolicy.from_dict(obj["rolloutPolicy"]) if obj.get("rolloutPolicy") is not None else None,
            "template": FleetSpecTemplate.from_dict(obj["template"]) if obj.get("template") is not None else None
        })
        return _obj


