# Ansible Modules used to Automate Cisco ACI
### *Idempotent Modules to manage ACI and much more!*

---
### Requirements
* ACI Fabric 1.0(3f)+
* Cobra SDK

---
### Modules

  * [aci_context - manage private networks, contexts, in an aci fabric](#aci_context)
  * [aci_filter - manages top level filter objects](#aci_filter)
  * [aci_filter_entry - manages filter entries that will be assigned to a filter](#aci_filter_entry)
  * [aci_bridge_domain - manages bridge domains in an aci fabric](#aci_bridge_domain)
  * [aci_contract - manages initial contracts (does not include contract subjs)](#aci_contract)
  * [aci_tenant - manage tenants in an aci fabric](#aci_tenant)
  * [aci_rest - direct access to the apic api](#aci_rest)
  * [aci_epg - manages aci end point groups and related contracts](#aci_epg)
  * [aci_contract_subject - manages contract subjects](#aci_contract_subject)
  * [aci_anp - manage top level application network profile objects](#aci_anp)

---

## aci_context
Manage private networks, contexts, in an aci fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
Offers ability to manage private networks. Each context is a private network associated to a tenant, i.e. VRF

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |  null  | <ul></ul> |  Password used to login to the switch  |
| host  |   no  |  https  | <ul>  </ul> | IP Address or hostname of APIC resolvable by Ansible control host |
| protocol  |   yes  |  | <ul><li>http</li>  <li>https</li></ul> |  Dictates connection protocol |
| action | yes   |  | <ul> <li>post</li> <li>get</li> </ul>| Http verbs, i.e. Get or Post|
| tenant_name  |   yes  |  unspecified  | <ul></ul> |  Name of the Tenant  |
| vrf_name  |   yes |  | <ul></ul> |  Name of the Context  |
| policy_control_direction  |   no  | ingress | <ul> <li>ingress</li>  <li>egress</li> </ul> |  The preferred policy control in relation to where the policy will be applied  |
| policy_control_preference  |   no  | enforced  | <ul><li>enforced</li> <li>unenforced</li></ul> |    |
| descr  |   no  | null | <ul></ul> | Description for the filter entry  |

 
#### Examples

```
-aci_context:
       action: "{{ action }}"
       vrf_name: "{{ vrf_name }}"
       tenant_name: "{{ tenant_name }}"
       policy_control_direction: "{{  policy_control_direction }}"
       policy_control_preference: "{{ policy_control_preference }}"
       descr: "{{ descr }}"
       host: "{{ inventory_hostname }}"
       username: "{{ user }}"
       password: "{{ pass }}"
       protocol: "{{ protocol }}"

```


#### Notes

- Tenant must be exist prior to using this module


---


## aci_filter
Manages top level filter objects

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Manages top level filter objects, i.e. not each entry

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| host | yes | |<ul></ul> | IP Address or hostname of APIC resolvable by Ansible control host |
| action | yes   |  | <ul> <li>post</li> <li>get</li> </ul>| Http verbs, i.e. Get or Post|
| filter_name  |   yes  |  | <ul></ul> | name of the filter the entry will be a part of |
| entry_name | yes | | <ul></ul> | name of the filter entry  |
| tenant_name  |   yes  |  | <ul></ul> |  name of the tenant this filter will be a part of |
| descr  |   no  |  null  | <ul> </ul> |   description of filter entry  |


 
#### Examples

```

 aci_filter:
       action: "{{ action }}"
       filter_name: "{{ filter_name }}"
       tenant_name: "{{ tenant_name }}"
       descr: "{{ descr }}"
       host: "{{ inventory_hostname }}"
       username: "{{ user }}"
       password: "{{ pass }}"
       protocol: "{{ protocol }}"


```
#### Notes

- Tenant must be exist prior to using this module

---

## aci_filter_entry
Manages filter entries that will be assigned to a filter

  * Synopsis
  * Options
  * Examples

#### Synopsis
Manages filter entries that will be assigned to an already created filter

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| host | yes | |<ul></ul> | IP Address or hostname of APIC resolvable by Ansible control host |
| action | yes   |  | <ul> <li>post</li> <li>get</li> </ul>| Http verbs, i.e. Get or Post|
| filter_name  |   yes  |  | <ul></ul> | name of the filter the entry will be a part of  |
| tenant_name  |   yes  |  | <ul></ul> |  name of the tenant this filter will be a part  |
| entry_name | yes | | <ul></ul> | name of the entry |
| ether_type | no | unspecified | <ul><li>ARP</li><li>FCOE</li><li>IP</li><li>MAC Security</li><li>MPLS Unicast</li><li>Trill</li><li>Unspecified</li> </ul> | EtherType of the filter entry |
| icmp_msg_type | no | unspecified | <ul> <li>echo</li> <li>echo-rep</li> <li>dst-unreach</li> <li>unspecified</li> </ul> | ICMP Message Type |
| descr  |   no  |  null  | <ul> </ul> |   description of filter  |

 
#### Examples

```
  aci_filter_entry:
       action: "{{ action }}"
       filter_name; "{{ filter_name }}"
       entry_name: "{{ entry_name }}"
       tenant_name: "{{ tenant_name }}"
       ether_name: "{{  ether_name }}"
       icmp_msg_type: "{{ icmp_msg_type }}"
       descr: "{{ descr }}"
       host: "{{ inventory_hostname }}"
       username: "{{ user }}"
       password: "{{ pass }}"
       protocol: "{{ protocol }}"

```
#### Notes

- Tenant and Filter must exist prior to using this module

---

## aci_bridge_domain
Manages bridge domains in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Manages bridge domains within an ACI fabric

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| subnet  |   no  |  | <ul></ul> |  name of subnet that is paired to bridge domain  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| name  |   yes  |  | <ul></ul> |  Name of the bridge domain  |
| descr  |   no  |  | <ul></ul> |  description of bridge domain  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| state  |   no  |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Desired state of the bridge domain  |
| context  |   yes  |  | <ul></ul> |  name of context (private network / VRF)  |
| password  |   yes  |  C1sco12345  | <ul></ul> |  Password used to login to the switch  |
| tenant  |   yes  |  | <ul></ul> |  name of tenant this bridge domain will be part of  |


 
#### Examples

```

# ensure bridge domain 1 exists
- aci_bridge_domain: name=ACILab_BD1 context=ACILab_VRF subnet=10.10.10.1/24 tenant=ACILab state=present host={{ inventory_hostname }} username={{ user }} password={{ pass }}

# ensure bd 1 doesn't exist
- aci_bridge_domain: name=ACILab_BD1 context=ACILab_VRF tenant=ACILab state=absent host={{ inventory_hostname }} username={{ user }} password={{ pass }}


```


#### Notes

- Tenant and context must be exist prior to using this module

- One subnet can be added per task (per module call)

- state=absent removes complete bridge domain configuration including all subnets


---


## aci_contract
Manages initial contracts (does not include contract subjs)

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Manages contract resource, but does not include subjects although subjects can be removed using this module

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| name  |   yes  |  | <ul></ul> |  Name of the contract  |
| prio  |   no  |  | <ul> <li>unspecified</li>  <li>level1</li>  <li>level2</li>  <li>level3</li> </ul> |  priority (qosclass) of contract  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| state  |   no  |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Desired state of the contract  |
| descr  |   no  |  | <ul></ul> |  description of contract  |
| scope  |   no  |  | <ul> <li>application-profile</li>  <li>context</li>  <li>global</li>  <li>tenant</li> </ul> |  scope of contract  |
| password  |   yes  |  C1sco12345  | <ul></ul> |  Password used to login to the switch  |
| tenant  |   yes  |  | <ul></ul> |  name of tenant this contract will be part of  |


 
#### Examples

```
# ensure contract exists
- aci_contract: name=web-contract descr='web contracy by ansible' tenant=customer_1 host={{ inventory_hostname }} username={{ user }} password={{ pass }}

# ensure contract exists with added params
- aci_contract: name=web-contract descr='web contracy by ansible' tenant=customer_1 prio=level2 scope=context host={{ inventory_hostname }} username={{ user }} password={{ pass }}

# ensure contract does not exist
- aci_contract: name=web-contract tenant=customer_1 state=absent host={{ inventory_hostname }} username={{ user }} password={{ pass }}


```


#### Notes

- Tenant and context must be exist prior to using this module

- state=absent removes complete contract including the contract subjects that were deployed with the aci_contract_subject module


---


## aci_tenant
Manage tenants in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage tenants

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| name  |   yes  |  | <ul></ul> |  Name of tenant  |
| descr  |   no  |  | <ul></ul> |  description of tenant  |
| state  |   no  |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Desired state of the tenant  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| password  |   yes  |  C1sco12345  | <ul></ul> |  Password used to login to the switch  |


 
#### Examples

```
# ensure tenant exists
- aci_tenant: name=ACILab descr='tenant by Ansible' host={{ inventory_hostname }} username={{ user }} password={{ pass }}

# ensure tenant does not exist on system
- aci_tenant: name=ACILab state=absent host={{ inventory_hostname }} username={{ user }} password={{ pass }}


```



---


## aci_rest
Direct access to the APIC API

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers direct access to the APIC API

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| config_file  |   no  |  | <ul></ul> |  name of the absolute path of the filname that includes the body of the http request being sent to the ACI fabric  |
| uri  |   yes  |  | <ul></ul> |  uri being used to execute API calls. Must end in .xml or .json  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action  |   yes  |  | <ul> <li>post</li>  <li>get</li> </ul> |  http verb, i.e. post or get  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| password  |   yes  |  C1sco12345  | <ul></ul> |  Password used to login to the switch  |


 
#### Examples

```

# add a tenant
- aci_rest: action=post uri=/api/mo/uni.xml config_file=/home/cisco/ansible/aci/configs/aci_config.xml host={{ inventory_hostname }} username={{ user }} password={{ pass }}

# get tenants
- aci_rest: action=get uri=/api/node/class/fvTenant.json host={{ inventory_hostname }} username={{ user }} password={{ pass }}

# configure contracts
- aci_rest: action=post uri=/api/mo/uni.xml config_file=/home/cisco/ansible/aci/configs/contract_config.xml host={{ inventory_hostname }} username={{ user }} password={{ pass }}


```


#### Notes

- Tenant must be exist prior to using this module


---


## aci_epg
Manages ACI end point groups and related contracts

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Manages ACI end point groups and related contracts

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |  C1sco12345  | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| name  |   yes  |  | <ul></ul> |  Name of the application network profile  |
| prio  |   no  |  | <ul> <li>unspecified</li>  <li>level1</li>  <li>level2</li>  <li>level3</li> </ul> |  priority (qos class) for epg  |
| vmm_domain  |   no  |  | <ul></ul> |  desired vmm domain or list of vmm domains (VMware only)  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| state  |   no  |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Desired state of the epg  |
| anp  |   yes  |  | <ul></ul> |  name of the application profile this will be part of  |
| descr  |   no  |  | <ul></ul> |  description of the application network profile  |
| consumed_contracts  |   no  |  | <ul></ul> |  desired contract or list of consumed contracts  |
| bridge_domain  |   no  |  | <ul></ul> |  desired bridge domain or list of bridge domains  |
| tenant  |   yes  |  | <ul></ul> |  name of tenant this application network profile will be part of  |
| provided_contracts  |   no  |  | <ul></ul> |  desired contract or list of provided contracts  |


 
#### Examples

```

# ensure web epg exists
- aci_epg:
    name: Web_EPG
    consumed_contracts: Web_Con
    provided_contracts: App_Con
    bridge_domain: ACILab_BD1
    vmm_domain: My-vCenter
    anp: 3Tier_App
    tenant: ACILab
    state: present
    host: "{{ inventory_hostname }}"

# ensure app epg exists
- aci_epg:
    name: App_EPG
    consumed_contracts: App_Con
    provided_contracts: DB_Con
    bridge_domain: ACILab_BD1
    vmm_domain: My-vCenter
    anp: 3Tier_App
    tenant: ACILab
    state: present
    host: "{{ inventory_hostname }}"


```


#### Notes

- provided_contracts, consumed_contracts, vmm_domain, and bridge_domain could be supplied as a string or a list of names for that particular resource.  They also ensure each are in the desired state. This means if resources are already assigned and not in the new list (or str), they will be removed.


---


## aci_contract_subject
Manages contract subjects

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Manages contract subjects that are a necessity for contracts

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| in_filters  |   no  |  | <ul></ul> |  Filter or list of filters being applied inbound when the contract is applied as a policy between EPGs  |
| out_filters  |   no  |  | <ul></ul> |  Filter or list of filters being applied inbound when the contract is applied as a policy between EPGs  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| name  |   yes  |  | <ul></ul> |  Name of contract subject  |
| prio  |   no  |  | <ul> <li>unspecified</li>  <li>level1</li>  <li>level2</li>  <li>level3</li> </ul> |  priority (qos class) for subject (not per direction filters)  |
| apply_both_directions  |   no  |  True  | <ul> <li>true</li>  <li>false</li>  <li>yes</li>  <li>no</li> </ul> |  determines if the contract applies to both inbound and outbound traffic  |
| state  |   no  |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Desired state of the contract subject  |
| contract  |   yes  |  | <ul></ul> |  Name of contract this subject will be applied to  |
| svc_graph  |   no  |  | <ul></ul> |  distinguished name of the service graph. The service graph is an image that shows the relationship between contracts and subjects. Not yet supported in this module.  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC (resolvable by Ansible control host)  |
| reverse_filter_ports  |   no  |  | <ul> <li>true</li>  <li>false</li>  <li>yes</li>  <li>no</li> </ul> |  Apply the same subject rule to the reverse filter ports when the contract applies in both directions.  apply_both_directions must be true to use this flag  |
| filters  |   no  |  | <ul></ul> |  Filter or list of filters being applied to the contract subject. To be used when a single filter is being applied in both directions.  |
| descr  |   no  |  | <ul></ul> |  description of contract subject  |
| password  |   yes  |  C1sco12345  | <ul></ul> |  Password used to login to the switch  |
| tenant  |   yes  |  | <ul></ul> |  Name of tenant the contract and subject will be applied to  |


 
#### Examples

```

# ensure contract subject for web exists
- aci_contract_subject: name=web_subject contract=Web_Con filters=Web_Filter tenant=ACILab host={{ inventory_hostname }}

# created a subject using a different filter for each direction
- aci_contract_subject: name=web_subject contract=Web_Con in_filters=arp out_filters=Web_Filter apply_both_directions=false descr='web subj2' tenant=ACILab host={{ inventory_hostname }}


```


#### Notes

- Tenant & Contract must be exist prior to using this module

- filters, in_filters, and out_filters can be a single filter or a list of filters.  In either case, it is the desired filters that should be applied to the contract subject.  This means if filters are already assigned and not in the new list, they will be removed.

- QOS class per filter "group" when not applying the same group of filters in not yet supported

- Service is currently not supported.


---


## aci_context
Manage private networks, contexts, in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage private networks. Each context is a private network associated to a tenant, i.e. VRF

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| name  |   yes  |  | <ul></ul> |  Name of context (private network / VRF)  |
| descr  |   no  |  | <ul></ul> |  description of context (private network)  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| state  |   no  |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Desired state of the context  |
| password  |   yes  |  C1sco12345  | <ul></ul> |  Password used to login to the switch  |
| tenant  |   yes  |  | <ul></ul> |  name of tenant the private network will be associated to  |


 
#### Examples

```
# ensure context for tenant exists (private network)
- aci_context: name=ACILab_VRF descr='ACILab VRF' tenant=ACILab host={{ inventory_hostname }} username={{ user }} password={{ pass }}

# ensure context for tenant exists (private network)
- aci_context: name=ACILab_VRF tenant=ACILab state=absent host={{ inventory_hostname }} username={{ user }} password={{ pass }}



```


#### Notes

- Tenant must be exist prior to using this module


---


## aci_anp
Manage top level application network profile objects

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Manage top level application network profile object, i.e. this does not manage EPGs.

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| name  |   yes  |  | <ul></ul> |  Name of the application network profile  |
| descr  |   no  |  | <ul></ul> |  description of the application network profile  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| state  |   yes  |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Desired state of the application network profile  |
| password  |   yes  |  C1sco12345  | <ul></ul> |  Password used to login to the switch  |
| tenant  |   yes  |  | <ul></ul> |  name of tenant this application network profile will be part of  |


 
#### Examples

```

# ensure application network profile exists
- aci_anp: name=3Tier_App tenant=ACILab state=present host={{ inventory_hostname }} username={{ user }} password={{ pass }}


```



---


---
Created by Network to Code, LLC
For:
2015
