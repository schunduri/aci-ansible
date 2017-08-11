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
module: aci_anp
short_description: Manage top level application network profile objects
description:
    -  Manage top level application network profile object, i.e. this does
      not manage EPGs.
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieesrs)
version_added: '2.4'
requirements:
    - ACI Fabric 1.0(3f)+
notes: Tenant must exist prior to using this module
options:
   tenant_name:
     description:
     - The name of the tenant
     required: yes
   app_profile_name:
     description:
     - The name of the application network profile
     required: yes
   descr:
     description:
     - Description for the ANP
  state:
    description:
    - Use C(present) or C(absent) for adding or removing.
    - Use C(query) for listing an object or multiple objects.
    choices: [ absent, present, query ]
    default: present
extends_documentation_fragment: aci
'''

EXAMPLES = r'''
- name: Add a new ANP
  aci_anp:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant_name: production
    application_profile_name: default
    description: default ap
    state: present

- name: Remove an ANP
  aci_anp:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant_name: production
    app_profile_name: default
    state: absent

- name: Query an ANP
  aci_anp:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant_name: production
    app_profile_name: default
    state: query

- name: Query all ANPs
  aci_anp:
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
        app_profile=dict(type='str', aliases=['app_profile_name']),
        description=dict(type='str', aliases=['descr'], required=False),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        method=dict(type='str', choices=['delete', 'get', 'post'], aliases=['action'], removed_in_version='2.6'),  # Deprecated starting from v2.6
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    tenant = module.params['tenant']
    app_profile = module.params['app_profile']
    description = module.params['description']
    state = module.params['state']

    aci = ACIModule(module)

    if tenant is not None:
        # Work with a specific application profile name
        path = 'api/mo/uni/tn-%(tenant)s/ap-%(app_profile)s.json' % module.params
    elif state == 'query':
        # Query all application profile name
        path = 'api/class/fvAp.json'
    else:
        module.fail_json(msg="Parameter 'tenant' and 'app_profile' are required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # Filter out module parameters with null values
        aci.payload(aci_class='fvAp', class_config=dict(name=app_profile, descr=description))

        # Generate config diff which will be used as POST request body
        aci.get_diff(aci_class='fvAp')

        # Submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
