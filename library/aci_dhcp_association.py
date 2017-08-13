#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: aci_dhcp_assocation
short_description: Direct access to the APIC API
description:
    - Offers direct access to the APIC API
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
- Jacob McGill (@jmcgill298)
version_added: '2.4'
requirements:
    - ACI Fabric 1.0(3f)+
notes:
    - Tenant should already exist
options:
   action:
        description:
            - post, get, and delete
        required: true
        choices: ['post','get','delete']
   tenant_name:
        description:
            - Tenant Name
        required: true
   bd_name:
        description:
            - Bridge Domain
        required: true
   dhcp_name:
        description:
            - Name for the DHCP relay label to be added
   dhcp_scope:
        description:
            - DHCP Relay label scope can be either tenant or infra
        default: 'infra'
        choices: ['tenant','infra']
   host:
        description:
            - IP Address or hostname of APIC resolvable by Ansible control host
        required: true
   username:
        description:
            - Username used to login to the switch
        required: true
        default: 'admin'
   password:
        description:
            - Password used to login to the switch
        required: true
   protocol:
        description:
            - Dictates connection protocol to use
        default: https
        choices: ['http', 'https']
'''

EXAMPLES = r'''
- aci_dhcp_association:
    action: "{{ action }}"
    tenant_name: "{{ tenant_name }}"
    bd_name: "{{ bd_name }}"
    dhcp_name: "{{ dhcp_name }}"
    dhcp_scope: "{{ dhcp_scope }}"
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    protocol: "{{ protocol }}"
'''

import socket
import json
import requests


def main():
    ''' Ansible module to take all the parameter values from the playbook '''

    module = AnsibleModule(
        argument_spec=dict(
            action=dict(choices=['get', 'post', 'delete'], required=False),
            tenant_name=dict(type='str', required=True),
            bd_name=dict(type='str', required=True),
            dhcp_name=dict(type="str"),
            dhcp_scope=dict(choices=['tenant', 'infra'], default='infra'),
            host=dict(required=True),
            username=dict(type='str', default='admin'),
            password=dict(type='str'),
            protocol=dict(choices=['http', 'https'], default='https'),
        ),
        supports_check_mode=False,
    )

    tenant_name = module.params['tenant_name']
    host = socket.gethostbyname(module.params['host'])
    bd_name = module.params['bd_name']
    username = module.params['username']
    password = module.params['password']
    protocol = module.params['protocol']
    action = module.params['action']

    # DHCP Relay Labels
    dhcp_name = module.params['dhcp_name']
    dhcp_scope = module.params['dhcp_scope']

    post_uri = 'api/mo/uni/tn-' + tenant_name + '/BD-' + bd_name + '.json'
    get_uri = 'api/node/class/dhcpLbl.json'
    delete_uri = 'api/mo/uni/tn-' + tenant_name + '/BD-' + bd_name + '/dhcplbl-' + dhcp_name + '.json'

    config_data = {
        "fvBD": {
            "attributes": {
                "name": bd_name
            },
            "children": [
                {
                    "dhcpLbl": {
                        "attributes": {
                            "name": dhcp_name,
                            "owner": dhcp_scope
                        }
                    }
                }
            ]

        }
    }

    payload_data = json.dumps(config_data)

    apic = '{0}://{1}/'.format(protocol, host)

    auth = dict(aaaUser=dict(attributes=dict(name=username,
                                             pwd=password)))
    url = apic + 'api/aaaLogin.json'

    authenticate = requests.post(url, data=json.dumps(auth), timeout=2,
                                 verify=False)

    if authenticate.status_code != 200:
        module.fail_json(msg='could not authenticate to apic',
                         status=authenticate.status_code,
                         response=authenticate.text)

    if post_uri.startswith('/'):
        post_uri = post_uri[1:]
    post_url = apic + post_uri

    if get_uri.startswith('/'):
        get_uri = get_uri[1:]
    get_url = apic + get_uri

    if delete_uri.startswith('/'):
        delete_uri = delete_uri[1:]
    delete_url = apic + delete_uri

    bd_get = apic + '/api/class/fvBD.json'
    if action == 'post':
        get_bd = requests.get(bd_get, cookies=authenticate.cookies,
                              data=payload_data, verify=False)
        data = json.loads(get_bd.text)
        count = data['totalCount']
        count = int(count)
        bridge_domain_list = []
        if get_bd.status_code == 200:
            for name in range(0, count):
                bd = data['imdata'][name]['fvBD']['attributes']['name']
                bridge_domain_list.append(bd)
        if bd_name in bridge_domain_list:
            req = requests.post(post_url, cookies=authenticate.cookies, data=payload_data, verify=False)
        else:
            module.fail_json(msg='Bridge Domain doesnt exist. Please create bridge domain before creating DHCP Relay Label')

    elif action == 'get':
        req = requests.get(get_url, cookies=authenticate.cookies,
                           data=payload_data, verify=False)
    elif action == 'delete':
        req = requests.delete(delete_url, cookies=authenticate.cookies, data=payload_data, verify=False)

    response = req.text
    status = req.status_code

    changed = False
    if req.status_code == 200:
        if action == 'post':
            changed = True
        else:
            changed = False
    else:
        module.fail_json(msg=response,
                         response=response, status=status)

    results = {}
    results['status'] = status
    results['response'] = response
    results['changed'] = changed

    module.exit_json(**results)


from ansible.module_utils.basic import *
if __name__ == "__main__":
    main()
