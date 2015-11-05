===========================
Enabling evoque in DevStack
===========================

1. Download DevStack::

     git clone https://git.openstack.org/openstack-dev/devstack
     cd devstack

2. Add this repo as an external repository into your ``local.conf`` file::

     [[local|localrc]]
     enable_plugin evoque https://git.openstack.org/openstack/evoque

3. Run ``stack.sh``.
