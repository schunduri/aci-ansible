.. _aci_context:


aci_context - Manage private networks (aka. contexts) on Cisco ACI fabrics
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage private networks (aka. contexts) on Cisco ACI fabrics.
* Each context is a private network associated to a tenant, i.e. VRF.


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
                <tr><td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Description for the VRF.</div>        </td></tr>
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
                <tr><td>policy_control_direction<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>egress</li><li>ingress</li></ul></td>
        <td><div>Determines if the policy should be enforced by the fabric on ingress or egress.</div>        </td></tr>
                <tr><td>policy_control_preference<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>enforced</li><li>unenforced</li></ul></td>
        <td><div>Determines if the Fabric should enforce Contrac Policies.</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>absent</li><li>present</li><li>query</li></ul></td>
        <td><div>Use <code>present</code> or <code>absent</code> for adding or removing.</div><div>Use <code>query</code> for listing an object or multiple objects.</div>        </td></tr>
                <tr><td>tenant<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the Tenant the VRF should belong to.</div></br>
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
                <tr><td>vrf<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the VRF.</div></br>
    <div style="font-size: small;">aliases: context, name, vrf_name<div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    - name: Add a new VRF to a tenant
      aci_context:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        vrf: vrf_lab
        tenant: lab_tenant
        descr: Lab VRF
        policy_control_preference: enforced
        policy_control_direction: ingress
        state: present
    
    - name: Remove a VRF for a tenant
      aci_context:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        vrf: vrf_lab
        tenant: lab_tenant
        state: absent
    
    - name: Query a VRF of a tenant
      aci_context:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        vrf: vrf_lab
        tenant: lab_tenant
        state: query
    
    - name: Query all VRFs
      aci_context:
        hostname: apic
        username: admin
        password: SomeSecretPassword
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
