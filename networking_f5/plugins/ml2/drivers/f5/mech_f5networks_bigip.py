u"""This module provides a ML2 driver for BIG-IP."""
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


from oslo_log import log

from neutron.extensions import portbindings
from neutron.plugins.common import constants as p_constants
from neutron.plugins.ml2 import driver_api as api
from neutron.plugins.ml2.drivers import mech_agent

from networking_f5.plugins.ml2.drivers.f5 import constants

LOG = log.getLogger(__name__)


class F5NetworksMechanismDriver(mech_agent.SimpleAgentMechanismDriverBase):
    """F5NetworksMechanismDriver implementation.

    Provides BIG-IP with Neutron Port Binding capability.
    """

    def __init__(self,
                 agent_type=constants.AGENT_TYPE_LOADBALANCERV2,
                 vif_type=portbindings.VIF_TYPE_OTHER,
                 vif_details=dict(),
                 supported_vnic_types=[constants.VNIC_F5_APPLIANCE,
                                       portbindings.VNIC_BAREMETAL]):
        """Create F5NetworksMechanismDriver."""
        super(F5NetworksMechanismDriver, self).__init__(
            agent_type=constants.AGENT_TYPE_LOADBALANCERV2,
            vif_type=portbindings.VIF_TYPE_OTHER,
            vif_details=dict(),
            supported_vnic_types=[constants.VNIC_F5_APPLIANCE,
                                  portbindings.VNIC_BAREMETAL])

        self.vif_type = vif_type
        self.vif_details = vif_details

    def initialize(self):
        """Initialize the F5Networks mechanism driver."""
        LOG.debug("F5Networks Mechanism Driver Initialize")

    def get_mappings(self, agent):
        """Return the agent's bridge or interface mappings."""
        bridge_mappings = dict()

        if agent:
            agent_config = agent.get('configurations', {})
            agent_config.get('configurations', {})

            bridge_mappings = agent_config.get(
                constants.AGENT_BRIDGE_MAPPINGS, {})

        return bridge_mappings

    def get_allowed_network_types(self, agent=None):
        """Return a list of network types that the agent can bind."""
        allowed_network_types = list()

        if agent:
            agent_config = agent.get('configurations', {})

            tunnel_types = agent_config.get(constants.AGENT_TUNNEL_TYPES, [])

            allowed_network_types.extend(tunnel_types)

            bridge_mappings = agent_config.get(
                constants.AGENT_BRIDGE_MAPPINGS, {})
            if bridge_mappings:
                allowed_network_types.extend(
                    [p_constants.TYPE_FLAT, p_constants.TYPE_VLAN])

        return allowed_network_types

    def try_to_bind_segment_for_agent(self, context, segment, agent):
        """Try to bind with segment for agent.

        :param context: PortContext instance describing the port
        :param segment: segment dictionary describing segment to bind
        :param agent: agents_db entry describing agent to bind
        :returns: True iff segment has been bound for agent

        Called outside any transaction during bind_port() so that
        derived MechanismDrivers can use agent_db data along with
        built-in knowledge of the corresponding agent's capabilities
        to attempt to bind to the specified network segment for the
        agent.
        """
        # Can we bind the port to this segment?
        bind_segment = self.check_segment_for_agent(segment, agent)
        if bind_segment:
            # Yes, set the binding for now the vif details are
            # empty.
            vif_details = dict()
            context.set_binding(
                segment[api.ID],
                portbindings.VIF_TYPE_OTHER,
                vif_details)

        return bind_segment

    def check_segment_for_agent(self, segment, agent):
        """Check if it is possible to bind this segment to the agent."""
        if not agent:
            LOG.warn("No agent passed in to binding call.")
            return False

        agent_config = agent.get('configurations', {})

        agent_binary = agent.get('binary', "")
        if agent_binary not in constants.AGENT_BINARIES:
            LOG.debug("F5 mech driver does not support agent %s.",
                      agent_binary)
            return False

        # Get the supporting tunnel types (e.g. vxlan, gre)
        tunnel_types = agent_config.get(constants.AGENT_TUNNEL_TYPES, [])

        # Get the BigIP interface to physicaL_network mappings to
        # determine what vlan/flat networks the BigIP is connected to.
        bridge_mappings = agent_config.get(constants.AGENT_BRIDGE_MAPPINGS, {})

        # Get the physical network of the Hierachical Port Binding
        # network segment.
        hpb_physical_network_segment = agent_config.get(
            constants.AGENT_HPB_PHYSICAL_NETWORK, None)

        network_type = segment.get(api.NETWORK_TYPE, "")

        # The criteria for port binding is if the segment network type is:
        # 1. If the segment network type is the same as one of the
        #    advertised tunnel types, the port can be bound.
        # 2. If the segment network type is 'flat' or 'vlan' and the
        #    agent advertises a bridge mapping between the physical_network
        #    of the segment and an interface on the BIG-IP, the port can
        #    be bound.
        # 3. If the agent is advertising the physical network name of
        #    a segment in a hierarchical network, the port can be bound
        #    as long as the segment physical_network matches that of the
        #    agent's
        bind_segment = False
        if network_type in tunnel_types:
            LOG.debug("binding segment with tunnel type: %s" % network_type)
            bind_segment = True
        elif network_type in [p_constants.TYPE_FLAT, p_constants.TYPE_VLAN]:
            physnet = segment[api.PHYSICAL_NETWORK]
            if physnet in bridge_mappings:
                LOG.debug("binding segment with network type: %(network_type)s"
                          " on physical network %(physical_network)s.",
                          {'network_type': network_type,
                           'physical_network': physnet})
                bind_segment = True
            elif physnet == hpb_physical_network_segment:
                LOG.debug("binding segment with network type: %(network_type)s"
                          " on hierarchical network, physical network "
                          "%(physical_network)s",
                          {'network_type': network_type,
                           'physical_network': physnet})
                bind_segment = True

        return bind_segment
