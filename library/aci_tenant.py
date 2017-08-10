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
  tenant:
    description:
    - The name of the tenant.
    required: yes
    aliases: [ name, tenant_name ]
  description:
    description:
    - Description for the AEP.
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
- name: Add a new tenant
  aci_tenant:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    description: Production tenant
    state: present

- name: Remove a tenant
  aci_tenant:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    state: absent

- name: Query a tenant
  aci_tenant:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    state: query

- name: Query all tenants
  aci_tenant:
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
        tenant=dict(type='str', aliases=['name', 'tenant_name'], required=False),
        description=dict(type='str', aliases=['descr'], required=False),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        method=dict(type='str', choices=['delete', 'get', 'post'], aliases=['action'], removed_in_version='2.6'),  # Deprecated starting from v2.6
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    tenant = module.params['tenant']
    description = module.params['description']
    state = module.params['state']

    aci = ACIModule(module)

    if tenant_name is not None:
        # Work with a specific tenant
        path = 'api/mo/uni/tn-%(tenant)s.json' % module.params
    elif state == 'query':
        # Query all tenants
        path = 'api/class/fvTenant.json'
    else:
        module.fail_json(msg="Parameter 'tenant' is required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # Filter out module params with null values
        aci.payload(aci_class='fvTenant', class_config=dict(name=tenant, descr=description))

        # Generate config diff which will be used as POST reqest body
        aci.get_diff(aci_class='fvTenant')

        # Submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
