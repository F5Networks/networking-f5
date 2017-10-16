u"""This module provides unit tests for F5 ML2 driver."""
# coding=utf-8
#
# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from mock import MagicMock
import pytest

from networking_f5.plugins.ml2.drivers.f5.mech_f5networks_bigip \
    import F5NetworksMechanismDriver
from neutron.plugins.ml2 import driver_api as api


@pytest.fixture
def f5_mech_driver():
    return F5NetworksMechanismDriver()


@pytest.fixture
def context():
    return MagicMock()


@pytest.fixture
def agent():
    agent = dict()
    agent['tunnel_types'] = []
    agent['bridge_mappings'] = {}
    agent['binary'] = ""
    return agent


@pytest.fixture
def agent_with_vxlan_vtep():
    return {
        'binary': "f5-oslbaasv2-agent",
        'configurations': {
            'tunnel_types': ['vxlan']
        }
    }


@pytest.fixture
def agent_with_gre_vtep():
    return {
        'binary': "f5-oslbaasv2-agent",
        'configurations': {
            'tunnel_types': ['gre']
        }
    }


@pytest.fixture
def agent_with_all_vtep():
    return {
        'binary': "f5-oslbaasv2-agent",
        'configurations': {
            'tunnel_types': ['gre', 'vxlan']
        }
    }


@pytest.fixture
def agent_bridge_mappings():
    return {
        'binary': "f5-oslbaasv2-agent",
        'configurations': {
            'bridge_mappings': {
                "default": "1,3",
                "physnet1": "1.4"
            }
        }
    }


@pytest.fixture
def agent_hpb_bridge_mappings():
    return {
        'binary': "f5-oslbaasv2-agent",
        'configurations': {
            'bridge_mappings': {
                "default": "1,3",
                "physnet": "1.4"
            },
            'network_segment_physical_network': "physnet1"
        }
    }


@pytest.fixture
def agent_no_bridge_mappings():
    return {
        'binary': "f5-oslbaasv2-agent",
        'configurations': {
            'bridge_mappings': {
            }
        }
    }


@pytest.fixture
def agent_no_binary():
    return {
        'binary': "f5-oslbaasv2-agent",
        'configurations': {
            'bridge_mappings': {
            }
        }
    }


@pytest.fixture
def agent_mismatched_binary():
    return {
        'binary': "not-an-f5-agent",
        'configurations': {
            'bridge_mappings': {
            }
        }
    }


@pytest.fixture
def vlan_segment():
    return {
        api.ID: 'seg-uuid',
        api.NETWORK_TYPE: 'vlan',
        api.SEGMENTATION_ID: 100,
        api.PHYSICAL_NETWORK: 'physnet1'
    }


@pytest.fixture
def vxlan_segment():
    return {
        api.ID: 'seg-uuid',
        api.NETWORK_TYPE: 'vxlan',
        api.SEGMENTATION_ID: 10000,
        api.PHYSICAL_NETWORK: ''
    }


@pytest.fixture
def gre_segment():
    return {
        api.ID: 'seg-uuid',
        api.NETWORK_TYPE: 'gre',
        api.SEGMENTATION_ID: 10000,
        api.PHYSICAL_NETWORK: ''
    }


@pytest.fixture
def flat_segment():
    return {
        api.ID: 'seg-uuid',
        api.NETWORK_TYPE: 'flat',
        api.SEGMENTATION_ID: None,
        api.PHYSICAL_NETWORK: 'physnet-flat'
    }


def test_initialize(f5_mech_driver):
    """Test call to initialize function.

    Nothing to test other than the message that is printed
    """
    f5_mech_driver.initialize()


def test_binding_no_agent_config(f5_mech_driver, context):
    """Test that no binding occurs when agent config is empty.

    The agent that is retured from the context is None.
    The agent that is retured from the context is {}.

    Passes if no binding is performed.
    """
    agent = None
    segment = {}
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, segment, agent)

    assert not retval
    context.set_binding.assert_not_called()

    agent = {}
    segment = {}
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, segment, agent)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_vlan_no_advertised_tunnels(
        f5_mech_driver, context, agent, vlan_segment):
    """Test proper behaviour when agent advertises no tunnels.

    Ensure that no binding occurs for vlan segment with no
    tunnels advertised or physical network bridge mappings
    defined.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vlan_segment, agent)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_flat_no_advertised_tunnels(
        f5_mech_driver, context, agent, flat_segment):
    """Test proper behaviour when agent advertises no tunnels.

    Ensure that no binding occurs for flat segment with no
    tunnels advertised or physical network bridge mappings
    defined.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, flat_segment, agent)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_vxlan_no_advertised_tunnels(
        f5_mech_driver, context, agent, vxlan_segment):
    """Test proper behaviour when agent advertises no tunnels.

    Ensure that no binding occurs for vxlan segment with no
    vxlan tunnelling advertised.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vxlan_segment, agent)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_gre_no_advertised_tunnels(
        f5_mech_driver, context, agent, gre_segment):
    """Test proper behaviour when agent advertises no tunnels.

    Ensure that no binding occurs for vxlan segment with no
    gre tunnelling advertised.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, gre_segment, agent)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_vlan_vxlan_tunnel_advertised(
        f5_mech_driver, context, agent_with_vxlan_vtep, vlan_segment):
    """Test proper behaviour when agent advertises vxlan tunnels.

    The network segment is vlan and there are no bridge mappings
    in the agent configuration.

    Pass if no binding is performed
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vlan_segment, agent_with_vxlan_vtep)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_flat_vxlan_tunnel_advertised(
        f5_mech_driver, context, agent_with_vxlan_vtep, flat_segment):
    """Test proper behaviour when agent advertises no tunnels.

    The network segment is flat and there are no bridge mappings
    in the agent configuration.

    Pass if no binding is performed
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, flat_segment, agent_with_vxlan_vtep)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_gre_segment_vxlan_tunnel_advertised(
        f5_mech_driver, context, agent_with_vxlan_vtep, gre_segment):
    """Test proper behaviour when agent advertises vxlan tunnels.

    The network segment is gre and the only advertised tunnel type
    is vxlan

    Pass if no binding is performed
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, gre_segment, agent_with_vxlan_vtep)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_gre_segment_gre_tunnel_advertised(
        f5_mech_driver, context, agent_with_gre_vtep, gre_segment):
    """Test proper behaviour when agent advertises gre tunnels.

    The network segment is gre and the only advertised tunnel type
    is gre

    Pass if binding is performed with: VIF_TYPE_OTHER and VIF_DETAILS
    are left empty.  This does not disable the port security.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, gre_segment, agent_with_gre_vtep)

    assert retval
    context.set_binding.assert_called_with('seg-uuid', 'other', {})


def test_bind_gre_segment_all_tunnel_advertised(
        f5_mech_driver, context, agent_with_all_vtep, gre_segment):
    """Test proper behaviour when agent advertises all tunnels.

    The network segment is gre and both vxlan and gre tunnel types
    are advertised

    Pass if binding is performed with: VIF_TYPE_OTHER and VIF_DETAILS
    are left empty.  This does not disable the port security.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, gre_segment, agent_with_all_vtep)

    assert retval
    context.set_binding.assert_called_with('seg-uuid', 'other', {})


def test_bind_vxlan_segment_all_tunnel_advertised(
        f5_mech_driver, context, agent_with_all_vtep, vxlan_segment):
    """Test proper behaviour when agent advertises all tunnels.

    The network segment is vxlan and both vxlan and gre tunnel types
    are advertised

    Pass if binding is performed with: VIF_TYPE_OTHER and VIF_DETAILS
    are left empty.  This does not disable the port security.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vxlan_segment, agent_with_all_vtep)

    assert retval
    context.set_binding.assert_called_with('seg-uuid', 'other', {})


def test_bind_physical_segment_bridge_mapping_match(
        f5_mech_driver, context, agent_bridge_mappings, vlan_segment):
    """Test proper behaviour when agent advertises bridge mappgings.

    The segment is type vlan with physical_network physnet1 and there
    is a bridge mapping advertised by the agent that an interface is
    connected to that physical network.

    Pass if binding is performed with: VIF_TYPE_OTHER and VIF_DETAILS
    are left empty.  This does not disable the port security.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vlan_segment, agent_bridge_mappings)

    assert retval
    context.set_binding.assert_called_with('seg-uuid', 'other', {})


def test_bind_physical_segment_no_bridge_mapping_match(
        f5_mech_driver, context, agent_bridge_mappings, flat_segment):
    """Test proper behaviour when agent advertises bridge mappings.

    The segment has physical_network physnet and there
    is not a bridge mapping advertised by the agent that an interface is
    connected to that physical network.

    Pass if no binding id performed
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, flat_segment, agent_bridge_mappings)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_physical_segment_empty_bridge_mapping(
        f5_mech_driver, context, agent_no_bridge_mappings, vlan_segment):
    """Test proper behaviour when agent advertises no bridge mappings.

    The agent configuration does not have any mappings for a physical
    network.

    Pass if no binding is performed.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vlan_segment, agent_no_bridge_mappings)

    assert not retval
    context.set_binding.assert_not_called()


def test_bind_physical_segment_without_hpb_conflict(
        f5_mech_driver, context, agent_hpb_bridge_mappings, vlan_segment):
    """Test the proper behaviour when a HPB segment physical name is configured

    The HPB configuration item is in the agent config but the physical network
    name is different from any of the bridge mapping networks.

    Pass if no binding is performed, we are not binding HPB ports at this
    time to avoid conflict with the HPB mechanism driver.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vlan_segment, agent_hpb_bridge_mappings)

    assert retval
    context.set_binding.assert_called_with('seg-uuid', 'other', {})


def test_bind_physical_segment_with_hpb_conflict(
        f5_mech_driver, context, agent_hpb_bridge_mappings, vlan_segment):
    """Test the proper behaviour when a HPB segment physical name is configured

    The HPB configuration item is in the agent config and the physical network
    name is the same as one of the bridge mapping networks.

    Pass if binding is performed with: VIF_TYPE_OTHER and VIF_DETAILS
    are left empty.  This does not disable the port security.
    """
    bridge_map = agent_hpb_bridge_mappings['configurations']['bridge_mappings']
    bridge_map["physnet1"] = "1.5"
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vlan_segment, agent_hpb_bridge_mappings)

    assert retval
    context.set_binding.assert_called_with('seg-uuid', 'other', {})


def test_bind_no_binary_in_agent_config(
        f5_mech_driver, context, agent_no_binary, vlan_segment):
    """Test the proper behaviour when no binary key is in agent config

    Passes if no binding is performed.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vlan_segment, agent_no_binary)

    assert not retval


def test_bind_mismatched_binary_in_agent_config(
        f5_mech_driver, context, agent_mismatched_binary, vlan_segment):
    """Test the proper behaviour when agent binary key is not supported

    Passes if no binding is performed.
    """
    retval = f5_mech_driver.try_to_bind_segment_for_agent(
        context, vlan_segment, agent_mismatched_binary)

    assert not retval


def test_get_allowed_network_types(
        f5_mech_driver, agent_with_all_vtep, agent_bridge_mappings):
    """Test the correct list of network types given different agent configs

    """
    retval = f5_mech_driver.get_allowed_network_types(agent_with_all_vtep)

    assert sorted(retval) == ["gre", "vxlan"]

    retval = f5_mech_driver.get_allowed_network_types(agent_bridge_mappings)

    assert sorted(retval) == ["flat", "vlan"]
