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
module: aci_context
short_description: Manage private networks, contexts, in an ACI fabric
description:
- Offers ability to manage private networks. Each context is a private network associated to a tenant, i.e. VRF
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
version_added: '2.4'
requirements:
- ACI Fabric 1.0(3f)+
notes:
- Tenant must be exist prior to using this module
options:
  tenant_name:
    description:
    - Tenant Name
    required: false
  vrf_name:
    description:
    - Context Name
    required: false
  policy_control_direction:
    description:
    - Policy Control Direction
    required: false
    choices: ['egress','ingress']
  policy_control_preference:
    description:
    - Policy Control Preference
    required: false
    choices: ['enforced', 'unenforced']
  descr:
    description:
    - Description for the AEP
    required: false
extends_documentation_fragment: aci
'''

EXAMPLES = '''
- name: ENSURE CONTEXT EXISTS
  aci_context:
    vrf_name: "vrf_lab"
    tenant_name: "lab_tenant"
    descr: "Lab VRF"
    host: "{{ inventory_hostname }}"
    username: "{{ user }}"
    password: "{{ pass }}"
'''

RETURN = '''
'''

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        description=dict(type='str', required=False),
        policy_control_direction=dict(choices=['ingress', 'egress'], type='str', required=False),
        policy_control_preference=dict(choices=['enforced', 'unenforced'], type='str', required=False),
        state=dict(choices=['absent', 'present', 'query'], type='str', default='present'),
        tenant_name=dict(type='str', required=False),
        vrf_name=dict(type='str', required=False)
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    description = module.params['description']
    policy_control_direction = module.params['policy_control_direction']
    policy_control_preference = module.params['policy_control_preference']
    state = module.params['state']
    tenant_name = module.params['tenant_name']
    vrf_name = module.params['vrf_name']

    aci = ACIModule(module)

    if vrf_name is not None:
        # fail when vrf_name is provided without tenant_name
        if tenant_name is not None:
            path = 'api/mo/uni/tn-%(tenant_name)s/ctx-%(vrf_name)s.json' % module.params
        else:
            module.fail_json(msg="Parameter 'tenant_name' is required with 'vrf_name'")
    elif state == 'query':
        path = 'api/class/fvCtx.json'
    else:
        module.fail_json(msg="Parameters 'tenant_name,' and 'vrf_name' are required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # Filter out module params with null values
        aci.payload(aci_class='fvCtx', class_config=dict(descr=description, pcEnfDir=policy_control_direction, pcEnfPref=policy_control_preference, name=vrf_name))

        # generate config diff which will be used as POST request body
        aci.get_diff(aci_class='fvCtx')

        # submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
