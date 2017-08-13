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
module: aci_span_src_group
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
            - post, get, or delete
        required: true
        choices: ['post','get', 'delete']
    tenant_name:
        description:
            - Tenant Name
        required: true
    src_group:
        description:
            - Span source group name
        required: true
    dst_group:
        description:
            - Span destination group name
        required: true
    admin_state:
        description:
            - Enable or Disable admin state
        default: 'enabled'
        choices: ['enabled','disabled']
    descr:
        description:
            - Description for Span source group
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

EXAMPLES = '''
- aci_span_src_group:
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
'''

import socket
import json
import requests


def main():
    ''' Ansible module to take all the parameter values from the playbook '''

    module = AnsibleModule(
        argument_spec=dict(
            action=dict(choices=['get', 'post', 'delete'], required=False),
            src_group=dict(type='str'),
            dst_group=dict(type='str'),
            admin_state=dict(choices=['enabled', 'disabled'], default='enabled'),
            tenant_name=dict(type='str'),
            descr=dict(type='str', required=False),
            host=dict(required=True),
            username=dict(type='str', default='admin'),
            password=dict(type='str'),
            protocol=dict(choices=['http', 'https'], default='https'),
        ),
        supports_check_mode=False,
    )

    host = socket.gethostbyname(module.params['host'])
    username = module.params['username']
    password = module.params['password']
    protocol = module.params['protocol']
    action = module.params['action']

    admin_state = module.params['admin_state']
    src_group = module.params['src_group']
    dst_group = module.params['dst_group']
    tenant_name = module.params['tenant_name']
    descr = module.params['descr']

    post_uri = '/api/mo/uni/tn-' + tenant_name + '/srcgrp-' + src_group + '.json'
    get_uri = '/api/node/class/spanSrcGrp.json'

    config_data = {
        "spanSrcGrp": {
            "attributes": {
                "adminSt": admin_state,
                "descr": descr,
                "name": src_group
            },
            "children": [{
                "spanSpanLbl": {
                    "attributes": {
                        "name": dst_group,
                    }
                }
            }]
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

    if action == 'post':
        req = requests.post(post_url, cookies=authenticate.cookies,
                            data=payload_data, verify=False)
    elif action == 'get':
        req = requests.get(get_url, cookies=authenticate.cookies,
                           data=payload_data, verify=False)
    elif action == 'delete':
        req = requests.delete(post_url, cookies=authenticate.cookies, data=payload_data, verify=False)

    response = req.text
    status = req.status_code

    changed = False
    if req.status_code == 200:
        if action == 'post':
            changed = True
        else:
            changed = False
    else:
        module.fail_json(msg='error issuing api request',
                         response=response, status=status)

    results = {}
    results['status'] = status
    results['response'] = response
    results['changed'] = changed

    module.exit_json(**results)

from ansible.module_utils.basic import *
if __name__ == "__main__":
    main()
