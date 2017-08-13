.. _aci_bridge_domain:


aci_bridge_domain - Direct access to the APIC API
+++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Offers direct access to the APIC API


Requirements (on host that executes module)
-------------------------------------------

  * ACI Fabric 1.0(3f)+


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
                <tr><td>action<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>post</li><li>get</li><li>delete</li></ul></td>
        <td><div>post, get or delete</div>        </td></tr>
                <tr><td>arp_flooding<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Enable or Disable ARP_Flooding</div>        </td></tr>
                <tr><td>bd_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Bridge Domain</div>        </td></tr>
                <tr><td>gateway_ip<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Gateway IP for subnet</div>        </td></tr>
                <tr><td>host<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>IP Address or hostname of APIC resolvable by Ansible control host</div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Password used to login to the switch</div>        </td></tr>
                <tr><td>protocol<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>https</td>
        <td><ul><li>http</li><li>https</li></ul></td>
        <td><div>Dictates connection protocol to use</div>        </td></tr>
                <tr><td>scope<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>private</td>
        <td></td>
        <td><div>Subent Scope - can be private or public and shared</div>        </td></tr>
                <tr><td>subnet_mask<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Value of the subnet mask</div>        </td></tr>
                <tr><td>tenant_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Tenant Name</div>        </td></tr>
                <tr><td>username<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>admin</td>
        <td></td>
        <td><div>Username used to login to the switch</div>        </td></tr>
                <tr><td>vrf_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>VRF name to associate to the Bridge Domain</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    - aci_bridge_domain:
         action: "{{ action }}"
         tenant_name: "{{ tenant_name }}" 
         bd_name: "{{ bd_name }}" 
         vrf_name: "{{ vrf_name }}"
         arp_flooding: "{{ arp_flooding }}"
         l2_unknown_unicast: "{{ l2_unknown_unicast }}"
         l3_unknown_multicast: "{{ l3_unknown_multicast }}"
         multi_dest: "{{ multi_dest }}" 
         gateway_ip: "{{ gateway_ip }}"
         subnet_mask: "{{ subnet_mask }}"
         scope: "{{ scope }}"
         host: "{{ inventory_hostname }}"
         username: "{{ username }}"
         password: "{{ password }}"
         protocol: "{{ protocol }}"
    
    


Notes
-----

.. note::
    - Tenant should already exist



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
