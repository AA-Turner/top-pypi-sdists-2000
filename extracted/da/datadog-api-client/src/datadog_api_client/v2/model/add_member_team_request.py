# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.member_team import MemberTeam


class AddMemberTeamRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.member_team import MemberTeam

        return {
            "data": (MemberTeam,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: MemberTeam, **kwargs):
        """
        Request to add a member team to super team's hierarchy

        :param data: A member team
        :type data: MemberTeam
        """
        super().__init__(kwargs)

        self_.data = data
