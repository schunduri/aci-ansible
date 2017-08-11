#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
module: aci_aep
short_description: Direct access to the Cisco ACI APIC API
description:
- Offers direct access to the Cisco ACI APIC API to manage Attachable Entity Profile.
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
- Jacob McGill (@jmcgill298)
version_added: '2.4'
requirements:
- ACI Fabric 1.0(3f)+
options:
    aep_name:
      description:
      - The name of the Attachable Access Entity Profile.
      required: yes
    description:
      description:
      - Description for the AEP.
    state:
      description:
      - Use C(present) or C(absent) for adding or removing.
      - Use C(query) for listing an object or multiple objects.
      default: present
      choices: [ absent, present, query ]
extends_documentation_fragment: aci
'''

EXAMPLES = r'''
- name: Add a new AEP
  aci_aep:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    aep_name: ACI-AEP
    description: default
    state: present

- name: Remove an existing AEP
  aci_aep:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    aep_name: ACI-AEP
    state: absent

- name: Query an AEP
  aci_aep:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    aep_name: ACI-AEP
    state: query

- name: Query all AEPs
  aci_aep:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    state: query
'''

RETURN = r'''
#
'''

import json

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule

def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        aep_name=dict(type='str'),
        description=dict(type='str', aliases=['descr']),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        method=dict(type='str', choices=['delete', 'get', 'post'], aliases=['action'], removed_in_version='2.6'),  # Deprecated starting from v2.6
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    aep_name = module.params['aep_name']
    description = module.params['description']
    state = module.params['state']

    aci = ACIModule(module)

    # TODO: Investigate for a URI to query objects for a specific tenant
    if aep_name is not None:
        # Work with a specific AEP 
        path = 'api/mo/uni/infra/attentp-%(aep_name)s.json' % module.params
    elif state == 'query':
        # Query all AEP
        path = 'api/node/class/infraAttEntityP.json'
    else:
        module.fail_json(msg="Parameter 'aep_name' is required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # filter out module parameters with null values
        aci.payload(aci_class='infraAttEntityP', class_config=dict(name=aep_name, descr=description))

        # Generate config diff which will be used as POST request body
        aci.get_diff(aci_class='infraAttEntityP')

        # Submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
