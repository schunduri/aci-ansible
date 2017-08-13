.. _aci_epg_domain_binding:


aci_epg_domain_binding - Direct access to the APIC API
++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
  * Cobra SDK


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
        <td><div>post, get, or delete</div>        </td></tr>
                <tr><td>app_profile_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Application Profile Name</div>        </td></tr>
                <tr><td>deploy_immediacy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>on-demand</td>
        <td><ul><li>on-demand</li><li>immediate</li></ul></td>
        <td><div>On Demand | Immediate</div>        </td></tr>
                <tr><td>domain<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>phys</td>
        <td><ul><li>phys</li><li>vmm</li></ul></td>
        <td><div>Dictates domain to be used</div>        </td></tr>
                <tr><td>domain_profile<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Dictates domain profile to be attached</div>        </td></tr>
                <tr><td>encap<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Vlan encapsulation</div>        </td></tr>
                <tr><td>epg_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>EPG Name</div>        </td></tr>
                <tr><td>host<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>IP Address or hostname of APIC resolvable by Ansible control host</div>        </td></tr>
                <tr><td>netflow<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>enabled</td>
        <td><ul><li>enabled</li><li>disabled</li></ul></td>
        <td><div>Enabled | Disabled</div>        </td></tr>
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
                <tr><td>resolution_immediacy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>on-demand</td>
        <td><ul><li>on-demand</li><li>immediate</li><li>pre-provision</li></ul></td>
        <td><div>On Demand | Immediate | Pre-Provision</div>        </td></tr>
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
                <tr><td>vlan_mode<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>dynamic</td>
        <td><ul><li>dynamic</li><li>static</li></ul></td>
        <td><div>Dynamic | Static</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    
    #Physical domain binding
        aci_epg_domain_binding: 
            action: "{{ action }}"
    	tenant_name: "{{ tenant_name }}"
    	app_profile_name: "{{ app_profile_name }}"
    	epg_name: "{{ epg_name }}"
    	encap: "{{ encap }}"
    	domain: phys
    	domain_profile: "{{ domain_profile }}"
    	deploy_immediacy: "{{ deploy_immediacy }}"
            resolution_immediacy: "{{ resolution_immediacy }}" 
    	host: "{{ inventory_hostname }}"
    	username: "{{ user }}"
    	password: "{{ pass }}"
    	protocol: "{{ protocol }}"
    
    
    #VMM domain biniding
        aci_epg_domain_binding: 
            action: "{{ action }}"
            tenant_name: "{{ tenant_name }}"
            app_profile_name: "{{ app_profile_name }}"
            epg_name: "{{ epg_name }}"
            encap: "{{ encap }}"
            domain: vmm
            domain_profile: "{{ domain_profile }}"
            vlan_mode: "{{ vlan_mode }}"
            deploy_immediacy: "{{ deploy_immediacy }}"
            resolution_immediacy: "{{ resolution_immediacy }}" 
            host: "{{ inventory_hostname }}"
            username: "{{ user }}"
            password: "{{ pass }}"
            protocol: "{{ protocol }}"
    


Notes
-----

.. note::
    - EPG Sould be existing



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
