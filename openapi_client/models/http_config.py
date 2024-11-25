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

from pydantic import BaseModel, ConfigDict, Field, SecretStr, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class HttpConfig(BaseModel):
    """
    HttpConfig
    """ # noqa: E501
    username: Optional[StrictStr] = Field(default=None, description="The username for auth with HTTP transport")
    password: Optional[SecretStr] = Field(default=None, description="The password for auth with HTTP transport")
    tls_crt: Optional[SecretStr] = Field(default=None, description="Base64 encoded TLS cert data", alias="tls.crt")
    tls_key: Optional[SecretStr] = Field(default=None, description="Base64 encoded TLS cert key", alias="tls.key")
    ca_crt: Optional[StrictStr] = Field(default=None, description="Base64 encoded root CA", alias="ca.crt")
    skip_server_verification: Optional[StrictBool] = Field(default=None, description="Skip remote server verification", alias="skipServerVerification")
    token: Optional[SecretStr] = Field(default=None, description="The token for auth with HTTP transport")
    __properties: ClassVar[List[str]] = ["username", "password", "tls.crt", "tls.key", "ca.crt", "skipServerVerification", "token"]

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
        """Create an instance of HttpConfig from a JSON string"""
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
        """Create an instance of HttpConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "username": obj.get("username"),
            "password": obj.get("password"),
            "tls.crt": obj.get("tls.crt"),
            "tls.key": obj.get("tls.key"),
            "ca.crt": obj.get("ca.crt"),
            "skipServerVerification": obj.get("skipServerVerification"),
            "token": obj.get("token")
        })
        return _obj


