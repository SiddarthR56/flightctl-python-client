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
import json
from enum import Enum
from typing_extensions import Self


class RolloutStrategy(str, Enum):
    """
    The strategy of choice for device selection in rollout policy.
    """

    """
    allowed enum values
    """
    BATCHSEQUENCE = 'BatchSequence'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RolloutStrategy from a JSON string"""
        return cls(json.loads(json_str))


