# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class CloudWorkloadSecurityAgentRuleActionHash(ModelNormal):
    def __init__(self_, **kwargs):
        """
        An empty object indicating the hash action
        """
        super().__init__(kwargs)
