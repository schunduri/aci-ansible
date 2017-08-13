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
module: aci_filter_entry
short_description: Manage filter entries on Cisco ACI fabrics
description:
- Manage filter entries for a filter on Cisco ACI fabrics.
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
- Jacob McGill (@jmcgill298)
version_added: '2.4'
requirements:
- Tested with ACI Fabric 1.0(3f)+
notes:
- The tenant used must exist before using this module in your playbook. The M(aci_tenant) module can be used for this.
- The filter used must exist before using this module in your playbook. The M(aci_filter) module can be used for this.
options:
  arp_flag:
    description:
    - The arp flag to use when the ether_type is arp.
    choices: [ arp_reply, arp_request, unspecified ]
    type: str
  description:
    description:
    - Description for the Filter Entry.
    alias: [ descr ]
    type: str
  dst_port:
    description:
    - Used to set both destination start and end ports to the same value when ip_protocol is tcp or udp.
    choices: [ Valid TCP/UDP Port Ranges]
    type: str
  dst_port_end:
    description:
    - Used to set the destination end port when ip_protocol is tcp or udp.
    choices: [ Valid TCP/UDP Port Ranges]
    type: str
  dst_port_start:
    description:
    - Used to set the destination start port when ip_protocol is tcp or udp.
    choices: [ Valid TCP/UDP Port Ranges]
    type: str
  entry:
    description:
    - Then name of the Filter Entry.
    aliases: [ entry_name, name ]
    type: str
  ether_type:
    description:
    - The Ethernet type.
    type: str
    choices: [ arp, fcoe, ip, mac_security, mpls_ucast, trill, unspecified ]
  filter_name:
    description:
      The name of Filter that the entry should belong to.
    type: str
  icmp_msg_type:
    description:
    - ICMPv4 message type; used when ip_protocol is icmp.
    choices: [ dst_unreachable, echo, echo_reply, src_quench, time_exceeded, unspecified ]
    type: str
  icmp6_msg_type:
    description:
    - ICMPv6 message type; used when ip_protocol is icmpv6.
    choices: [ dst_unreachable, echo_request, echo_reply, neighbor_advertisement, neighbor_solicitation, redirect, time_exceeded, unspecified ]
    type: str
  ip_protocol:
    description:
    - The IP Protocol type when ether_type is ip.
    choices: [ eigrp, egp, icmp, icmpv6, igmp, igp, l2tp, ospfigp, pim, tcp, udp, unspecified ]
    type: str
  state:
    description:
    - present, absent, query
    default: present
    choices: [ absent, present, query ]
    type: str
  stateful:
    description:
    - Determines the statefulness of the filter entry.
    type: str
  tenant:
    description:
    - The name of the tenant.
    alias: [ tenant_name ]
    type: str
extends_documentation_fragment: aci
'''

EXAMPLES = r'''
- aci_filter_entry:
    action: "{{ action }}"
    entry: "{{ entry }}"
    tenant: "{{ tenant }}"
    ether_name: "{{  ether_name }}"
    icmp_msg_type: "{{ icmp_msg_type }}"
    filter_name: "{{ filter_name }}"
    descr: "{{ descr }}"
    host: "{{ inventory_hostname }}"
    username: "{{ user }}"
    password: "{{ pass }}"
    protocol: "{{ protocol }}"
'''

RETURN = ''' # '''

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule

VALID_ARP_FLAGS = ['arp_reply', 'arp_request', 'unspecified']
VALID_ETHER_TYPES = ['arp', 'fcoe', 'ip', 'mac_security', 'mpls_ucast', 'trill', 'unspecified']
VALID_ICMP_TYPES = ['dst_unreachable', 'echo', 'echo_reply', 'src_quench', 'time_exceeded',
                    'unspecified', 'echo-rep', 'dst-unreach']
VALID_ICMP6_TYPES = ['dst_unreachable', 'echo_request', 'echo_reply', 'neighbor_advertisement',
                     'neighbor_solicitation', 'redirect', 'time_exceeded', 'unspecified']
VALID_IP_PROTOCOLS = ['eigrp', 'egp', 'icmp', 'icmpv6', 'igmp', 'igp', 'l2tp', 'ospfigp', 'pim', 'tcp', 'udp', 'unspecified']

# mapping dicts are used to normalize the proposed data to what the APIC expects, which will keep diffs accurate
ARP_FLAG_MAPPING = dict(arp_reply='reply', arp_request='req', unspecified=None)
FILTER_PORT_MAPPING = {'443': 'https', '25': 'smtp', '80': 'http', '20': 'ftpData', '53': 'dns', '110': 'pop3', '554': 'rtsp'}
ICMP_MAPPING = {'dst_unreachable': 'dst-unreach', 'echo': 'echo', 'echo_reply': 'echo-rep', 'src_quench': 'src-quench',
                'time_exceeded': 'time-exceeded', 'unspecified': 'unspecified', 'echo-re': 'echo-rep', 'dst-unreach': 'dst-unreach'}
ICMP6_MAPPING = dict(dst_unreachable='dst-unreach', echo_request='echo-req', echo_reply='echo-rep', neighbor_advertisement='nbr-advert',
                     neighbor_solicitation='nbr-solicit', redirect='redirect', time_exceeded='time-exceeded', unspecified='unspecified')


def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        arp_flag=dict(type='str', choices=VALID_ARP_FLAGS),
        description=dict(type='str'),
        dst_port=dict(type='str'),
        dst_port_end=dict(type='str'),
        dst_port_start=dict(type='str'),
        entry=dict(type='str', aliases=['entry_name', 'name']),
        ether_type=dict(choices=VALID_ETHER_TYPES, type='str'),
        filter_name=dict(type='str'),
        icmp_msg_type=dict(type='str', choices=VALID_ICMP_TYPES),
        icmp6_msg_type=dict(type='str', choices=VALID_ICMP6_TYPES),
        ip_protocol=dict(choices=VALID_IP_PROTOCOLS, type='str'),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        stateful=dict(type='str', choices=['no', 'yes']),
        tenant=dict(type="str", aliases=['tenant_name'])
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    arp_flag = module.params['arp_flag']
    if arp_flag is not None:
        arp_flag = ARP_FLAG_MAPPING[arp_flag]
    description = module.params['description']
    dst_port = module.params['dst_port']
    if dst_port in FILTER_PORT_MAPPING.keys():
        dst_port = FILTER_PORT_MAPPING[dst_port]
    dst_end = module.params['dst_port_end']
    if dst_end in FILTER_PORT_MAPPING.keys():
        dst_end = FILTER_PORT_MAPPING[dst_end]
    dst_start = module.params['dst_port_start']
    if dst_start in FILTER_PORT_MAPPING.keys():
        dst_start = FILTER_PORT_MAPPING[dst_start]
    entry = module.params['entry']
    ether_type = module.params['ether_type']
    filter_name = module.params['filter_name']
    icmp_msg_type = module.params['icmp_msg_type']
    if icmp_msg_type is not None:
        icmp_msg_type = ICMP_MAPPING[icmp_msg_type]
    icmp6_msg_type = module.params['icmp6_msg_type']
    if icmp6_msg_type is not None:
        icmp6_msg_type = ICMP6_MAPPING[icmp6_msg_type]
    ip_protocol = module.params['ip_protocol']
    state = module.params['state']
    stateful = module.params['stateful']
    tenant = module.params['tenant']

    aci = ACIModule(module)

    # validate that dst_port is not passed with dst_start or dst_end
    if dst_port is not None and (dst_end is not None or dst_start is not None):
        module.fail_json(msg="Parameter 'dst_port' cannot be used with 'dst_end' and 'dst_start'")
    elif dst_port is not None:
        dst_end = dst_port
        dst_start = dst_port

    # validate that filter_name is not passed without tenant
    if filter_name is not None and tenant is None:
        module.fail_json(msg="Parameter 'filter_name' cannot be used without 'tenant'")

    # TODO: Think through the logic here and see if there is a better way
    if entry is not None:
        # fail when entry is provided without tenant and filter_name
        if tenant is not None and filter_name is not None:
            path = 'api/mo/uni/tn-%(tenant)s/flt-%(filter_name)s/e-%(entry)s.json' % module.params
        elif tenant is not None and state == 'query':
            path = 'api/mo/uni/tn-%(tenant)s.json?rsp-subtree=full&rsp-subtree-class=vzEntry&rsp-subtree-filter=eq(vzEntry.name, \
                   \"%(entry)s\")&rsp-subtree-include=no-scoped' % module.params
        else:
            path = 'api/class/vzEntry.json?query-target-filter=eq(vzEntry.name, \"%(entry)s\")' % module.params
    elif state == 'query':
        if tenant is None:
            path = 'api/class/vzEntry.json'
        else:
            path = 'api/mo/uni/tn-%(tenant)s.json?rsp-subtree=full&rsp-subtree-class=vzEntry&rsp-subtree-include=no-scoped' % module.params
    else:
        module.fail_json(msg="Parameters 'tenant', 'filter_name', and 'entry' are required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # Filter out module params with null values
        aci.payload(aci_class='vzEntry', class_config=dict(arpOpc=arp_flag,
                                                           descr=description,
                                                           dFromPort=dst_start,
                                                           dToPort=dst_end,
                                                           etherT=ether_type,
                                                           icmpv4T=icmp_msg_type,
                                                           icmpv6T=icmp6_msg_type,
                                                           name=entry,
                                                           prot=ip_protocol,
                                                           stateful=stateful))

        # generate config diff which will be used as POST request body
        aci.get_diff(aci_class='vzEntry')

        # submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
