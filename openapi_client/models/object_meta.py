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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ObjectMeta(BaseModel):
    """
    ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.
    """ # noqa: E501
    creation_timestamp: Optional[datetime] = Field(default=None, alias="creationTimestamp")
    deletion_timestamp: Optional[datetime] = Field(default=None, alias="deletionTimestamp")
    name: Optional[StrictStr] = Field(default=None, description="name of the object")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Map of string keys and values that can be used to organize and categorize (scope and select) objects.")
    generation: Optional[StrictInt] = Field(default=None, description="A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.")
    owner: Optional[StrictStr] = Field(default=None, description="A resource that owns this resource, in \"kind/name\" format.")
    annotations: Optional[Dict[str, StrictStr]] = Field(default=None, description="Properties set by the service.")
    resource_version: Optional[StrictStr] = Field(default=None, description="An opaque string that identifies the server's internal version of an object.", alias="resourceVersion")
    __properties: ClassVar[List[str]] = ["creationTimestamp", "deletionTimestamp", "name", "labels", "generation", "owner", "annotations", "resourceVersion"]

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
        """Create an instance of ObjectMeta from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "creationTimestamp": obj.get("creationTimestamp"),
            "deletionTimestamp": obj.get("deletionTimestamp"),
            "name": obj.get("name"),
            "labels": obj.get("labels"),
            "generation": obj.get("generation"),
            "owner": obj.get("owner"),
            "annotations": obj.get("annotations"),
            "resourceVersion": obj.get("resourceVersion")
        })
        return _obj


