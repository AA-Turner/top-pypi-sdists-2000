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

from google.ads.googleads.v20.common.types import simulation
from google.ads.googleads.v20.enums.types import simulation_modification_method
from google.ads.googleads.v20.enums.types import simulation_type


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.resources",
    marshal="google.ads.googleads.v20",
    manifest={
        "CampaignSimulation",
    },
)


class CampaignSimulation(proto.Message):
    r"""A campaign simulation. Supported combinations of advertising channel
    type, simulation type and simulation modification method is detailed
    below respectively.

    -  SEARCH - CPC_BID - UNIFORM
    -  SEARCH - CPC_BID - SCALING
    -  SEARCH - TARGET_CPA - UNIFORM
    -  SEARCH - TARGET_CPA - SCALING
    -  SEARCH - TARGET_ROAS - UNIFORM
    -  SEARCH - TARGET_IMPRESSION_SHARE - UNIFORM
    -  SEARCH - BUDGET - UNIFORM
    -  SHOPPING - BUDGET - UNIFORM
    -  SHOPPING - TARGET_ROAS - UNIFORM
    -  MULTI_CHANNEL - TARGET_CPA - UNIFORM
    -  MULTI_CHANNEL - TARGET_ROAS - UNIFORM
    -  DEMAND_GEN - TARGET_CPA - DEFAULT
    -  DISPLAY - TARGET_CPA - UNIFORM
    -  PERFORMANCE_MAX - TARGET_CPA - UNIFORM
    -  PERFORMANCE_MAX - TARGET_ROAS - UNIFORM
    -  PERFORMANCE_MAX - BUDGET - UNIFORM

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_name (str):
            Output only. The resource name of the campaign simulation.
            Campaign simulation resource names have the form:

            ``customers/{customer_id}/campaignSimulations/{campaign_id}~{type}~{modification_method}~{start_date}~{end_date}``
        campaign_id (int):
            Output only. Campaign id of the simulation.
        type_ (google.ads.googleads.v20.enums.types.SimulationTypeEnum.SimulationType):
            Output only. The field that the simulation
            modifies.
        modification_method (google.ads.googleads.v20.enums.types.SimulationModificationMethodEnum.SimulationModificationMethod):
            Output only. How the simulation modifies the
            field.
        start_date (str):
            Output only. First day on which the
            simulation is based, in YYYY-MM-DD format.
        end_date (str):
            Output only. Last day on which the simulation
            is based, in YYYY-MM-DD format
        cpc_bid_point_list (google.ads.googleads.v20.common.types.CpcBidSimulationPointList):
            Output only. Simulation points if the simulation type is
            CPC_BID.

            This field is a member of `oneof`_ ``point_list``.
        target_cpa_point_list (google.ads.googleads.v20.common.types.TargetCpaSimulationPointList):
            Output only. Simulation points if the simulation type is
            TARGET_CPA.

            This field is a member of `oneof`_ ``point_list``.
        target_roas_point_list (google.ads.googleads.v20.common.types.TargetRoasSimulationPointList):
            Output only. Simulation points if the simulation type is
            TARGET_ROAS.

            This field is a member of `oneof`_ ``point_list``.
        target_impression_share_point_list (google.ads.googleads.v20.common.types.TargetImpressionShareSimulationPointList):
            Output only. Simulation points if the simulation type is
            TARGET_IMPRESSION_SHARE.

            This field is a member of `oneof`_ ``point_list``.
        budget_point_list (google.ads.googleads.v20.common.types.BudgetSimulationPointList):
            Output only. Simulation points if the
            simulation type is BUDGET.

            This field is a member of `oneof`_ ``point_list``.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    campaign_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    type_: simulation_type.SimulationTypeEnum.SimulationType = proto.Field(
        proto.ENUM,
        number=3,
        enum=simulation_type.SimulationTypeEnum.SimulationType,
    )
    modification_method: (
        simulation_modification_method.SimulationModificationMethodEnum.SimulationModificationMethod
    ) = proto.Field(
        proto.ENUM,
        number=4,
        enum=simulation_modification_method.SimulationModificationMethodEnum.SimulationModificationMethod,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=5,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=6,
    )
    cpc_bid_point_list: simulation.CpcBidSimulationPointList = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="point_list",
        message=simulation.CpcBidSimulationPointList,
    )
    target_cpa_point_list: simulation.TargetCpaSimulationPointList = (
        proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="point_list",
            message=simulation.TargetCpaSimulationPointList,
        )
    )
    target_roas_point_list: simulation.TargetRoasSimulationPointList = (
        proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="point_list",
            message=simulation.TargetRoasSimulationPointList,
        )
    )
    target_impression_share_point_list: (
        simulation.TargetImpressionShareSimulationPointList
    ) = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="point_list",
        message=simulation.TargetImpressionShareSimulationPointList,
    )
    budget_point_list: simulation.BudgetSimulationPointList = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="point_list",
        message=simulation.BudgetSimulationPointList,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
