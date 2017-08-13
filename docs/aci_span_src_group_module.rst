.. _aci_span_src_group:


aci_span_src_group - Direct access to the APIC API
++++++++++++++++++++++++++++++++++++++++++++++++++

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
        <td><div>post, get, or delete</div>        </td></tr>
                <tr><td>admin_state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>enabled</td>
        <td><ul><li>enabled</li><li>disabled</li></ul></td>
        <td><div>Enable or Disable admin state</div>        </td></tr>
                <tr><td>descr<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Description for Span source group</div>        </td></tr>
                <tr><td>dst_group<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Span destination group name</div>        </td></tr>
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
                <tr><td>src_group<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Span source group name</div>        </td></tr>
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
        </table>
    </br>



Examples
--------

 ::

    
    
        aci_span_src_group: 
    	action:"{{ action }}" 	
    	tenant_name:"{{ tenant_name }}" 
    	src_group:"{{ src_group }}" 
    	dst_group:"{{ dst_group }}" 
    	admin_state:"{{ admin_state }}" 
    	descr:"{{ descr }}" 
    	host:"{{ inventory_hostname }}" 
    	username:"{{ username }}" 
    	password:"{{ password }}"
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
