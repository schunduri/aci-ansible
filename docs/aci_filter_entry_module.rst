.. _aci_filter_entry:


aci_filter_entry - Manage filter entries on Cisco ACI fabrics
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage filter entries for a filter on Cisco ACI fabrics.


Requirements (on host that executes module)
-------------------------------------------

  * Tested with ACI Fabric 1.0(3f)+


Options
-------

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
                <tr><td>arp_flag<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>arp_reply</li><li>arp_request</li><li>unspecified</li></ul></td>
        <td><div>The arp flag to use when the ether_type is arp.</div>        </td></tr>
                <tr><td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Description for the Filter Entry.</div>        </td></tr>
                <tr><td>dst_port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>Valid TCP/UDP Port Ranges</li></ul></td>
        <td><div>Used to set both destination start and end ports to the same value when ip_protocol is tcp or udp.</div>        </td></tr>
                <tr><td>dst_port_end<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>Valid TCP/UDP Port Ranges</li></ul></td>
        <td><div>Used to set the destination end port when ip_protocol is tcp or udp.</div>        </td></tr>
                <tr><td>dst_port_start<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>Valid TCP/UDP Port Ranges</li></ul></td>
        <td><div>Used to set the destination start port when ip_protocol is tcp or udp.</div>        </td></tr>
                <tr><td>entry<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Then name of the Filter Entry.</div></br>
    <div style="font-size: small;">aliases: entry_name, name<div>        </td></tr>
                <tr><td>ether_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>arp</li><li>fcoe</li><li>ip</li><li>mac_security</li><li>mpls_ucast</li><li>trill</li><li>unspecified</li></ul></td>
        <td><div>The Ethernet type.</div>        </td></tr>
                <tr><td>filter_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of Filter that the entry should belong to.</div>        </td></tr>
                <tr><td>hostname<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>IP Address or hostname of APIC resolvable by Ansible control host.</div></br>
    <div style="font-size: small;">aliases: host<div>        </td></tr>
                <tr><td>icmp6_msg_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>dst_unreachable</li><li>echo_request</li><li>echo_reply</li><li>neighbor_advertisement</li><li>neighbor_solicitation</li><li>redirect</li><li>time_exceeded</li><li>unspecified</li></ul></td>
        <td><div>ICMPv6 message type; used when ip_protocol is icmpv6.</div>        </td></tr>
                <tr><td>icmp_msg_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>dst_unreachable</li><li>echo</li><li>echo_reply</li><li>src_quench</li><li>time_exceeded</li><li>unspecified</li></ul></td>
        <td><div>ICMPv4 message type; used when ip_protocol is icmp.</div>        </td></tr>
                <tr><td>ip_protocol<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>eigrp</li><li>egp</li><li>icmp</li><li>icmpv6</li><li>igmp</li><li>igp</li><li>l2tp</li><li>ospfigp</li><li>pim</li><li>tcp</li><li>udp</li><li>unspecified</li></ul></td>
        <td><div>The IP Protocol type when ether_type is ip.</div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password to use for authentication.</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>absent</li><li>present</li><li>query</li></ul></td>
        <td><div>present, absent, query</div>        </td></tr>
                <tr><td>stateful<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Determines the statefulness of the filter entry.</div>        </td></tr>
                <tr><td>tenant<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the tenant.</div>        </td></tr>
                <tr><td>timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>30</td>
        <td></td>
        <td><div>The socket level timeout in seconds.</div>        </td></tr>
                <tr><td>use_proxy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If <code>no</code>, it will not use a proxy, even if one is defined in an environment variable on the target hosts.</div>        </td></tr>
                <tr><td>use_ssl<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If <code>no</code>, an HTTP connection will be used instead of the default HTTPS connection.</div>        </td></tr>
                <tr><td>username<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>admin</td>
        <td></td>
        <td><div>The username to use for authentication.</div></br>
    <div style="font-size: small;">aliases: user<div>        </td></tr>
                <tr><td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If <code>no</code>, SSL certificates will not be validated.</div><div>This should only set to <code>no</code> used on personally controlled sites using self-signed certificates.</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    - aci_filter_entry:
        action: "{{ action }}"
        entry: "{{ entry }}"
        tenant: "{{ tenant }}"
        ether_name: "{{  ether_name }}"
        icmp_msg_type: "{{ icmp_msg_type }}"
        filter_name: "{{ filter_name }}"
        descr: "{{ descr }}"
        host: "{{ inventory_hostname }}"
        username: "{{ user }}"
        password: "{{ pass }}"
        protocol: "{{ protocol }}"


Notes
-----

.. note::
    - The tenant used must exist before using this module in your playbook. The :ref:`aci_tenant <aci_tenant>` module can be used for this.
    - The filter used must exist before using this module in your playbook. The :ref:`aci_filter <aci_filter>` module can be used for this.
    - By default, if an environment variable ``<protocol>_proxy`` is set on the target host, requests will be sent through that proxy. This behaviour can be overridden by setting a variable for this task (see `setting the environment <http://docs.ansible.com/playbooks_environment.html>`_), or by using the ``use_proxy`` option.
    - HTTP redirects can redirect from HTTP to HTTPS so you should be sure that your proxy environment for both protocols is correct.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
