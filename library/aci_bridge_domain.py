#!/usr/bin/python

DOCUMENTATION = '''
---

module: aci_bridge_domain
short_description: Direct access to the APIC API
description:
    - Offers direct access to the APIC API
author: Cisco
requirements:
    - ACI Fabric 1.0(3f)+
notes:
    - Tenant should already exist
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
   bd_name:
        description:
            - Bridge Domain
        required: true
        default: null
        choices: []
        aliases: []
   vrf_name:
        description:
            - VRF name to associate to the Bridge Domain
        required: true
        default: null
        choices: []
        aliases: []
   arp_flooding:
        description:
            - Enable or Disable ARP_Flooding
        required: true
        default: null
        choices: []
        aliases: []
    gateway_ip:
        description:
            - Gateway IP for subnet
        required: true
        default: null
        choices: []
        aliases: [] 
    subnet_mask:
        description:
            - Value of the subnet mask 
        required: true 
        default: null 
        choices: []
        aliases: [] 
    scope:
        description:
            - Subent Scope - can be private or public and shared  
        required: false 
        default: 'private'
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
        aliases: []
    protocol:
        description:
            - Dictates connection protocol to use
        required: false
        default: https
        choices: ['http', 'https']
        aliases: []
'''

EXAMPLES =  '''

 aci_bridge_domain:
     action: "{{ action }}"
     tenant_name: "{{ tenant_name }}" 
     bd_name: "{{ bd_name }}" 
     vrf_name: "{{ vrf_name }}"
     arp_flooding: "{{ arp_flooding }}"
     l2_unknown_unicast: "{{ l2_unknown_unicast }}"
     l3_unknown_multicast: "{{ l3_unknown_multicast }}"
     multi_dest: "{{ multi_dest }}" 
     gateway_ip: "{{ gateway_ip }}"
     subnet_mask: "{{ subnet_mask }}"
     scope: "{{ scope }}"
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

    module = AnsibleModule(argument_spec=dict(
        action=dict(choices=['get', 'post', 'delete']),
        tenant_name=dict(type='str', required=True),
        bd_name=dict(type='str', required=True),
        arp_flooding=dict(choices=['yes','no'], default="yes"),
        l2_unknown_unicast=dict(choices=['proxy','flood'], default='proxy'),
        l3_unknown_multicast=dict(choices=['flood','opt-flood'], default='flood'),
        multi_dest=dict(choices=['bd-flood','drop','encap-flood'], default='bd-flood'),
        vrf_name=dict(type='str'),
        gateway_ip=dict(type='str', default=0, required=False),
        subnet_mask=dict(type='str', default=0, required=False),
        scope=dict(type='str',default='private'),
        host=dict(required=True),
        username=dict(type='str', default='admin'),
        password=dict(type='str'),
        protocol=dict(choices=['http', 'https'], default='http'),
        ), supports_check_mode=False)

    tenant_name = module.params['tenant_name']
    host = socket.gethostbyname(module.params['host'])
    bd_name = module.params['bd_name']
    arp_flooding = module.params['arp_flooding']
    l2_unknown_unicast = module.params['l2_unknown_unicast']
    l3_unknown_multicast = module.params['l3_unknown_multicast']
    multi_dest = module.params['multi_dest']
    vrf_name = module.params['vrf_name']
    username = module.params['username']
    password = module.params['password']
    protocol = module.params['protocol']
    action = module.params['action']

    #subnet
    gateway_ip = module.params['gateway_ip']
    subnet_mask = module.params['subnet_mask']
    if gateway_ip != 0  and subnet_mask != 0:
       ip = gateway_ip + "/" + subnet_mask
    else:
       ip = ''
    scope = module.params['scope']
   
    post_uri = 'api/mo/uni/tn-' + tenant_name + '/BD-' + bd_name + '.json'
    get_uri = 'api/node/class/fvBD.json'

    config_data =  {
         "fvBD": {
             "attributes": {
                  "descr": "test",
                  "arpFlood": arp_flooding,
                  "unkMacUcastAct":l2_unknown_unicast,
                  "unkMcastAct": l3_unknown_multicast,
                  "multiDstPktAct": multi_dest
               },
              "children":[{
                   "fvRsCtx": {
                      "attributes": {
                          "tnFvCtxName": vrf_name
                         }
                      }
                  }
                ]

           }
     }

    subnet_config_data =  {
                   "fvSubnet":{
                      "attributes":{
                          "ip": ip,
                          "scope": scope
                        }
                    }
                  }


    payload_data = json.dumps(config_data)
    subnet_payload_data = json.dumps(subnet_config_data)

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
        if gateway_ip != 0:
           get_bd = requests.get(post_url, cookies=authenticate.cookies,
                                 data=payload_data, verify=False)
           data =json.loads(get_bd.text)
           count = data['totalCount']
           count = int(count)
           bridge_domain_list = []
           if get_bd.status_code == 200:
              for name in range(0,count):
                  bd = data['imdata'][name]['fvBD']['attributes']['name']
                  bridge_domain_list.append(bd)
                  if bd_name in bridge_domain_list:
                      subnet_req = requests.post(post_url, cookies=authenticate.cookies,
                                                 data=subnet_payload_data, verify=False)
                  else:
                       module.fail_json(msg='Subnet creation failed.')
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
        module.fail_json(msg=response,
                         response=response, status=status)

    results = {}
    results['status'] = status
    results['response'] = response
    results['changed'] = changed
    module.exit_json(**results)

from ansible.module_utils.basic import *
if __name__ == '__main__':
   main()