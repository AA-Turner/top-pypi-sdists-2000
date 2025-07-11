"""
Main interface for ec2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ec2 import (
        BundleTaskCompleteWaiter,
        Client,
        ConversionTaskCancelledWaiter,
        ConversionTaskCompletedWaiter,
        ConversionTaskDeletedWaiter,
        CustomerGatewayAvailableWaiter,
        DescribeAddressTransfersPaginator,
        DescribeAddressesAttributePaginator,
        DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator,
        DescribeByoipCidrsPaginator,
        DescribeCapacityBlockExtensionHistoryPaginator,
        DescribeCapacityBlockExtensionOfferingsPaginator,
        DescribeCapacityBlockOfferingsPaginator,
        DescribeCapacityBlockStatusPaginator,
        DescribeCapacityBlocksPaginator,
        DescribeCapacityReservationBillingRequestsPaginator,
        DescribeCapacityReservationFleetsPaginator,
        DescribeCapacityReservationsPaginator,
        DescribeCarrierGatewaysPaginator,
        DescribeClassicLinkInstancesPaginator,
        DescribeClientVpnAuthorizationRulesPaginator,
        DescribeClientVpnConnectionsPaginator,
        DescribeClientVpnEndpointsPaginator,
        DescribeClientVpnRoutesPaginator,
        DescribeClientVpnTargetNetworksPaginator,
        DescribeCoipPoolsPaginator,
        DescribeDhcpOptionsPaginator,
        DescribeEgressOnlyInternetGatewaysPaginator,
        DescribeExportImageTasksPaginator,
        DescribeFastLaunchImagesPaginator,
        DescribeFastSnapshotRestoresPaginator,
        DescribeFleetsPaginator,
        DescribeFlowLogsPaginator,
        DescribeFpgaImagesPaginator,
        DescribeHostReservationOfferingsPaginator,
        DescribeHostReservationsPaginator,
        DescribeHostsPaginator,
        DescribeIamInstanceProfileAssociationsPaginator,
        DescribeImagesPaginator,
        DescribeImportImageTasksPaginator,
        DescribeImportSnapshotTasksPaginator,
        DescribeInstanceConnectEndpointsPaginator,
        DescribeInstanceCreditSpecificationsPaginator,
        DescribeInstanceEventWindowsPaginator,
        DescribeInstanceImageMetadataPaginator,
        DescribeInstanceStatusPaginator,
        DescribeInstanceTopologyPaginator,
        DescribeInstanceTypeOfferingsPaginator,
        DescribeInstanceTypesPaginator,
        DescribeInstancesPaginator,
        DescribeInternetGatewaysPaginator,
        DescribeIpamPoolsPaginator,
        DescribeIpamResourceDiscoveriesPaginator,
        DescribeIpamResourceDiscoveryAssociationsPaginator,
        DescribeIpamScopesPaginator,
        DescribeIpamsPaginator,
        DescribeIpv6PoolsPaginator,
        DescribeLaunchTemplateVersionsPaginator,
        DescribeLaunchTemplatesPaginator,
        DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
        DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
        DescribeLocalGatewayRouteTablesPaginator,
        DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
        DescribeLocalGatewayVirtualInterfacesPaginator,
        DescribeLocalGatewaysPaginator,
        DescribeMacHostsPaginator,
        DescribeMacModificationTasksPaginator,
        DescribeManagedPrefixListsPaginator,
        DescribeMovingAddressesPaginator,
        DescribeNatGatewaysPaginator,
        DescribeNetworkAclsPaginator,
        DescribeNetworkInsightsAccessScopeAnalysesPaginator,
        DescribeNetworkInsightsAccessScopesPaginator,
        DescribeNetworkInsightsAnalysesPaginator,
        DescribeNetworkInsightsPathsPaginator,
        DescribeNetworkInterfacePermissionsPaginator,
        DescribeNetworkInterfacesPaginator,
        DescribePrefixListsPaginator,
        DescribePrincipalIdFormatPaginator,
        DescribePublicIpv4PoolsPaginator,
        DescribeReplaceRootVolumeTasksPaginator,
        DescribeReservedInstancesModificationsPaginator,
        DescribeReservedInstancesOfferingsPaginator,
        DescribeRouteServerEndpointsPaginator,
        DescribeRouteServerPeersPaginator,
        DescribeRouteServersPaginator,
        DescribeRouteTablesPaginator,
        DescribeScheduledInstanceAvailabilityPaginator,
        DescribeScheduledInstancesPaginator,
        DescribeSecurityGroupRulesPaginator,
        DescribeSecurityGroupVpcAssociationsPaginator,
        DescribeSecurityGroupsPaginator,
        DescribeSnapshotTierStatusPaginator,
        DescribeSnapshotsPaginator,
        DescribeSpotFleetInstancesPaginator,
        DescribeSpotFleetRequestsPaginator,
        DescribeSpotInstanceRequestsPaginator,
        DescribeSpotPriceHistoryPaginator,
        DescribeStaleSecurityGroupsPaginator,
        DescribeStoreImageTasksPaginator,
        DescribeSubnetsPaginator,
        DescribeTagsPaginator,
        DescribeTrafficMirrorFiltersPaginator,
        DescribeTrafficMirrorSessionsPaginator,
        DescribeTrafficMirrorTargetsPaginator,
        DescribeTransitGatewayAttachmentsPaginator,
        DescribeTransitGatewayConnectPeersPaginator,
        DescribeTransitGatewayConnectsPaginator,
        DescribeTransitGatewayMulticastDomainsPaginator,
        DescribeTransitGatewayPeeringAttachmentsPaginator,
        DescribeTransitGatewayPolicyTablesPaginator,
        DescribeTransitGatewayRouteTableAnnouncementsPaginator,
        DescribeTransitGatewayRouteTablesPaginator,
        DescribeTransitGatewayVpcAttachmentsPaginator,
        DescribeTransitGatewaysPaginator,
        DescribeTrunkInterfaceAssociationsPaginator,
        DescribeVerifiedAccessEndpointsPaginator,
        DescribeVerifiedAccessGroupsPaginator,
        DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator,
        DescribeVerifiedAccessInstancesPaginator,
        DescribeVerifiedAccessTrustProvidersPaginator,
        DescribeVolumeStatusPaginator,
        DescribeVolumesModificationsPaginator,
        DescribeVolumesPaginator,
        DescribeVpcClassicLinkDnsSupportPaginator,
        DescribeVpcEndpointConnectionNotificationsPaginator,
        DescribeVpcEndpointConnectionsPaginator,
        DescribeVpcEndpointServiceConfigurationsPaginator,
        DescribeVpcEndpointServicePermissionsPaginator,
        DescribeVpcEndpointServicesPaginator,
        DescribeVpcEndpointsPaginator,
        DescribeVpcPeeringConnectionsPaginator,
        DescribeVpcsPaginator,
        EC2Client,
        EC2ServiceResource,
        ExportTaskCancelledWaiter,
        ExportTaskCompletedWaiter,
        GetAssociatedIpv6PoolCidrsPaginator,
        GetAwsNetworkPerformanceDataPaginator,
        GetGroupsForCapacityReservationPaginator,
        GetInstanceTypesFromInstanceRequirementsPaginator,
        GetIpamAddressHistoryPaginator,
        GetIpamDiscoveredAccountsPaginator,
        GetIpamDiscoveredResourceCidrsPaginator,
        GetIpamPoolAllocationsPaginator,
        GetIpamPoolCidrsPaginator,
        GetIpamResourceCidrsPaginator,
        GetManagedPrefixListAssociationsPaginator,
        GetManagedPrefixListEntriesPaginator,
        GetNetworkInsightsAccessScopeAnalysisFindingsPaginator,
        GetSecurityGroupsForVpcPaginator,
        GetSpotPlacementScoresPaginator,
        GetTransitGatewayAttachmentPropagationsPaginator,
        GetTransitGatewayMulticastDomainAssociationsPaginator,
        GetTransitGatewayPolicyTableAssociationsPaginator,
        GetTransitGatewayPrefixListReferencesPaginator,
        GetTransitGatewayRouteTableAssociationsPaginator,
        GetTransitGatewayRouteTablePropagationsPaginator,
        GetVpnConnectionDeviceTypesPaginator,
        ImageAvailableWaiter,
        ImageExistsWaiter,
        InstanceExistsWaiter,
        InstanceRunningWaiter,
        InstanceStatusOkWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
        InternetGatewayExistsWaiter,
        KeyPairExistsWaiter,
        ListImagesInRecycleBinPaginator,
        ListSnapshotsInRecycleBinPaginator,
        NatGatewayAvailableWaiter,
        NatGatewayDeletedWaiter,
        NetworkInterfaceAvailableWaiter,
        PasswordDataAvailableWaiter,
        SearchLocalGatewayRoutesPaginator,
        SearchTransitGatewayMulticastGroupsPaginator,
        SecurityGroupExistsWaiter,
        SecurityGroupVpcAssociationAssociatedWaiter,
        SecurityGroupVpcAssociationDisassociatedWaiter,
        ServiceResource,
        SnapshotCompletedWaiter,
        SnapshotImportedWaiter,
        SpotInstanceRequestFulfilledWaiter,
        StoreImageTaskCompleteWaiter,
        SubnetAvailableWaiter,
        SystemStatusOkWaiter,
        VolumeAvailableWaiter,
        VolumeDeletedWaiter,
        VolumeInUseWaiter,
        VpcAvailableWaiter,
        VpcExistsWaiter,
        VpcPeeringConnectionDeletedWaiter,
        VpcPeeringConnectionExistsWaiter,
        VpnConnectionAvailableWaiter,
        VpnConnectionDeletedWaiter,
    )

    session = Session()
    client: EC2Client = session.client("ec2")

    resource: EC2ServiceResource = session.resource("ec2")

    bundle_task_complete_waiter: BundleTaskCompleteWaiter = client.get_waiter("bundle_task_complete")
    conversion_task_cancelled_waiter: ConversionTaskCancelledWaiter = client.get_waiter("conversion_task_cancelled")
    conversion_task_completed_waiter: ConversionTaskCompletedWaiter = client.get_waiter("conversion_task_completed")
    conversion_task_deleted_waiter: ConversionTaskDeletedWaiter = client.get_waiter("conversion_task_deleted")
    customer_gateway_available_waiter: CustomerGatewayAvailableWaiter = client.get_waiter("customer_gateway_available")
    export_task_cancelled_waiter: ExportTaskCancelledWaiter = client.get_waiter("export_task_cancelled")
    export_task_completed_waiter: ExportTaskCompletedWaiter = client.get_waiter("export_task_completed")
    image_available_waiter: ImageAvailableWaiter = client.get_waiter("image_available")
    image_exists_waiter: ImageExistsWaiter = client.get_waiter("image_exists")
    instance_exists_waiter: InstanceExistsWaiter = client.get_waiter("instance_exists")
    instance_running_waiter: InstanceRunningWaiter = client.get_waiter("instance_running")
    instance_status_ok_waiter: InstanceStatusOkWaiter = client.get_waiter("instance_status_ok")
    instance_stopped_waiter: InstanceStoppedWaiter = client.get_waiter("instance_stopped")
    instance_terminated_waiter: InstanceTerminatedWaiter = client.get_waiter("instance_terminated")
    internet_gateway_exists_waiter: InternetGatewayExistsWaiter = client.get_waiter("internet_gateway_exists")
    key_pair_exists_waiter: KeyPairExistsWaiter = client.get_waiter("key_pair_exists")
    nat_gateway_available_waiter: NatGatewayAvailableWaiter = client.get_waiter("nat_gateway_available")
    nat_gateway_deleted_waiter: NatGatewayDeletedWaiter = client.get_waiter("nat_gateway_deleted")
    network_interface_available_waiter: NetworkInterfaceAvailableWaiter = client.get_waiter("network_interface_available")
    password_data_available_waiter: PasswordDataAvailableWaiter = client.get_waiter("password_data_available")
    security_group_exists_waiter: SecurityGroupExistsWaiter = client.get_waiter("security_group_exists")
    security_group_vpc_association_associated_waiter: SecurityGroupVpcAssociationAssociatedWaiter = client.get_waiter("security_group_vpc_association_associated")
    security_group_vpc_association_disassociated_waiter: SecurityGroupVpcAssociationDisassociatedWaiter = client.get_waiter("security_group_vpc_association_disassociated")
    snapshot_completed_waiter: SnapshotCompletedWaiter = client.get_waiter("snapshot_completed")
    snapshot_imported_waiter: SnapshotImportedWaiter = client.get_waiter("snapshot_imported")
    spot_instance_request_fulfilled_waiter: SpotInstanceRequestFulfilledWaiter = client.get_waiter("spot_instance_request_fulfilled")
    store_image_task_complete_waiter: StoreImageTaskCompleteWaiter = client.get_waiter("store_image_task_complete")
    subnet_available_waiter: SubnetAvailableWaiter = client.get_waiter("subnet_available")
    system_status_ok_waiter: SystemStatusOkWaiter = client.get_waiter("system_status_ok")
    volume_available_waiter: VolumeAvailableWaiter = client.get_waiter("volume_available")
    volume_deleted_waiter: VolumeDeletedWaiter = client.get_waiter("volume_deleted")
    volume_in_use_waiter: VolumeInUseWaiter = client.get_waiter("volume_in_use")
    vpc_available_waiter: VpcAvailableWaiter = client.get_waiter("vpc_available")
    vpc_exists_waiter: VpcExistsWaiter = client.get_waiter("vpc_exists")
    vpc_peering_connection_deleted_waiter: VpcPeeringConnectionDeletedWaiter = client.get_waiter("vpc_peering_connection_deleted")
    vpc_peering_connection_exists_waiter: VpcPeeringConnectionExistsWaiter = client.get_waiter("vpc_peering_connection_exists")
    vpn_connection_available_waiter: VpnConnectionAvailableWaiter = client.get_waiter("vpn_connection_available")
    vpn_connection_deleted_waiter: VpnConnectionDeletedWaiter = client.get_waiter("vpn_connection_deleted")

    describe_address_transfers_paginator: DescribeAddressTransfersPaginator = client.get_paginator("describe_address_transfers")
    describe_addresses_attribute_paginator: DescribeAddressesAttributePaginator = client.get_paginator("describe_addresses_attribute")
    describe_aws_network_performance_metric_subscriptions_paginator: DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator = client.get_paginator("describe_aws_network_performance_metric_subscriptions")
    describe_byoip_cidrs_paginator: DescribeByoipCidrsPaginator = client.get_paginator("describe_byoip_cidrs")
    describe_capacity_block_extension_history_paginator: DescribeCapacityBlockExtensionHistoryPaginator = client.get_paginator("describe_capacity_block_extension_history")
    describe_capacity_block_extension_offerings_paginator: DescribeCapacityBlockExtensionOfferingsPaginator = client.get_paginator("describe_capacity_block_extension_offerings")
    describe_capacity_block_offerings_paginator: DescribeCapacityBlockOfferingsPaginator = client.get_paginator("describe_capacity_block_offerings")
    describe_capacity_block_status_paginator: DescribeCapacityBlockStatusPaginator = client.get_paginator("describe_capacity_block_status")
    describe_capacity_blocks_paginator: DescribeCapacityBlocksPaginator = client.get_paginator("describe_capacity_blocks")
    describe_capacity_reservation_billing_requests_paginator: DescribeCapacityReservationBillingRequestsPaginator = client.get_paginator("describe_capacity_reservation_billing_requests")
    describe_capacity_reservation_fleets_paginator: DescribeCapacityReservationFleetsPaginator = client.get_paginator("describe_capacity_reservation_fleets")
    describe_capacity_reservations_paginator: DescribeCapacityReservationsPaginator = client.get_paginator("describe_capacity_reservations")
    describe_carrier_gateways_paginator: DescribeCarrierGatewaysPaginator = client.get_paginator("describe_carrier_gateways")
    describe_classic_link_instances_paginator: DescribeClassicLinkInstancesPaginator = client.get_paginator("describe_classic_link_instances")
    describe_client_vpn_authorization_rules_paginator: DescribeClientVpnAuthorizationRulesPaginator = client.get_paginator("describe_client_vpn_authorization_rules")
    describe_client_vpn_connections_paginator: DescribeClientVpnConnectionsPaginator = client.get_paginator("describe_client_vpn_connections")
    describe_client_vpn_endpoints_paginator: DescribeClientVpnEndpointsPaginator = client.get_paginator("describe_client_vpn_endpoints")
    describe_client_vpn_routes_paginator: DescribeClientVpnRoutesPaginator = client.get_paginator("describe_client_vpn_routes")
    describe_client_vpn_target_networks_paginator: DescribeClientVpnTargetNetworksPaginator = client.get_paginator("describe_client_vpn_target_networks")
    describe_coip_pools_paginator: DescribeCoipPoolsPaginator = client.get_paginator("describe_coip_pools")
    describe_dhcp_options_paginator: DescribeDhcpOptionsPaginator = client.get_paginator("describe_dhcp_options")
    describe_egress_only_internet_gateways_paginator: DescribeEgressOnlyInternetGatewaysPaginator = client.get_paginator("describe_egress_only_internet_gateways")
    describe_export_image_tasks_paginator: DescribeExportImageTasksPaginator = client.get_paginator("describe_export_image_tasks")
    describe_fast_launch_images_paginator: DescribeFastLaunchImagesPaginator = client.get_paginator("describe_fast_launch_images")
    describe_fast_snapshot_restores_paginator: DescribeFastSnapshotRestoresPaginator = client.get_paginator("describe_fast_snapshot_restores")
    describe_fleets_paginator: DescribeFleetsPaginator = client.get_paginator("describe_fleets")
    describe_flow_logs_paginator: DescribeFlowLogsPaginator = client.get_paginator("describe_flow_logs")
    describe_fpga_images_paginator: DescribeFpgaImagesPaginator = client.get_paginator("describe_fpga_images")
    describe_host_reservation_offerings_paginator: DescribeHostReservationOfferingsPaginator = client.get_paginator("describe_host_reservation_offerings")
    describe_host_reservations_paginator: DescribeHostReservationsPaginator = client.get_paginator("describe_host_reservations")
    describe_hosts_paginator: DescribeHostsPaginator = client.get_paginator("describe_hosts")
    describe_iam_instance_profile_associations_paginator: DescribeIamInstanceProfileAssociationsPaginator = client.get_paginator("describe_iam_instance_profile_associations")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_import_image_tasks_paginator: DescribeImportImageTasksPaginator = client.get_paginator("describe_import_image_tasks")
    describe_import_snapshot_tasks_paginator: DescribeImportSnapshotTasksPaginator = client.get_paginator("describe_import_snapshot_tasks")
    describe_instance_connect_endpoints_paginator: DescribeInstanceConnectEndpointsPaginator = client.get_paginator("describe_instance_connect_endpoints")
    describe_instance_credit_specifications_paginator: DescribeInstanceCreditSpecificationsPaginator = client.get_paginator("describe_instance_credit_specifications")
    describe_instance_event_windows_paginator: DescribeInstanceEventWindowsPaginator = client.get_paginator("describe_instance_event_windows")
    describe_instance_image_metadata_paginator: DescribeInstanceImageMetadataPaginator = client.get_paginator("describe_instance_image_metadata")
    describe_instance_status_paginator: DescribeInstanceStatusPaginator = client.get_paginator("describe_instance_status")
    describe_instance_topology_paginator: DescribeInstanceTopologyPaginator = client.get_paginator("describe_instance_topology")
    describe_instance_type_offerings_paginator: DescribeInstanceTypeOfferingsPaginator = client.get_paginator("describe_instance_type_offerings")
    describe_instance_types_paginator: DescribeInstanceTypesPaginator = client.get_paginator("describe_instance_types")
    describe_instances_paginator: DescribeInstancesPaginator = client.get_paginator("describe_instances")
    describe_internet_gateways_paginator: DescribeInternetGatewaysPaginator = client.get_paginator("describe_internet_gateways")
    describe_ipam_pools_paginator: DescribeIpamPoolsPaginator = client.get_paginator("describe_ipam_pools")
    describe_ipam_resource_discoveries_paginator: DescribeIpamResourceDiscoveriesPaginator = client.get_paginator("describe_ipam_resource_discoveries")
    describe_ipam_resource_discovery_associations_paginator: DescribeIpamResourceDiscoveryAssociationsPaginator = client.get_paginator("describe_ipam_resource_discovery_associations")
    describe_ipam_scopes_paginator: DescribeIpamScopesPaginator = client.get_paginator("describe_ipam_scopes")
    describe_ipams_paginator: DescribeIpamsPaginator = client.get_paginator("describe_ipams")
    describe_ipv6_pools_paginator: DescribeIpv6PoolsPaginator = client.get_paginator("describe_ipv6_pools")
    describe_launch_template_versions_paginator: DescribeLaunchTemplateVersionsPaginator = client.get_paginator("describe_launch_template_versions")
    describe_launch_templates_paginator: DescribeLaunchTemplatesPaginator = client.get_paginator("describe_launch_templates")
    describe_local_gateway_route_table_virtual_interface_group_associations_paginator: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator = client.get_paginator("describe_local_gateway_route_table_virtual_interface_group_associations")
    describe_local_gateway_route_table_vpc_associations_paginator: DescribeLocalGatewayRouteTableVpcAssociationsPaginator = client.get_paginator("describe_local_gateway_route_table_vpc_associations")
    describe_local_gateway_route_tables_paginator: DescribeLocalGatewayRouteTablesPaginator = client.get_paginator("describe_local_gateway_route_tables")
    describe_local_gateway_virtual_interface_groups_paginator: DescribeLocalGatewayVirtualInterfaceGroupsPaginator = client.get_paginator("describe_local_gateway_virtual_interface_groups")
    describe_local_gateway_virtual_interfaces_paginator: DescribeLocalGatewayVirtualInterfacesPaginator = client.get_paginator("describe_local_gateway_virtual_interfaces")
    describe_local_gateways_paginator: DescribeLocalGatewaysPaginator = client.get_paginator("describe_local_gateways")
    describe_mac_hosts_paginator: DescribeMacHostsPaginator = client.get_paginator("describe_mac_hosts")
    describe_mac_modification_tasks_paginator: DescribeMacModificationTasksPaginator = client.get_paginator("describe_mac_modification_tasks")
    describe_managed_prefix_lists_paginator: DescribeManagedPrefixListsPaginator = client.get_paginator("describe_managed_prefix_lists")
    describe_moving_addresses_paginator: DescribeMovingAddressesPaginator = client.get_paginator("describe_moving_addresses")
    describe_nat_gateways_paginator: DescribeNatGatewaysPaginator = client.get_paginator("describe_nat_gateways")
    describe_network_acls_paginator: DescribeNetworkAclsPaginator = client.get_paginator("describe_network_acls")
    describe_network_insights_access_scope_analyses_paginator: DescribeNetworkInsightsAccessScopeAnalysesPaginator = client.get_paginator("describe_network_insights_access_scope_analyses")
    describe_network_insights_access_scopes_paginator: DescribeNetworkInsightsAccessScopesPaginator = client.get_paginator("describe_network_insights_access_scopes")
    describe_network_insights_analyses_paginator: DescribeNetworkInsightsAnalysesPaginator = client.get_paginator("describe_network_insights_analyses")
    describe_network_insights_paths_paginator: DescribeNetworkInsightsPathsPaginator = client.get_paginator("describe_network_insights_paths")
    describe_network_interface_permissions_paginator: DescribeNetworkInterfacePermissionsPaginator = client.get_paginator("describe_network_interface_permissions")
    describe_network_interfaces_paginator: DescribeNetworkInterfacesPaginator = client.get_paginator("describe_network_interfaces")
    describe_prefix_lists_paginator: DescribePrefixListsPaginator = client.get_paginator("describe_prefix_lists")
    describe_principal_id_format_paginator: DescribePrincipalIdFormatPaginator = client.get_paginator("describe_principal_id_format")
    describe_public_ipv4_pools_paginator: DescribePublicIpv4PoolsPaginator = client.get_paginator("describe_public_ipv4_pools")
    describe_replace_root_volume_tasks_paginator: DescribeReplaceRootVolumeTasksPaginator = client.get_paginator("describe_replace_root_volume_tasks")
    describe_reserved_instances_modifications_paginator: DescribeReservedInstancesModificationsPaginator = client.get_paginator("describe_reserved_instances_modifications")
    describe_reserved_instances_offerings_paginator: DescribeReservedInstancesOfferingsPaginator = client.get_paginator("describe_reserved_instances_offerings")
    describe_route_server_endpoints_paginator: DescribeRouteServerEndpointsPaginator = client.get_paginator("describe_route_server_endpoints")
    describe_route_server_peers_paginator: DescribeRouteServerPeersPaginator = client.get_paginator("describe_route_server_peers")
    describe_route_servers_paginator: DescribeRouteServersPaginator = client.get_paginator("describe_route_servers")
    describe_route_tables_paginator: DescribeRouteTablesPaginator = client.get_paginator("describe_route_tables")
    describe_scheduled_instance_availability_paginator: DescribeScheduledInstanceAvailabilityPaginator = client.get_paginator("describe_scheduled_instance_availability")
    describe_scheduled_instances_paginator: DescribeScheduledInstancesPaginator = client.get_paginator("describe_scheduled_instances")
    describe_security_group_rules_paginator: DescribeSecurityGroupRulesPaginator = client.get_paginator("describe_security_group_rules")
    describe_security_group_vpc_associations_paginator: DescribeSecurityGroupVpcAssociationsPaginator = client.get_paginator("describe_security_group_vpc_associations")
    describe_security_groups_paginator: DescribeSecurityGroupsPaginator = client.get_paginator("describe_security_groups")
    describe_snapshot_tier_status_paginator: DescribeSnapshotTierStatusPaginator = client.get_paginator("describe_snapshot_tier_status")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_spot_fleet_instances_paginator: DescribeSpotFleetInstancesPaginator = client.get_paginator("describe_spot_fleet_instances")
    describe_spot_fleet_requests_paginator: DescribeSpotFleetRequestsPaginator = client.get_paginator("describe_spot_fleet_requests")
    describe_spot_instance_requests_paginator: DescribeSpotInstanceRequestsPaginator = client.get_paginator("describe_spot_instance_requests")
    describe_spot_price_history_paginator: DescribeSpotPriceHistoryPaginator = client.get_paginator("describe_spot_price_history")
    describe_stale_security_groups_paginator: DescribeStaleSecurityGroupsPaginator = client.get_paginator("describe_stale_security_groups")
    describe_store_image_tasks_paginator: DescribeStoreImageTasksPaginator = client.get_paginator("describe_store_image_tasks")
    describe_subnets_paginator: DescribeSubnetsPaginator = client.get_paginator("describe_subnets")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    describe_traffic_mirror_filters_paginator: DescribeTrafficMirrorFiltersPaginator = client.get_paginator("describe_traffic_mirror_filters")
    describe_traffic_mirror_sessions_paginator: DescribeTrafficMirrorSessionsPaginator = client.get_paginator("describe_traffic_mirror_sessions")
    describe_traffic_mirror_targets_paginator: DescribeTrafficMirrorTargetsPaginator = client.get_paginator("describe_traffic_mirror_targets")
    describe_transit_gateway_attachments_paginator: DescribeTransitGatewayAttachmentsPaginator = client.get_paginator("describe_transit_gateway_attachments")
    describe_transit_gateway_connect_peers_paginator: DescribeTransitGatewayConnectPeersPaginator = client.get_paginator("describe_transit_gateway_connect_peers")
    describe_transit_gateway_connects_paginator: DescribeTransitGatewayConnectsPaginator = client.get_paginator("describe_transit_gateway_connects")
    describe_transit_gateway_multicast_domains_paginator: DescribeTransitGatewayMulticastDomainsPaginator = client.get_paginator("describe_transit_gateway_multicast_domains")
    describe_transit_gateway_peering_attachments_paginator: DescribeTransitGatewayPeeringAttachmentsPaginator = client.get_paginator("describe_transit_gateway_peering_attachments")
    describe_transit_gateway_policy_tables_paginator: DescribeTransitGatewayPolicyTablesPaginator = client.get_paginator("describe_transit_gateway_policy_tables")
    describe_transit_gateway_route_table_announcements_paginator: DescribeTransitGatewayRouteTableAnnouncementsPaginator = client.get_paginator("describe_transit_gateway_route_table_announcements")
    describe_transit_gateway_route_tables_paginator: DescribeTransitGatewayRouteTablesPaginator = client.get_paginator("describe_transit_gateway_route_tables")
    describe_transit_gateway_vpc_attachments_paginator: DescribeTransitGatewayVpcAttachmentsPaginator = client.get_paginator("describe_transit_gateway_vpc_attachments")
    describe_transit_gateways_paginator: DescribeTransitGatewaysPaginator = client.get_paginator("describe_transit_gateways")
    describe_trunk_interface_associations_paginator: DescribeTrunkInterfaceAssociationsPaginator = client.get_paginator("describe_trunk_interface_associations")
    describe_verified_access_endpoints_paginator: DescribeVerifiedAccessEndpointsPaginator = client.get_paginator("describe_verified_access_endpoints")
    describe_verified_access_groups_paginator: DescribeVerifiedAccessGroupsPaginator = client.get_paginator("describe_verified_access_groups")
    describe_verified_access_instance_logging_configurations_paginator: DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator = client.get_paginator("describe_verified_access_instance_logging_configurations")
    describe_verified_access_instances_paginator: DescribeVerifiedAccessInstancesPaginator = client.get_paginator("describe_verified_access_instances")
    describe_verified_access_trust_providers_paginator: DescribeVerifiedAccessTrustProvidersPaginator = client.get_paginator("describe_verified_access_trust_providers")
    describe_volume_status_paginator: DescribeVolumeStatusPaginator = client.get_paginator("describe_volume_status")
    describe_volumes_modifications_paginator: DescribeVolumesModificationsPaginator = client.get_paginator("describe_volumes_modifications")
    describe_volumes_paginator: DescribeVolumesPaginator = client.get_paginator("describe_volumes")
    describe_vpc_classic_link_dns_support_paginator: DescribeVpcClassicLinkDnsSupportPaginator = client.get_paginator("describe_vpc_classic_link_dns_support")
    describe_vpc_endpoint_connection_notifications_paginator: DescribeVpcEndpointConnectionNotificationsPaginator = client.get_paginator("describe_vpc_endpoint_connection_notifications")
    describe_vpc_endpoint_connections_paginator: DescribeVpcEndpointConnectionsPaginator = client.get_paginator("describe_vpc_endpoint_connections")
    describe_vpc_endpoint_service_configurations_paginator: DescribeVpcEndpointServiceConfigurationsPaginator = client.get_paginator("describe_vpc_endpoint_service_configurations")
    describe_vpc_endpoint_service_permissions_paginator: DescribeVpcEndpointServicePermissionsPaginator = client.get_paginator("describe_vpc_endpoint_service_permissions")
    describe_vpc_endpoint_services_paginator: DescribeVpcEndpointServicesPaginator = client.get_paginator("describe_vpc_endpoint_services")
    describe_vpc_endpoints_paginator: DescribeVpcEndpointsPaginator = client.get_paginator("describe_vpc_endpoints")
    describe_vpc_peering_connections_paginator: DescribeVpcPeeringConnectionsPaginator = client.get_paginator("describe_vpc_peering_connections")
    describe_vpcs_paginator: DescribeVpcsPaginator = client.get_paginator("describe_vpcs")
    get_associated_ipv6_pool_cidrs_paginator: GetAssociatedIpv6PoolCidrsPaginator = client.get_paginator("get_associated_ipv6_pool_cidrs")
    get_aws_network_performance_data_paginator: GetAwsNetworkPerformanceDataPaginator = client.get_paginator("get_aws_network_performance_data")
    get_groups_for_capacity_reservation_paginator: GetGroupsForCapacityReservationPaginator = client.get_paginator("get_groups_for_capacity_reservation")
    get_instance_types_from_instance_requirements_paginator: GetInstanceTypesFromInstanceRequirementsPaginator = client.get_paginator("get_instance_types_from_instance_requirements")
    get_ipam_address_history_paginator: GetIpamAddressHistoryPaginator = client.get_paginator("get_ipam_address_history")
    get_ipam_discovered_accounts_paginator: GetIpamDiscoveredAccountsPaginator = client.get_paginator("get_ipam_discovered_accounts")
    get_ipam_discovered_resource_cidrs_paginator: GetIpamDiscoveredResourceCidrsPaginator = client.get_paginator("get_ipam_discovered_resource_cidrs")
    get_ipam_pool_allocations_paginator: GetIpamPoolAllocationsPaginator = client.get_paginator("get_ipam_pool_allocations")
    get_ipam_pool_cidrs_paginator: GetIpamPoolCidrsPaginator = client.get_paginator("get_ipam_pool_cidrs")
    get_ipam_resource_cidrs_paginator: GetIpamResourceCidrsPaginator = client.get_paginator("get_ipam_resource_cidrs")
    get_managed_prefix_list_associations_paginator: GetManagedPrefixListAssociationsPaginator = client.get_paginator("get_managed_prefix_list_associations")
    get_managed_prefix_list_entries_paginator: GetManagedPrefixListEntriesPaginator = client.get_paginator("get_managed_prefix_list_entries")
    get_network_insights_access_scope_analysis_findings_paginator: GetNetworkInsightsAccessScopeAnalysisFindingsPaginator = client.get_paginator("get_network_insights_access_scope_analysis_findings")
    get_security_groups_for_vpc_paginator: GetSecurityGroupsForVpcPaginator = client.get_paginator("get_security_groups_for_vpc")
    get_spot_placement_scores_paginator: GetSpotPlacementScoresPaginator = client.get_paginator("get_spot_placement_scores")
    get_transit_gateway_attachment_propagations_paginator: GetTransitGatewayAttachmentPropagationsPaginator = client.get_paginator("get_transit_gateway_attachment_propagations")
    get_transit_gateway_multicast_domain_associations_paginator: GetTransitGatewayMulticastDomainAssociationsPaginator = client.get_paginator("get_transit_gateway_multicast_domain_associations")
    get_transit_gateway_policy_table_associations_paginator: GetTransitGatewayPolicyTableAssociationsPaginator = client.get_paginator("get_transit_gateway_policy_table_associations")
    get_transit_gateway_prefix_list_references_paginator: GetTransitGatewayPrefixListReferencesPaginator = client.get_paginator("get_transit_gateway_prefix_list_references")
    get_transit_gateway_route_table_associations_paginator: GetTransitGatewayRouteTableAssociationsPaginator = client.get_paginator("get_transit_gateway_route_table_associations")
    get_transit_gateway_route_table_propagations_paginator: GetTransitGatewayRouteTablePropagationsPaginator = client.get_paginator("get_transit_gateway_route_table_propagations")
    get_vpn_connection_device_types_paginator: GetVpnConnectionDeviceTypesPaginator = client.get_paginator("get_vpn_connection_device_types")
    list_images_in_recycle_bin_paginator: ListImagesInRecycleBinPaginator = client.get_paginator("list_images_in_recycle_bin")
    list_snapshots_in_recycle_bin_paginator: ListSnapshotsInRecycleBinPaginator = client.get_paginator("list_snapshots_in_recycle_bin")
    search_local_gateway_routes_paginator: SearchLocalGatewayRoutesPaginator = client.get_paginator("search_local_gateway_routes")
    search_transit_gateway_multicast_groups_paginator: SearchTransitGatewayMulticastGroupsPaginator = client.get_paginator("search_transit_gateway_multicast_groups")
    ```
"""

from .client import EC2Client
from .paginator import (
    DescribeAddressesAttributePaginator,
    DescribeAddressTransfersPaginator,
    DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator,
    DescribeByoipCidrsPaginator,
    DescribeCapacityBlockExtensionHistoryPaginator,
    DescribeCapacityBlockExtensionOfferingsPaginator,
    DescribeCapacityBlockOfferingsPaginator,
    DescribeCapacityBlocksPaginator,
    DescribeCapacityBlockStatusPaginator,
    DescribeCapacityReservationBillingRequestsPaginator,
    DescribeCapacityReservationFleetsPaginator,
    DescribeCapacityReservationsPaginator,
    DescribeCarrierGatewaysPaginator,
    DescribeClassicLinkInstancesPaginator,
    DescribeClientVpnAuthorizationRulesPaginator,
    DescribeClientVpnConnectionsPaginator,
    DescribeClientVpnEndpointsPaginator,
    DescribeClientVpnRoutesPaginator,
    DescribeClientVpnTargetNetworksPaginator,
    DescribeCoipPoolsPaginator,
    DescribeDhcpOptionsPaginator,
    DescribeEgressOnlyInternetGatewaysPaginator,
    DescribeExportImageTasksPaginator,
    DescribeFastLaunchImagesPaginator,
    DescribeFastSnapshotRestoresPaginator,
    DescribeFleetsPaginator,
    DescribeFlowLogsPaginator,
    DescribeFpgaImagesPaginator,
    DescribeHostReservationOfferingsPaginator,
    DescribeHostReservationsPaginator,
    DescribeHostsPaginator,
    DescribeIamInstanceProfileAssociationsPaginator,
    DescribeImagesPaginator,
    DescribeImportImageTasksPaginator,
    DescribeImportSnapshotTasksPaginator,
    DescribeInstanceConnectEndpointsPaginator,
    DescribeInstanceCreditSpecificationsPaginator,
    DescribeInstanceEventWindowsPaginator,
    DescribeInstanceImageMetadataPaginator,
    DescribeInstancesPaginator,
    DescribeInstanceStatusPaginator,
    DescribeInstanceTopologyPaginator,
    DescribeInstanceTypeOfferingsPaginator,
    DescribeInstanceTypesPaginator,
    DescribeInternetGatewaysPaginator,
    DescribeIpamPoolsPaginator,
    DescribeIpamResourceDiscoveriesPaginator,
    DescribeIpamResourceDiscoveryAssociationsPaginator,
    DescribeIpamScopesPaginator,
    DescribeIpamsPaginator,
    DescribeIpv6PoolsPaginator,
    DescribeLaunchTemplatesPaginator,
    DescribeLaunchTemplateVersionsPaginator,
    DescribeLocalGatewayRouteTablesPaginator,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
    DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
    DescribeLocalGatewaysPaginator,
    DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
    DescribeLocalGatewayVirtualInterfacesPaginator,
    DescribeMacHostsPaginator,
    DescribeMacModificationTasksPaginator,
    DescribeManagedPrefixListsPaginator,
    DescribeMovingAddressesPaginator,
    DescribeNatGatewaysPaginator,
    DescribeNetworkAclsPaginator,
    DescribeNetworkInsightsAccessScopeAnalysesPaginator,
    DescribeNetworkInsightsAccessScopesPaginator,
    DescribeNetworkInsightsAnalysesPaginator,
    DescribeNetworkInsightsPathsPaginator,
    DescribeNetworkInterfacePermissionsPaginator,
    DescribeNetworkInterfacesPaginator,
    DescribePrefixListsPaginator,
    DescribePrincipalIdFormatPaginator,
    DescribePublicIpv4PoolsPaginator,
    DescribeReplaceRootVolumeTasksPaginator,
    DescribeReservedInstancesModificationsPaginator,
    DescribeReservedInstancesOfferingsPaginator,
    DescribeRouteServerEndpointsPaginator,
    DescribeRouteServerPeersPaginator,
    DescribeRouteServersPaginator,
    DescribeRouteTablesPaginator,
    DescribeScheduledInstanceAvailabilityPaginator,
    DescribeScheduledInstancesPaginator,
    DescribeSecurityGroupRulesPaginator,
    DescribeSecurityGroupsPaginator,
    DescribeSecurityGroupVpcAssociationsPaginator,
    DescribeSnapshotsPaginator,
    DescribeSnapshotTierStatusPaginator,
    DescribeSpotFleetInstancesPaginator,
    DescribeSpotFleetRequestsPaginator,
    DescribeSpotInstanceRequestsPaginator,
    DescribeSpotPriceHistoryPaginator,
    DescribeStaleSecurityGroupsPaginator,
    DescribeStoreImageTasksPaginator,
    DescribeSubnetsPaginator,
    DescribeTagsPaginator,
    DescribeTrafficMirrorFiltersPaginator,
    DescribeTrafficMirrorSessionsPaginator,
    DescribeTrafficMirrorTargetsPaginator,
    DescribeTransitGatewayAttachmentsPaginator,
    DescribeTransitGatewayConnectPeersPaginator,
    DescribeTransitGatewayConnectsPaginator,
    DescribeTransitGatewayMulticastDomainsPaginator,
    DescribeTransitGatewayPeeringAttachmentsPaginator,
    DescribeTransitGatewayPolicyTablesPaginator,
    DescribeTransitGatewayRouteTableAnnouncementsPaginator,
    DescribeTransitGatewayRouteTablesPaginator,
    DescribeTransitGatewaysPaginator,
    DescribeTransitGatewayVpcAttachmentsPaginator,
    DescribeTrunkInterfaceAssociationsPaginator,
    DescribeVerifiedAccessEndpointsPaginator,
    DescribeVerifiedAccessGroupsPaginator,
    DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator,
    DescribeVerifiedAccessInstancesPaginator,
    DescribeVerifiedAccessTrustProvidersPaginator,
    DescribeVolumesModificationsPaginator,
    DescribeVolumesPaginator,
    DescribeVolumeStatusPaginator,
    DescribeVpcClassicLinkDnsSupportPaginator,
    DescribeVpcEndpointConnectionNotificationsPaginator,
    DescribeVpcEndpointConnectionsPaginator,
    DescribeVpcEndpointServiceConfigurationsPaginator,
    DescribeVpcEndpointServicePermissionsPaginator,
    DescribeVpcEndpointServicesPaginator,
    DescribeVpcEndpointsPaginator,
    DescribeVpcPeeringConnectionsPaginator,
    DescribeVpcsPaginator,
    GetAssociatedIpv6PoolCidrsPaginator,
    GetAwsNetworkPerformanceDataPaginator,
    GetGroupsForCapacityReservationPaginator,
    GetInstanceTypesFromInstanceRequirementsPaginator,
    GetIpamAddressHistoryPaginator,
    GetIpamDiscoveredAccountsPaginator,
    GetIpamDiscoveredResourceCidrsPaginator,
    GetIpamPoolAllocationsPaginator,
    GetIpamPoolCidrsPaginator,
    GetIpamResourceCidrsPaginator,
    GetManagedPrefixListAssociationsPaginator,
    GetManagedPrefixListEntriesPaginator,
    GetNetworkInsightsAccessScopeAnalysisFindingsPaginator,
    GetSecurityGroupsForVpcPaginator,
    GetSpotPlacementScoresPaginator,
    GetTransitGatewayAttachmentPropagationsPaginator,
    GetTransitGatewayMulticastDomainAssociationsPaginator,
    GetTransitGatewayPolicyTableAssociationsPaginator,
    GetTransitGatewayPrefixListReferencesPaginator,
    GetTransitGatewayRouteTableAssociationsPaginator,
    GetTransitGatewayRouteTablePropagationsPaginator,
    GetVpnConnectionDeviceTypesPaginator,
    ListImagesInRecycleBinPaginator,
    ListSnapshotsInRecycleBinPaginator,
    SearchLocalGatewayRoutesPaginator,
    SearchTransitGatewayMulticastGroupsPaginator,
)
from .waiter import (
    BundleTaskCompleteWaiter,
    ConversionTaskCancelledWaiter,
    ConversionTaskCompletedWaiter,
    ConversionTaskDeletedWaiter,
    CustomerGatewayAvailableWaiter,
    ExportTaskCancelledWaiter,
    ExportTaskCompletedWaiter,
    ImageAvailableWaiter,
    ImageExistsWaiter,
    InstanceExistsWaiter,
    InstanceRunningWaiter,
    InstanceStatusOkWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
    InternetGatewayExistsWaiter,
    KeyPairExistsWaiter,
    NatGatewayAvailableWaiter,
    NatGatewayDeletedWaiter,
    NetworkInterfaceAvailableWaiter,
    PasswordDataAvailableWaiter,
    SecurityGroupExistsWaiter,
    SecurityGroupVpcAssociationAssociatedWaiter,
    SecurityGroupVpcAssociationDisassociatedWaiter,
    SnapshotCompletedWaiter,
    SnapshotImportedWaiter,
    SpotInstanceRequestFulfilledWaiter,
    StoreImageTaskCompleteWaiter,
    SubnetAvailableWaiter,
    SystemStatusOkWaiter,
    VolumeAvailableWaiter,
    VolumeDeletedWaiter,
    VolumeInUseWaiter,
    VpcAvailableWaiter,
    VpcExistsWaiter,
    VpcPeeringConnectionDeletedWaiter,
    VpcPeeringConnectionExistsWaiter,
    VpnConnectionAvailableWaiter,
    VpnConnectionDeletedWaiter,
)

try:
    from .service_resource import EC2ServiceResource
except ImportError:
    from builtins import object as EC2ServiceResource  # type: ignore[assignment]

Client = EC2Client

ServiceResource = EC2ServiceResource

__all__ = (
    "BundleTaskCompleteWaiter",
    "Client",
    "ConversionTaskCancelledWaiter",
    "ConversionTaskCompletedWaiter",
    "ConversionTaskDeletedWaiter",
    "CustomerGatewayAvailableWaiter",
    "DescribeAddressTransfersPaginator",
    "DescribeAddressesAttributePaginator",
    "DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator",
    "DescribeByoipCidrsPaginator",
    "DescribeCapacityBlockExtensionHistoryPaginator",
    "DescribeCapacityBlockExtensionOfferingsPaginator",
    "DescribeCapacityBlockOfferingsPaginator",
    "DescribeCapacityBlockStatusPaginator",
    "DescribeCapacityBlocksPaginator",
    "DescribeCapacityReservationBillingRequestsPaginator",
    "DescribeCapacityReservationFleetsPaginator",
    "DescribeCapacityReservationsPaginator",
    "DescribeCarrierGatewaysPaginator",
    "DescribeClassicLinkInstancesPaginator",
    "DescribeClientVpnAuthorizationRulesPaginator",
    "DescribeClientVpnConnectionsPaginator",
    "DescribeClientVpnEndpointsPaginator",
    "DescribeClientVpnRoutesPaginator",
    "DescribeClientVpnTargetNetworksPaginator",
    "DescribeCoipPoolsPaginator",
    "DescribeDhcpOptionsPaginator",
    "DescribeEgressOnlyInternetGatewaysPaginator",
    "DescribeExportImageTasksPaginator",
    "DescribeFastLaunchImagesPaginator",
    "DescribeFastSnapshotRestoresPaginator",
    "DescribeFleetsPaginator",
    "DescribeFlowLogsPaginator",
    "DescribeFpgaImagesPaginator",
    "DescribeHostReservationOfferingsPaginator",
    "DescribeHostReservationsPaginator",
    "DescribeHostsPaginator",
    "DescribeIamInstanceProfileAssociationsPaginator",
    "DescribeImagesPaginator",
    "DescribeImportImageTasksPaginator",
    "DescribeImportSnapshotTasksPaginator",
    "DescribeInstanceConnectEndpointsPaginator",
    "DescribeInstanceCreditSpecificationsPaginator",
    "DescribeInstanceEventWindowsPaginator",
    "DescribeInstanceImageMetadataPaginator",
    "DescribeInstanceStatusPaginator",
    "DescribeInstanceTopologyPaginator",
    "DescribeInstanceTypeOfferingsPaginator",
    "DescribeInstanceTypesPaginator",
    "DescribeInstancesPaginator",
    "DescribeInternetGatewaysPaginator",
    "DescribeIpamPoolsPaginator",
    "DescribeIpamResourceDiscoveriesPaginator",
    "DescribeIpamResourceDiscoveryAssociationsPaginator",
    "DescribeIpamScopesPaginator",
    "DescribeIpamsPaginator",
    "DescribeIpv6PoolsPaginator",
    "DescribeLaunchTemplateVersionsPaginator",
    "DescribeLaunchTemplatesPaginator",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator",
    "DescribeLocalGatewayRouteTableVpcAssociationsPaginator",
    "DescribeLocalGatewayRouteTablesPaginator",
    "DescribeLocalGatewayVirtualInterfaceGroupsPaginator",
    "DescribeLocalGatewayVirtualInterfacesPaginator",
    "DescribeLocalGatewaysPaginator",
    "DescribeMacHostsPaginator",
    "DescribeMacModificationTasksPaginator",
    "DescribeManagedPrefixListsPaginator",
    "DescribeMovingAddressesPaginator",
    "DescribeNatGatewaysPaginator",
    "DescribeNetworkAclsPaginator",
    "DescribeNetworkInsightsAccessScopeAnalysesPaginator",
    "DescribeNetworkInsightsAccessScopesPaginator",
    "DescribeNetworkInsightsAnalysesPaginator",
    "DescribeNetworkInsightsPathsPaginator",
    "DescribeNetworkInterfacePermissionsPaginator",
    "DescribeNetworkInterfacesPaginator",
    "DescribePrefixListsPaginator",
    "DescribePrincipalIdFormatPaginator",
    "DescribePublicIpv4PoolsPaginator",
    "DescribeReplaceRootVolumeTasksPaginator",
    "DescribeReservedInstancesModificationsPaginator",
    "DescribeReservedInstancesOfferingsPaginator",
    "DescribeRouteServerEndpointsPaginator",
    "DescribeRouteServerPeersPaginator",
    "DescribeRouteServersPaginator",
    "DescribeRouteTablesPaginator",
    "DescribeScheduledInstanceAvailabilityPaginator",
    "DescribeScheduledInstancesPaginator",
    "DescribeSecurityGroupRulesPaginator",
    "DescribeSecurityGroupVpcAssociationsPaginator",
    "DescribeSecurityGroupsPaginator",
    "DescribeSnapshotTierStatusPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeSpotFleetInstancesPaginator",
    "DescribeSpotFleetRequestsPaginator",
    "DescribeSpotInstanceRequestsPaginator",
    "DescribeSpotPriceHistoryPaginator",
    "DescribeStaleSecurityGroupsPaginator",
    "DescribeStoreImageTasksPaginator",
    "DescribeSubnetsPaginator",
    "DescribeTagsPaginator",
    "DescribeTrafficMirrorFiltersPaginator",
    "DescribeTrafficMirrorSessionsPaginator",
    "DescribeTrafficMirrorTargetsPaginator",
    "DescribeTransitGatewayAttachmentsPaginator",
    "DescribeTransitGatewayConnectPeersPaginator",
    "DescribeTransitGatewayConnectsPaginator",
    "DescribeTransitGatewayMulticastDomainsPaginator",
    "DescribeTransitGatewayPeeringAttachmentsPaginator",
    "DescribeTransitGatewayPolicyTablesPaginator",
    "DescribeTransitGatewayRouteTableAnnouncementsPaginator",
    "DescribeTransitGatewayRouteTablesPaginator",
    "DescribeTransitGatewayVpcAttachmentsPaginator",
    "DescribeTransitGatewaysPaginator",
    "DescribeTrunkInterfaceAssociationsPaginator",
    "DescribeVerifiedAccessEndpointsPaginator",
    "DescribeVerifiedAccessGroupsPaginator",
    "DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator",
    "DescribeVerifiedAccessInstancesPaginator",
    "DescribeVerifiedAccessTrustProvidersPaginator",
    "DescribeVolumeStatusPaginator",
    "DescribeVolumesModificationsPaginator",
    "DescribeVolumesPaginator",
    "DescribeVpcClassicLinkDnsSupportPaginator",
    "DescribeVpcEndpointConnectionNotificationsPaginator",
    "DescribeVpcEndpointConnectionsPaginator",
    "DescribeVpcEndpointServiceConfigurationsPaginator",
    "DescribeVpcEndpointServicePermissionsPaginator",
    "DescribeVpcEndpointServicesPaginator",
    "DescribeVpcEndpointsPaginator",
    "DescribeVpcPeeringConnectionsPaginator",
    "DescribeVpcsPaginator",
    "EC2Client",
    "EC2ServiceResource",
    "ExportTaskCancelledWaiter",
    "ExportTaskCompletedWaiter",
    "GetAssociatedIpv6PoolCidrsPaginator",
    "GetAwsNetworkPerformanceDataPaginator",
    "GetGroupsForCapacityReservationPaginator",
    "GetInstanceTypesFromInstanceRequirementsPaginator",
    "GetIpamAddressHistoryPaginator",
    "GetIpamDiscoveredAccountsPaginator",
    "GetIpamDiscoveredResourceCidrsPaginator",
    "GetIpamPoolAllocationsPaginator",
    "GetIpamPoolCidrsPaginator",
    "GetIpamResourceCidrsPaginator",
    "GetManagedPrefixListAssociationsPaginator",
    "GetManagedPrefixListEntriesPaginator",
    "GetNetworkInsightsAccessScopeAnalysisFindingsPaginator",
    "GetSecurityGroupsForVpcPaginator",
    "GetSpotPlacementScoresPaginator",
    "GetTransitGatewayAttachmentPropagationsPaginator",
    "GetTransitGatewayMulticastDomainAssociationsPaginator",
    "GetTransitGatewayPolicyTableAssociationsPaginator",
    "GetTransitGatewayPrefixListReferencesPaginator",
    "GetTransitGatewayRouteTableAssociationsPaginator",
    "GetTransitGatewayRouteTablePropagationsPaginator",
    "GetVpnConnectionDeviceTypesPaginator",
    "ImageAvailableWaiter",
    "ImageExistsWaiter",
    "InstanceExistsWaiter",
    "InstanceRunningWaiter",
    "InstanceStatusOkWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
    "InternetGatewayExistsWaiter",
    "KeyPairExistsWaiter",
    "ListImagesInRecycleBinPaginator",
    "ListSnapshotsInRecycleBinPaginator",
    "NatGatewayAvailableWaiter",
    "NatGatewayDeletedWaiter",
    "NetworkInterfaceAvailableWaiter",
    "PasswordDataAvailableWaiter",
    "SearchLocalGatewayRoutesPaginator",
    "SearchTransitGatewayMulticastGroupsPaginator",
    "SecurityGroupExistsWaiter",
    "SecurityGroupVpcAssociationAssociatedWaiter",
    "SecurityGroupVpcAssociationDisassociatedWaiter",
    "ServiceResource",
    "SnapshotCompletedWaiter",
    "SnapshotImportedWaiter",
    "SpotInstanceRequestFulfilledWaiter",
    "StoreImageTaskCompleteWaiter",
    "SubnetAvailableWaiter",
    "SystemStatusOkWaiter",
    "VolumeAvailableWaiter",
    "VolumeDeletedWaiter",
    "VolumeInUseWaiter",
    "VpcAvailableWaiter",
    "VpcExistsWaiter",
    "VpcPeeringConnectionDeletedWaiter",
    "VpcPeeringConnectionExistsWaiter",
    "VpnConnectionAvailableWaiter",
    "VpnConnectionDeletedWaiter",
)
