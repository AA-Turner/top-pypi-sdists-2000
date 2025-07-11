# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.enums",
    marshal="google.ads.googleads.v20",
    manifest={
        "PerformanceMaxUpgradeStatusEnum",
    },
)


class PerformanceMaxUpgradeStatusEnum(proto.Message):
    r"""Performance Max Upgrade status for campaign."""

    class PerformanceMaxUpgradeStatus(proto.Enum):
        r"""Performance Max Upgrade status enum for campaign.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            UPGRADE_IN_PROGRESS (3):
                The upgrade to a Performance Max campaign is
                in progress.
            UPGRADE_COMPLETE (4):
                The upgrade to a Performance Max campaign is
                complete.
            UPGRADE_FAILED (5):
                The upgrade to a Performance Max campaign
                failed. The campaign will still serve as it was
                before upgrade was attempted.
            UPGRADE_ELIGIBLE (6):
                The campaign is eligible for upgrade to a
                Performance Max campaign.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        UPGRADE_IN_PROGRESS = 3
        UPGRADE_COMPLETE = 4
        UPGRADE_FAILED = 5
        UPGRADE_ELIGIBLE = 6


__all__ = tuple(sorted(__protobuf__.manifest))
