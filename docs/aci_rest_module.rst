.. _aci_rest:


aci_rest - Direct access to the Cisco APIC REST API
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Enables the management of the Cisco ACI fabric through direct access to the Cisco APIC REST API.
* More information regarding the Cisco APIC REST API is available from http://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/2-x/rest_cfg/2_1_x/b_Cisco_APIC_REST_API_Configuration_Guide.html.


Requirements (on host that executes module)
-------------------------------------------

  * lxml (when using XML content)
  * xmljson >= 0.1.8 (when using XML content)
  * python 2.7+ (when using xmljson)


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
                <tr><td>content<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>When used instead of <code>src</code>, sets the content of the API request directly.</div><div>This may be convenient to template simple requests, for anything complex use the <span class='module'>template</span> module.</div>        </td></tr>
                <tr><td>hostname<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>IP Address or hostname of APIC resolvable by Ansible control host.</div></br>
    <div style="font-size: small;">aliases: host<div>        </td></tr>
                <tr><td>method<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>get</td>
        <td><ul><li>delete</li><li>get</li><li>post</li></ul></td>
        <td><div>The HTTP method of the request.</div><div>Using <code>delete</code> is typically used for deleting objects.</div><div>Using <code>get</code> is typically used for querying objects.</div><div>Using <code>post</code> is typically used for modifying objects.</div></br>
    <div style="font-size: small;">aliases: action<div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password to use for authentication.</div>        </td></tr>
                <tr><td>path<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>URI being used to execute API calls.</div><div>Must end in <code>.xml</code> or <code>.json</code>.</div></br>
    <div style="font-size: small;">aliases: uri<div>        </td></tr>
                <tr><td>src<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the absolute path of the filname that includes the body of the http request being sent to the ACI fabric.</div></br>
    <div style="font-size: small;">aliases: config_file<div>        </td></tr>
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

    
    - name: Add a tenant
      aci_rest:
        hostname: '{{ inventory_hostname }}'
        username: '{{ aci_username }}'
        password: '{{ aci_password }}'
        method: post
        path: /api/mo/uni.xml
        src: /home/cisco/ansible/aci/configs/aci_config.xml
      delegate_to: localhost
    
    - name: Get tenants
      aci_rest:
        hostname: '{{ inventory_hostname }}'
        username: '{{ aci_username }}'
        password: '{{ aci_password }}'
        method: get
        path: /api/node/class/fvTenant.json
      delegate_to: localhost
    
    - name: Configure contracts
      aci_rest:
        hostname: '{{ inventory_hostname }}'
        username: '{{ aci_username }}'
        password: '{{ aci_password }}'
        method: post
        path: /api/mo/uni.xml
        src: /home/cisco/ansible/aci/configs/contract_config.xml
      delegate_to: localhost
    
    - name: Register leaves and spines
      aci_rest:
        hostname: '{{ inventory_hostname }}'
        username: '{{ aci_username }}'
        password: '{{ aci_password }}'
        validate_certs: no
        method: post
        path: /api/mo/uni/controller/nodeidentpol.xml
        content: |
          <fabricNodeIdentPol>
            <fabricNodeIdentP name="{{ item.name }}" nodeId="{{ item.nodeid }}" status="{{ item.status }}" serial="{{ item.serial }}"/>
          </fabricNodeIdentPol>
      with_items:
      - '{{ apic_leavesspines }}'
      delegate_to: localhost
    
    - name: Wait for all controllers to become ready
      aci_rest:
        hostname: '{{ inventory_hostname }}'
        username: '{{ aci_username }}'
        password: '{{ aci_password }}'
        validate_certs: no
        path: /api/node/class/topSystem.json?query-target-filter=eq(topSystem.role,"controller")
      register: apics
      until: "'totalCount' in apics and apics.totalCount|int >= groups['apic']|count"
      retries: 120
      delay: 30
      delegate_to: localhost
      run_once: yes

Return Values
-------------

Common return values are documented here :doc:`common_return_values`, the following are the fields unique to this module:

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">name</th>
    <th class="head">description</th>
    <th class="head">returned</th>
    <th class="head">type</th>
    <th class="head">sample</th>
    </tr>

        <tr>
        <td> imdata </td>
        <td> Converted output returned by the APIC REST (register this for post-processing) </td>
        <td align=center> always </td>
        <td align=center> string </td>
        <td align=center> [{'error': {'attributes': {'text': 'unknown managed object class foo', 'code': '122'}}}] </td>
    </tr>
            <tr>
        <td> status </td>
        <td> HTTP status code </td>
        <td align=center> always </td>
        <td align=center> int </td>
        <td align=center> 400 </td>
    </tr>
            <tr>
        <td> raw </td>
        <td> The raw output returned by the APIC REST API (xml or json) </td>
        <td align=center> parse error </td>
        <td align=center> string </td>
        <td align=center> <?xml version="1.0" encoding="UTF-8"?><imdata totalCount="1"><error code="122" text="unknown managed object class foo"/></imdata> </td>
    </tr>
            <tr>
        <td> payload </td>
        <td> The (templated) payload send to the APIC REST API (xml or json) </td>
        <td align=center> always </td>
        <td align=center> string </td>
        <td align=center> <foo bar="boo"/> </td>
    </tr>
            <tr>
        <td> totalCount </td>
        <td> Number of items in the imdata array </td>
        <td align=center> always </td>
        <td align=center> string </td>
        <td align=center> 0 </td>
    </tr>
            <tr>
        <td> error_code </td>
        <td> The REST ACI return code, useful for troubleshooting on failure </td>
        <td align=center> always </td>
        <td align=center> int </td>
        <td align=center> 122 </td>
    </tr>
            <tr>
        <td> response </td>
        <td> HTTP response string </td>
        <td align=center> always </td>
        <td align=center> string </td>
        <td align=center> HTTP Error 400: Bad Request </td>
    </tr>
            <tr>
        <td> error_text </td>
        <td> The REST ACI descriptive text, useful for troubleshooting on failure </td>
        <td align=center> always </td>
        <td align=center> string </td>
        <td align=center> unknown managed object class foo </td>
    </tr>
        
    </table>
    </br></br>

Notes
-----

.. note::
    - When using inline-JSON (using ``content``), YAML requires to start with a blank line. Otherwise the JSON statement will be parsed as a YAML mapping (dictionary) and translated into invalid JSON as a result.
    - XML payloads require the ``lxml`` and ``xmljson`` python libraries. For JSON payloads nothing special is needed.
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
