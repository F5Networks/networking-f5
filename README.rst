.. raw:: html

   <!--
   Copyright 2016-2017 F5 Networks Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   -->

F5 ML2 Mechanism Driver for OpenStack Neutron
=============================================

|Build Status| |slack badge|

.. image:: https://coveralls.io/repos/github/F5Networks/networking-f5/badge.svg
   :target: https://coveralls.io/github/F5Networks/networking-f5

Introduction
------------

This repo houses the F5 ML2 Mechanism Driver for OpenStack Neutron and associated networking code. The F5 mechanism driver works with the F5 Agent for OpenStack Neutron to bind Neutron ports to loadbalancer resources that belong to F5 BIG-IP devices.

Compatibility
-------------

The F5 Mechanism Driver is compatible with OpenStack releases from Mitaka forward.

See the `F5 OpenStack Releases and Support Matrix <http://clouddocs.f5.com/cloud/openstack/latest/support/releases_and_versioning.html>`_ for more information.

Documentation
-------------

Documentation is published on `clouddocs.f5.com <http://clouddocs.f5.com/products/openstack/ml2-driver/latest>`_.

Filing Issues
-------------

If you find an issue, we would love to hear about it.
Please file an `issue <https://github.com/F5Networks/networking-f5/issues>`_ in this repository.
Use the issue template to tell us as much as you can about what you found, how you found it, your environment, etc.
Admins will triage your issue and assign it for a fix based on the priority level assigned.
We also welcome you to file issues for feature requests.

Contributing
------------

See `Contributing <CONTRIBUTING.md>`_.


Copyright
---------

Copyright 2017 F5 Networks Inc.

Support
-------

See `Support <SUPPORT>`_.

License
-------

Apache V2.0
~~~~~~~~~~~

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Contributor License Agreement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Individuals or business entities who contribute to this project must complete and submit the `F5 Contributor License
Agreement <http://clouddocs.f5.com/cloud/openstack/latest/support/cla_landing.html>`_ to Openstack_CLA@f5.com prior to their code submission being included in this project.


.. |Build Status| image:: https://travis-ci.org/F5Networks/networking-f5.svg?branch=master
   :target: https://travis-ci.org/F5Networks/networking-f5?branch=master
.. |slack badge| image:: https://f5-openstack-slack.herokuapp.com/badge.svg
   :target: https://f5-openstack-slack.herokuapp.com/
   :alt: Slack