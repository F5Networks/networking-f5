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

The |ml2-long| is an OpenStack Neutron `ML2 Mechanism Driver`_. When a user creates or updates a Neutron port (for example, as part of the :code:`neutron lbaas loadbalancer create` command), the |ml2| adds metadata that identify the port as belonging to an F5 device. This allows the |agent-long| to correctly identify and bind Neutron ports to BIG-IP resources.

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

   pip install https://github.com/F5Networks/f5-openstack-ml2-driver/releases/tag/v%(version)s
   pip install https://github.com/F5Networks/f5-openstack-ml2-driver@%(version)s

.. index::
   single: ML2 driver; Neutron setup

.. _configure-neutron ml2-driver:

Neutron Setup
-------------

The steps below to tell Neutron to use the |ml2| *after* all other configured ML2 mechanism drivers.

.. note::

   The config file names/locations may vary depending on your OpenStack platform.
   See `Partners`_ for a list of F5's certified OpenStack distribution partners and links to their documentation.


#. Add 'F5Networks' to the :code:`mechanism_drivers` section of the Neutron ml2_plugins configuration file: :file:`/etc/neutron/ml2_plugins.ini`.

   .. code-block:: text

      mechanism_drivers = [already defined plugins], append: "f5networks"


#. Restart Neutron

   .. code-block:: text

      systemctl restart neutron-server  \\ CentOS
      service neutron-server restart    \\ Ubuntu

What's Next
-----------

See `F5 LBaaSv2 Quick Reference`_ to find out how to install and set up the F5 Integration for OpenStack Neutron LBaaSv2.



.. |Build Status| image:: https://travis-ci.org/F5Networks/f5-openstack-lbaasv2-driver.svg?branch=liberty
   :target: https://travis-ci.org/F5Networks/f5-openstack-lbaasv2-driver
   :alt: Build Status
