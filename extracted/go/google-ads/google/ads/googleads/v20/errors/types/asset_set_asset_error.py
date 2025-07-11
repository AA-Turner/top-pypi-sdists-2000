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
    package="google.ads.googleads.v20.errors",
    marshal="google.ads.googleads.v20",
    manifest={
        "AssetSetAssetErrorEnum",
    },
)


class AssetSetAssetErrorEnum(proto.Message):
    r"""Container for enum describing possible asset set asset
    errors.

    """

    class AssetSetAssetError(proto.Enum):
        r"""Enum describing possible asset set asset errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            INVALID_ASSET_TYPE (2):
                The asset type is not eligible to be linked
                to the specific type of asset set.
            INVALID_ASSET_SET_TYPE (3):
                The asset set type is not eligible to contain
                the specified type of assets.
            DUPLICATE_EXTERNAL_KEY (4):
                The asset contains duplicate external key
                with another asset in the asset set.
            PARENT_LINKAGE_DOES_NOT_EXIST (5):
                When attaching a Location typed Asset to a
                LocationGroup typed AssetSet, the AssetSetAsset
                linkage between the parent LocationSync AssetSet
                and the Asset doesn't exist.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_ASSET_TYPE = 2
        INVALID_ASSET_SET_TYPE = 3
        DUPLICATE_EXTERNAL_KEY = 4
        PARENT_LINKAGE_DOES_NOT_EXIST = 5


__all__ = tuple(sorted(__protobuf__.manifest))
