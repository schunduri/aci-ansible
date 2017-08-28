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
module: aci_aaa_login_domain
short_description: Manage login domains on Cisco ACI fabrics (aaa:LoginDomain)
description:
- Manage login domains on Cisco ACI fabrics.
- More information from the internal APIC class
  I(aaa:LoginDomain) at U(https://developer.cisco.com/media/mim-ref/MO-aaaLoginDomain.html).
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
- Jacob McGill (@jmcgill298)
version_added: '2.4'
requirements:
    - ACI Fabric 1.0(3f)+
options:
    login_domain:
       description:
       - Domain name
       required: true
    description:
       description:
       - Description for Login Domain
       aliases: [ descr ]
    state:
       description:
       - Use C(present) or C(absent) for adding or removing.
       - Use C(query) for listing an object or multiple objects.
       choices: [ absent, present, query ]
       default: present
extends_documentation_fragment: aci
'''

EXAMPLES = r'''
- name: Add a new login domain
  aci_aaa_login_domain:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    login_domain: fallback
    description: fallback login domain
    state: present

- name: Remove a login domain
  aci_aaa_login_domain:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    login_domain: fallback
    state: absent

- name: Query a login domain
  aci_aaa_login_domain:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    login_domain: fallback
    state: query

- name: Query all login domain
  aci_aaa_login_domain:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    state: query
'''

RETURN = r'''
status:
  description: status code of the http request
  returned: always
  type: int
  sample: 200
response:
  description: response text returned by APIC
  returned: when a HTTP request has been made to APIC
  type: string
  sample: '{"totalCount":"0","imdata":[]}'
'''

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        login_domain=dict(type='str', required=False),
        description=dict(type='str', required=False, aliases=['descr']),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        method=dict(type='str', choices=['delete', 'get', 'post'], aliases=['action'], removed_in_version='2.6'),  # Deprecated starting from v2.6
    )
   
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[['state', 'absent', ['login_domain']],
                     ['state', 'present', ['login_domain']]]
    )

    login_domain = module.params['login_domain']
    description = module.params['description']
    state=module.params['state']

    aci = ACIModule(module)
    aci.construct_url(root_class="login_domain")
    aci.get_existing()

    if state == 'present':
        # Filter out module parameters with null values
        aci.payload(
            aci_class='aaaLoginDomain',
            class_config=dict(name=login_domain, descr=description),
            child_class=[{'aaaDomainAuth':{ 'attributes':{ 'realm':'local' }}}]       
        )

        # Generate config diff which will be used as POST request body
        aci.get_diff(aci_class='login_domain')

        # Submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)

if __name__ == "__main__":
    main()
