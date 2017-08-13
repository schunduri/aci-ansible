.. _aci_anp:


aci_anp - Manage top level application network profile objects
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage top level application network profile object, i.e. this does not manage EPGs.


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
                <tr><td>app_profile_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Tenant Name</div>        </td></tr>
                <tr><td>descr<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Description for the AEP</div>        </td></tr>
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

    
    
        aci_anp:
           action: "{{ action }}"
           app_profile_name: "{{ app_profile_name }}"
           tenant_name: "{{ tenant_name }}"
           descr: "{{ descr }}"
           host: "{{ inventory_hostname }}"
           username: "{{ user }}"
           password: "{{ pass }}"
           protocol: "{{ protocol }}"
    


Notes
-----

.. note::
    - T
    - e
    - n
    - a
    - n
    - t
    -  
    - m
    - u
    - s
    - t
    -  
    - e
    - x
    - i
    - s
    - t
    -  
    - p
    - r
    - i
    - o
    - r
    -  
    - t
    - o
    -  
    - u
    - s
    - i
    - n
    - g
    -  
    - t
    - h
    - i
    - s
    -  
    - m
    - o
    - d
    - u
    - l
    - e



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
