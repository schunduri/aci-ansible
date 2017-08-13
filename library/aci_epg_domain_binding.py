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
module: aci_epg_domain_binding
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
    - Cobra SDK
notes:
    - EPG Sould be existing
options:
    action:
        description:
            -  post, get, or delete
        required: true
        choices: ['post', 'get', 'delete']
    tenant_name:
        description:
            - Tenant Name
        required: true
    app_profile_name:
        description:
            - Application Profile Name
        required: true
    epg_name:
        description:
            - EPG Name
        required: true
    domain:
        description:
            - Dictates domain to be used
        default: phys
        choices: ['phys','vmm']
    domain_profile:
        description:
            - Dictates domain profile to be attached
        required: true
    vlan_mode:
        description:
            - Dynamic | Static
        default: dynamic
        choices: ['dynamic', 'static']
    encap:
        description:
            - Vlan encapsulation
        required: true
    deploy_immediacy:
        description:
            - On Demand | Immediate
        default: on-demand
        choices: ['on-demand','immediate']
    resolution_immediacy:
        description:
            - On Demand | Immediate | Pre-Provision
        default: on-demand
        choices: ['on-demand','immediate', 'pre-provision']
    netflow:
        description:
            - Enabled | Disabled
        default: enabled
        choices: ['enabled','disabled']
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
- name: Physical domain binding
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

- name: VMM domain biniding
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
'''

import socket
import json
import requests


def main():
    ''' Ansible module to take all the parameter values from the playbook '''
    module = AnsibleModule(
        argument_spec=dict(
            action=dict(choices=['post', 'get', 'delete']),
            tenant_name=dict(type='str', required=True),
            app_profile_name=dict(type='str', required=True),
            epg_name=dict(type='str', required=True),
            domain=dict(choices=['phys', 'vmm'], default='phys'),
            domain_profile=dict(type='str', required=True),
            vlan_mode=dict(choices=['dynamic', 'static'], default='dynamic'),
            encap=dict(type='str', required=False),
            deploy_immediacy=dict(choices=['immediate', 'on-demand'], default='on-demand'),
            resolution_immediacy=dict(choices=['immediate', 'on-demand', 'pre-provision'], default='on-demand'),
            netflow=dict(choices=['enabled', 'disabled'], default='disabled'),
            host=dict(required=True),
            username=dict(type='str', default='admin'),
            password=dict(type='str'),
            protocol=dict(choices=['http', 'https'], default='https')
        ),
        supports_check_mode=False,
    )

    tenant_name = module.params['tenant_name']
    app_profile_name = module.params['app_profile_name']
    epg_name = module.params['epg_name']
    vlan_mode = module.params['vlan_mode']
    netflow = module.params['netflow']
    domain = module.params['domain']
    if domain == 'vmm':
        domain = 'vmmp-VMware/dom'
    domain_profile = module.params['domain_profile']
    encap = module.params['encap']
    encap = str(encap)
    deploy_immediacy = module.params['deploy_immediacy']
    if deploy_immediacy == 'on-demand':
        deploy_immediacy = 'lazy'
    resolution_immediacy = module.params['resolution_immediacy']
    if resolution_immediacy == 'on-demand':
        resolution_immediacy = 'lazy'
    username = module.params['username']
    password = module.params['password']
    protocol = module.params['protocol']
    host = socket.gethostbyname(module.params['host'])

    action = module.params['action']

    post_uri = '/api/mo/uni/tn-' + tenant_name + '/ap-' + app_profile_name + '/epg-' + epg_name + '/rsdomAtt-[uni/' + domain + '-' + domain_profile + '].json'
    get_uri = '/api/node/class/fvRsDomAtt.json'

    config_data = {
        "fvRsDomAtt": {
            "attributes": {
                "encap": 'vlan-' + encap,
                "instrImedcy": deploy_immediacy,
                "netflowPref": netflow,
                "resImedcy": resolution_immediacy,
            }
        }
    }

    if domain == "vmmp-VMware/dom" and vlan_mode == 'dynamic':
        del config_data['fvRsDomAtt']['attributes']['encap']

    if domain == "phys":
        del config_data['fvRsDomAtt']['attributes']['netflowPref']

    payload_data = json.dumps(config_data)

    ''' authentication || || Throw an error otherwise'''
    apic = "{0}://{1}/".format(protocol, host)

    auth = dict(aaaUser=dict(attributes=dict(name=username, pwd=password)))
    url = apic + 'api/aaaLogin.json'

    authenticate = requests.post(url, data=json.dumps(auth), timeout=2, verify=False)

    if authenticate.status_code != 200:
        module.fail_json(msg='could not authenticate to apic', status=authenticate.status_code, response=authenticate.text)

    ''' Sending the request to APIC '''
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

    ''' Check response status and parse it for status || Throw an error otherwise '''
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
