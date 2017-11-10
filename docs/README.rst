F5 ML2 Driver for OpenStack
===========================

.. sidebar:: **OpenStack version:**

   |openstack|

|Build Status|

.. raw:: html

   <script async defer src="https://f5-openstack-slack.herokuapp.com/slackin.js"></script>

.. toctree:
   titlesonly
   hidden


version |release|
-----------------

|release-notes|


Architecture
------------

The |ml2-long| is an OpenStack Neutron `ML2 Mechanism Driver`_. It provides the means for the |agent-long| to correctly bind Neutron ports to BIG-IP resources.

When you create a new Neutron loadbalancer, the |ml2| does the following:

- checks whether the allocated Neutron port belongs to an F5 device, and
- looks for an active F5 Agent.

If it finds an active F5 Agent, the |ml2| checks the agent configuration to find out if the advertised tunnel type(s) matches the type of the requested port. If it doesn't find a matching tunnel type, the |ml2| checks the physical network bridge mappings (:code:`f5_external_physical_mappings`) for a match. The |ml2| will not bind the port if it doesn't find a match in either of these Agent settings. Likewise, if it doesn't find an Agent configuration file, the |ml2| won't bind the port.

When the |ml2| does find a match for the requested Neutron port in the the |agent| configuration file, it adds the following metadata to the port:

- :code:`device-owner = "network:f5lbaasv2"`
- :code:`host_id = <f5-agent-id>` [#agentid]_

This binds the Neutron port to a specific F5 Agent. [#affinity]_

.. [#agentid] This is the :code:`agent_id` setting in the `F5 Agent configuration file`_.
.. [#affinity] Agent selection and binding follows the same pattern as F5 LBaaSv2 `Agent-tenant affinity`_.

Guides
------

See the `F5 Integration for OpenStack Neutron`_ documentation.


.. index::
   single: ML2 driver; Installation

.. _install ml2-driver:

Installation
------------

You can install the |ml2| using ``pip`` from any release or branch:

.. parsed-literal::

   pip install |ml2_pip_version|
   pip install |ml2_pip_branch|

.. index::
   single: ML2 driver; Neutron setup

.. _configure-neutron ml2-driver:

Neutron Setup
-------------

The steps below set up Neutron to run the |ml2| *after* all other configured ML2 mechanism drivers.

.. note::

   The config file names/locations may vary depending on your OpenStack platform.
   See `Partners`_ for a list of F5's certified OpenStack distribution partners and links to their documentation.


#. Add 'F5Networks' to the end of the list of mechanism_drivers in the Neutron ML2 plugins configuration file: :file:`/etc/neutron/plugins/ml2/ml2_conf.ini`.

   .. code-block:: text

      mechanism_drivers = openvswitch,f5networks


#. Restart Neutron

   .. code-block:: text

      systemctl restart neutron-server  \\ CentOS, Ubuntu 16.04
      service neutron-server restart    \\ Ubuntu 14.04


What's Next
-----------

See `F5 LBaaSv2 Quick Reference`_ to find out how to install and set up the full F5 Integration for OpenStack Neutron.


.. |Build Status| image:: https://travis-ci.org/F5Networks/f5-openstack-ml2-driver.svg?branch=master
   :target: https://travis-ci.org/F5Networks/f5-openstack-ml2-driver
   :alt: Build Status
