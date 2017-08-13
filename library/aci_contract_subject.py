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
module: aci_contract_subject
short_description: Manages initial contract subjects(does not include contracts)
description:
-  Manage a group of filters for a specific application or service using contract subjects in Cisco ACI APIC APIs with this module.
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
- Jacob McGill (@jmcgill298)
requirements:
- ACI Fabric 1.0(3f)+
notes:
- The tenant used must exist before using this module in your playbook. The M(aci_tenant) module can be used for this.
options:
   tenant:
     description
     - The name of the tenant.
     required: yes
     aliases: ['tenant_name']
   subject:
     description:
     - The contract subject name.
     required: yes
     aliases: ['name', subject_name']
   contract:
     description:
     - the name of the Contract.
     required: yes
     aliases: ['contract_name']
   reverse_filter:
     description:
     - Select or De-select reverse filter port option.
     default: no
     choices: [ yes, no ]
   priority:
     description:
     - Qos class.
     default: unspecified
     choices: [ unspecified, level1, level2, level3 ]
   target:
     description:
     - Target DSCP.
     default: unspecified
   filter_name:
     description:
     - Filter Name
   directive:
     description:
     - Directive for filter  (can be none or log).
   description:
     description:
     - Description for the contract subject.
   state:
     description:
     - Use C(present) or C(absent) for adding or removing.
     - Use C(query) for listing an object or multiple objects.
     choices: [ absent, present, query ]
     default: present
extends_documentation_fragment: aci
'''

EXAMPLES = r'''

- name: Add a new contract subject
  aci_contract_subject:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    contract: web_to_db
    subject: default
    description: test
    reverse_filter: yes
    priority: level1
    target: unspecified
    filter_name: default
    directive: log
    state: present

- name: Remove a contract subject
  aci_contract_subject:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    contract: web_to_db
    subject: default
    state: absent

- name: Query a contract subject
  aci_contract_subject:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    contract: web_to_db
    subject: default
    state: query

- name: Query all contract subjects
  aci_contract_subject:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    state: query

'''

RETURN = r'''
#
'''

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        contract=dict(type="str", aliases=['contract_name']),
        subject=dict(type="str", aliases=['name', 'subject_name']),
        tenant=dict(type="str", aliases=['tenant_name']),
        priority=dict(choices=['unspecified', 'level1', 'level2', 'level3'], default='unspecified', required=False),
        reverse_filter=dict(choices=['yes', 'no'], required=False, default='yes'),
        target=dict(type="str", required=False, default='unspecified'),
        description=dict(type="str", required=False, aliases=['descr']),
        filter_name=dict(type="str", required=False),
        directive=dict(choices=['none', 'log'], required=False, default='none'),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        method=dict(type='str', choices=['delete', 'get', 'post'], aliases=['action'], removed_in_version='2.6'),  # Deprecated starting from v2.6
    )

    module = AnsibleModule(
       argument_spec=argument_spec,
       supports_check_mode=True,
    )

    subject = module.params['subject']
    tenant = module.params['tenant']
    priority = module.params['priority']
    reverse_filter = module.params['reverse_filter']
    target = module.params['target']
    description = module.params['description']
    contract = module.params['contract']
    filter_name = module.params['filter_name']
    directive = module.params['directive']
    state = module.params['state']

    if directive == "none":
        directive = ""

    aci = ACIModule(module)

    if (tenant, contract, subject) is not None:
        # Work with a specific filter
        path = 'api/mo/uni/tn-%(tenant)s/brc-%(contract)s/subj-%(subject)s.json' % module.params
    elif state == 'query':
        # Query all filters
        path = 'api/node/class/vzSubj.json'
    else:
        module.fail_json(msg="Parameters 'contract', 'subject' and 'tenant' are required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # Filter out module parameters with null values
        aci.payload(aci_class='vzSubj', class_config=dict(name=subject, prio=priority, revFltPorts=reverse_filter, targetDscp=target, descr=description),
                    child_configs=[dict(vzRsSubjFiltAtt=dict(attributes=dict(directives=directive, tnVzFilterName=filter_name)))])

        # Generate config diff which will be used as POST request body
        aci.get_diff(aci_class='vzSubj')

        # Submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)

if __name__ == "__main__":
    main()
