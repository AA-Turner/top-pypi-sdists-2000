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
        "DisplayAdFormatSettingEnum",
    },
)


class DisplayAdFormatSettingEnum(proto.Message):
    r"""Container for display ad format settings."""

    class DisplayAdFormatSetting(proto.Enum):
        r"""Enumerates display ad format settings.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                The value is unknown in this version.
            ALL_FORMATS (2):
                Text, image and native formats.
            NON_NATIVE (3):
                Text and image formats.
            NATIVE (4):
                Native format, for example, the format
                rendering is controlled by the publisher and not
                by Google.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_FORMATS = 2
        NON_NATIVE = 3
        NATIVE = 4


__all__ = tuple(sorted(__protobuf__.manifest))
