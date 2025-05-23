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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flightctl.models.encoding_type import EncodingType
from typing import Optional, Set
from typing_extensions import Self

class FileSpec(BaseModel):
    """
    FileSpec
    """ # noqa: E501
    content: StrictStr = Field(description="The plain text (UTF-8) or base64-encoded content of the file.")
    content_encoding: Optional[EncodingType] = Field(default=None, alias="contentEncoding")
    mode: Optional[StrictInt] = Field(default=None, description="The file's permission mode. You may specify the more familiar octal with a leading zero (e.g., 0644) or as a decimal without a leading zero (e.g., 420). Setuid/setgid/sticky bits are supported. If not specified, the permission mode for files defaults to 0644.")
    user: Optional[StrictStr] = Field(default=None, description="The file's owner, specified either as a name or numeric ID. Defaults to \"root\".")
    group: Optional[StrictStr] = Field(default=None, description="The file's group, specified either as a name or numeric ID. Defaults to \"root\".")
    path: StrictStr = Field(description="The absolute path to a file on the system. Note that any existing file will be overwritten.")
    __properties: ClassVar[List[str]] = ["content", "contentEncoding", "mode", "user", "group", "path"]

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
        """Create an instance of FileSpec from a JSON string"""
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
        """Create an instance of FileSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content": obj.get("content"),
            "contentEncoding": obj.get("contentEncoding"),
            "mode": obj.get("mode"),
            "user": obj.get("user"),
            "group": obj.get("group"),
            "path": obj.get("path")
        })
        return _obj


