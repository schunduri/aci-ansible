#!/usr/bin/python
DOCUMENTATION = '''
---

module: aci_anp
short_description: Manage top level application network profile objects
description:
    -  Manage top level application network profile object, i.e. this does
      not manage EPGs.
author: Cisco
requirements:
    - ACI Fabric 1.0(3f)+
notes: Tenant must exist prior to using this module
options:
   action:
        description:
            - post, get or delete
        required: true
        default: null
        choices: ['post', 'get','delete']
        aliases: []
   tenant_name:
        description:
            - Tenant Name
        required: true
        default: null
        choices: []
        aliases: []
   app_profile_name:
        description:
            - Tenant Name
        required: true
        default: null
        choices: []
        aliases: []
    descr:
        description:
            - Description for the AEP
        required: false
        default: null
        choices: []
        aliases: []
    host:
        description:
            - IP Address or hostname of APIC resolvable by Ansible control host
        required: true
        default: null
        choices: []
        aliases: []
    username:
        description:
            - Username used to login to the switch
        required: true
        default: 'admin'
        choices: []
        aliases: []
    password:
        description:
            - Password used to login to the switch
        required: true
        default: null
        choices: []
        aliases:[]                                                                  
     protocol:
        description:
            - Dictates connection protocol to use
        required: false
        default: https
        choices: ['http', 'https']
        aliases: []
'''

EXAMPLES = '''

    aci_anp:
       action: "{{ action }}"
       app_profile_name: "{{ app_profile_name }}"
       tenant_name: "{{ tenant_name }}"
       descr: "{{ descr }}"
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
            host=dict(required=True),
            username=dict(type='str', default='admin'),
            password=dict(type='str'),
            protocol=dict(choices=['http', 'https'], default='https'),
            app_profile_name=dict(type="str"),
            tenant_name=dict(type="str"),
            descr=dict(type="str"),
        ),
        supports_check_mode=False
    )

    app_profile_name=module.params['app_profile_name']
    tenant_name=module.params['tenant_name']
    descr=module.params['descr']
    descr = str(descr)
    username = module.params['username']
    password = module.params['password']
    protocol = module.params['protocol']
    host = socket.gethostbyname(module.params['host'])
    action = module.params['action']
    post_uri ='api/mo/uni/tn-'+tenant_name+'/ap-'+app_profile_name+'.json'
    get_uri = 'api/node/class/fvAp.json'

    ''' Config payload to enable the physical interface '''
    config_data = {"fvAp":{"attributes":{"name":app_profile_name, "descr":descr }}}
    payload_data = json.dumps(config_data)

    ''' authentication || || Throw an error otherwise'''
    apic = '{0}://{1}/'.format(protocol, host)
    auth = dict(aaaUser=dict(attributes=dict(name=username, pwd=password)))
    url=apic+'api/aaaLogin.json'
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
        req = requests.post(post_url, cookies=authenticate.cookies, data=payload_data, verify=False)
     
    elif action == 'delete':
        req = requests.delete(post_url, cookies=authenticate.cookies, data=payload_data, verify=False)

    elif action == 'get':
        req = requests.get(get_url, cookies=authenticate.cookies, data=payload_data, verify=False)

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
        module.fail_json(msg='error issuing api request',response=response, status=status)

    results = {}
    results['status'] = status
    results['response'] = response
    results['changed'] = changed
    module.exit_json(**results)

from ansible.module_utils.basic import *
if __name__ == "__main__":
    main()
