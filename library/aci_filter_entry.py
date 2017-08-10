#!usr/bin/python

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: aci_tenant
short_description: Manage tenants on Cisco ACI fabrics
description:
- Manage tenants on a Cisco ACI fabric.
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
version_added: '2.4'
requirements:
- ACI Fabric 1.0(3f)+
options:
  tenant_name:
    description:
    - The name of the tenant.
    required: yes
  descr:
    description:
    - Description for the AEP.
  state:
    description:
    - present, absent, query
    default: present
    choices: [ absent, present, query ]
extends_documentation_fragment: aci
'''

EXAMPLES = '''
- aci_filter_entry:
    action: "{{ action }}"
    entry_name: "{{ entry_name }}"
    tenant_name: "{{ tenant_name }}"
    ether_name: "{{  ether_name }}"
    icmp_msg_type: "{{ icmp_msg_type }}"
    filter_name: "{{ filter_name }}"
    descr: "{{ descr }}"
    host: "{{ inventory_hostname }}"
    username: "{{ user }}"
    password: "{{ pass }}"
    protocol: "{{ protocol }}"
'''

RETURN = '''
'''

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule

VALID_ARP_FLAGS = ['arp_reply', 'arp_request', 'unspecified']
VALID_ETHER_TYPES = ['arp', 'fcoe', 'ip', 'mac_security', 'mpls_ucast', 'trill', 'unspecified']
VALID_IP_PROTOCOLS = ['eigrp', 'egp', 'icmp', 'icmpv6', 'igmp', 'igp', 'l2tp', 'ospfigp', 'pim', 'tcp', 'udp', 'unspecified']

# mapping dicts are used to normalize the proposed data to what the APIC expects, which will keep diffs accurate
ARP_FLAG_MAPPING = dict(arp_reply='reply', arp_request='req', unspecified=None)
FILTER_PORT_MAPPING = {'443': 'https', '25': 'smtp', '80': 'http', '20': 'ftpData', '53': 'dns', '110': 'pop3', '554': 'rtsp'}


def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        arp_flag=dict(choices=VALID_ARP_FLAGS, required=False, type='str'),
        dest_port=dict(type="str", required=False),
        dest_port_end=dict(type="str", required=False),
        dest_port_start=dict(type="str", required=False),
        entry_name=dict(type="str", required=False),
        ether_type=dict(choices=VALID_ETHER_TYPES, type="str", required=False),
        filter_name=dict(type="str", required=False),
        ip_protocol=dict(choices=VALID_IP_PROTOCOLS, required=False, type='str'),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        tenant_name=dict(type="str", required=False)
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    arp_flag = module.params['arp_flag']
    if arp_flag is not None:
        arp_flag = ARP_FLAG_MAPPING[arp_flag]
    dest_port = module.params['dest_port']
    if dest_port in FILTER_PORT_MAPPING.keys():
        dest_port = FILTER_PORT_MAPPING[dest_port]
    dest_port_end = module.params['dest_port_end']
    if dest_port_end in FILTER_PORT_MAPPING.keys():
        dest_port_end = FILTER_PORT_MAPPING[dest_port_end]
    dest_port_start = module.params['dest_port_start']
    if dest_port_start in FILTER_PORT_MAPPING.keys():
        dest_port_start = FILTER_PORT_MAPPING[dest_port_start]
    entry_name = module.params['entry_name']
    ether_type = module.params['ether_type']
    filter_name = module.params['filter_name']
    ip_protocol = module.params['ip_protocol']
    state = module.params['state']
    tenant_name = module.params['tenant_name']

    aci = ACIModule(module)

    # validate that dest_port is not passed with dest_port_start or dest_port_end
    if dest_port is not None and (dest_port_end is not None or dest_port_start is not None):
        module.fail_json(msg="Parameter 'dest_port' cannot be used with 'dest_port_end' and 'dest_port_start'")
    elif dest_port is not None:
        dest_port_end = dest_port
        dest_port_start = dest_port

    if entry_name is not None:
        # fail when entry_name is provided without tenant_name and filter_name
        if tenant_name is not None and filter_name is not None:
            path = 'api/node/mo/uni/tn-%(tenant_name)s/flt-%(filter_name)s/e-%(entry_name)s.json' % module.params
        else:
            module.fail_json(msg="Parameters 'tenant_name' and 'filter_name' are required with 'entry_name'")
    elif state == 'query':
        path = 'api/node/class/vzEntry.json'
    else:
        module.fail_json(msg="Parameters 'tenant_name,' 'filter_name,' and 'entry_name' are required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # Filter out module params with null values
        aci.payload(aci_class='vzEntry', class_config=dict(arpOpc=arp_flag,
                                                           dFromPort=dest_port_start,
                                                           dToPort=dest_port_end,
                                                           etherT=ether_type,
                                                           name=entry_name,
                                                           prot=ip_protocol))

        # generate config diff which will be used as POST request body
        aci.get_diff(aci_class='vzEntry')

        # submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
