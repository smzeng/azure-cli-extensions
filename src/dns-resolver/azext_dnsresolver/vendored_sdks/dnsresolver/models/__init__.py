# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import DnsForwardingRuleset
    from ._models_py3 import DnsForwardingRulesetListResult
    from ._models_py3 import DnsForwardingRulesetPatch
    from ._models_py3 import DnsResolver
    from ._models_py3 import DnsResolverListResult
    from ._models_py3 import DnsResolverPatch
    from ._models_py3 import ForwardingRule
    from ._models_py3 import ForwardingRuleListResult
    from ._models_py3 import ForwardingRulePatch
    from ._models_py3 import InboundEndpoint
    from ._models_py3 import InboundEndpointListResult
    from ._models_py3 import InboundEndpointPatch
    from ._models_py3 import IpConfiguration
    from ._models_py3 import OutboundEndpoint
    from ._models_py3 import OutboundEndpointListResult
    from ._models_py3 import OutboundEndpointPatch
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import SubResource
    from ._models_py3 import SubResourceListResult
    from ._models_py3 import SystemData
    from ._models_py3 import TargetDnsServer
    from ._models_py3 import TrackedResource
    from ._models_py3 import VirtualNetworkDnsForwardingRuleset
    from ._models_py3 import VirtualNetworkDnsForwardingRulesetListResult
    from ._models_py3 import VirtualNetworkLink
    from ._models_py3 import VirtualNetworkLinkListResult
    from ._models_py3 import VirtualNetworkLinkPatch
except (SyntaxError, ImportError):
    from ._models import CloudErrorBody  # type: ignore
    from ._models import DnsForwardingRuleset  # type: ignore
    from ._models import DnsForwardingRulesetListResult  # type: ignore
    from ._models import DnsForwardingRulesetPatch  # type: ignore
    from ._models import DnsResolver  # type: ignore
    from ._models import DnsResolverListResult  # type: ignore
    from ._models import DnsResolverPatch  # type: ignore
    from ._models import ForwardingRule  # type: ignore
    from ._models import ForwardingRuleListResult  # type: ignore
    from ._models import ForwardingRulePatch  # type: ignore
    from ._models import InboundEndpoint  # type: ignore
    from ._models import InboundEndpointListResult  # type: ignore
    from ._models import InboundEndpointPatch  # type: ignore
    from ._models import IpConfiguration  # type: ignore
    from ._models import OutboundEndpoint  # type: ignore
    from ._models import OutboundEndpointListResult  # type: ignore
    from ._models import OutboundEndpointPatch  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import SubResourceListResult  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TargetDnsServer  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import VirtualNetworkDnsForwardingRuleset  # type: ignore
    from ._models import VirtualNetworkDnsForwardingRulesetListResult  # type: ignore
    from ._models import VirtualNetworkLink  # type: ignore
    from ._models import VirtualNetworkLinkListResult  # type: ignore
    from ._models import VirtualNetworkLinkPatch  # type: ignore

from ._dns_resolver_management_client_enums import (
    CreatedByType,
    DnsResolverState,
    ForwardingRuleState,
    IpAllocationMethod,
    ProvisioningState,
)

__all__ = [
    'CloudErrorBody',
    'DnsForwardingRuleset',
    'DnsForwardingRulesetListResult',
    'DnsForwardingRulesetPatch',
    'DnsResolver',
    'DnsResolverListResult',
    'DnsResolverPatch',
    'ForwardingRule',
    'ForwardingRuleListResult',
    'ForwardingRulePatch',
    'InboundEndpoint',
    'InboundEndpointListResult',
    'InboundEndpointPatch',
    'IpConfiguration',
    'OutboundEndpoint',
    'OutboundEndpointListResult',
    'OutboundEndpointPatch',
    'ProxyResource',
    'Resource',
    'SubResource',
    'SubResourceListResult',
    'SystemData',
    'TargetDnsServer',
    'TrackedResource',
    'VirtualNetworkDnsForwardingRuleset',
    'VirtualNetworkDnsForwardingRulesetListResult',
    'VirtualNetworkLink',
    'VirtualNetworkLinkListResult',
    'VirtualNetworkLinkPatch',
    'CreatedByType',
    'DnsResolverState',
    'ForwardingRuleState',
    'IpAllocationMethod',
    'ProvisioningState',
]