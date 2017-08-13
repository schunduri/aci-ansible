.. _aci_filter:


aci_filter - Manages top level filter objects on Cisco ACI fabrics
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manages top level filter objects on Cisco ACI fabrics.
* This modules does not manage filter entries, see :ref:`aci_filter_entry <aci_filter_entry>` for this functionality.


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
                <tr><td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Description for the filter.</div></br>
    <div style="font-size: small;">aliases: descr<div>        </td></tr>
                <tr><td>filter<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The name of the filter.</div></br>
    <div style="font-size: small;">aliases: filter_name, name<div>        </td></tr>
                <tr><td>hostname<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>IP Address or hostname of APIC resolvable by Ansible control host.</div></br>
    <div style="font-size: small;">aliases: host<div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password to use for authentication.</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>absent</li><li>present</li><li>query</li></ul></td>
        <td><div>Use <code>present</code> or <code>absent</code> for adding or removing.</div><div>Use <code>query</code> for listing an object or multiple objects.</div>        </td></tr>
                <tr><td>tenant<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The name of the tenant.</div></br>
    <div style="font-size: small;">aliases: tenant_name<div>        </td></tr>
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

    
    - name: Add a new filter to a tenant
      aci_filter:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        filter: web_filter
        description: Filter for web protocols
        tenant: production
        state: present
    
    - name: Remove a filter for a tenant
      aci_filter:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        filter: web_filter
        tenant: production
        state: absent
    
    - name: Query a filter of a tenant
      aci_filter:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        filter: web_filter
        tenant: production
        state: query
    
    - name: Query all filters for a tenant
      aci_filter:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        tenant: production
        state: query


Notes
-----

.. note::
    - The tenant used must exist before using this module in your playbook. The :ref:`aci_tenant <aci_tenant>` module can be used for this.
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
