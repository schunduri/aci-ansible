# Ansible Modules used to Automate Cisco ACI
### *Idempotent Modules to manage ACI and much more!*

---
### Requirements
* ACI Fabric 1.0(3f)+
* Python Requests Library

---
### Modules

  * [aci_context - manage private networks, contexts, in an aci fabric](#aci_context)
  * [aci_filter - manages top level filter objects](#aci_filter)
  * [aci_filter_entry - manages filter entries that will be assigned to a filter](#aci_filter_entry)
  * [aci_bridge_domain - manages bridge domains in an aci fabric](#aci_bridge_domain)
  * [aci_contract - manages initial contracts (does not include contract subjs)](#aci_contract)
  * [aci_contract_subject - manages contract subjects](#aci_contract_subject)
  * [aci_tenant - manage tenants in an aci fabric](#aci_tenant)
  * [aci_anp - manage top level application network profile objects](#aci_anp)
  * [aci_epg - manages aci end point groups and related contracts](#aci_epg)
  * [aci_epr - manages end point retention policies](#aci_epr)
  * [aci_fiber_channel_policy - manages fiber channel policies](#aci_fiber_channel_policy)
  * [aci_l2_interface_policy - manages l2 interface policies](#aci_l2_interface_policy)
  * [aci_lldp_interface_policy - manages lldp interface policies](#aci_lldp_interface_policy)
  * [aci_login_domain - manages login domains](#aci_login_domain)
  * [aci_monitoring_policy - manages monitoring policies](#aci_monitoring_policy)
  * [aci_mcp_interface - manages mcp interface policies](#aci_mcp_interface)
  * [aci_port_channel_interface - manages port channel interface policies](#aci_port_channel_interface)
  * [aci_port_security - manages port security](#aci_port_security)
  * [aci_route_tag_policy - manages route tag policy](#aci_route_tag_policy)
  * [aci_span_dst_group - manages span destination groups](#aci_span_dst_group)
  * [aci_span_src_group - manages span source groups](#aci_span_src_group)
  * [aci_taboo_contracts - manages taboo contracts](#aci_taboo_contracts)
  * [aci_action_rule_profile - manages action rule profiles](#aci_action_rule_profile)
  * [aci_aep - manages attachable entity profile](#aci_aep)
  * [aci_epg_domain_binding - manages epg physical domain binding](#aci_epg_domain_binding)
  * [aci_dynamic_vmm_binding - manages epg vmm dynamic domain binding](#aci_dynamic_vmm_binding)
  * [aci_rest - direct access to the apic api](#aci_rest)
 
 
 
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
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| host  |   no  |    | <ul>  </ul> | IP Address or hostname of APIC resolvable by Ansible control host |
| protocol  |   yes  | https | <ul><li>http</li>  <li>https</li></ul> |  Dictates connection protocol |
| action | yes   |  | <ul> <li>post</li> <li>get</li> </ul>| Http verbs, i.e. Get or Post|
| tenant_name  |   yes  |  unspecified  | <ul></ul> |  Name of the Tenant  |
| vrf_name  |   yes |  | <ul></ul> |  Name of the Context  |
| policy_control_direction  |   no  | ingress | <ul> <li>ingress</li>  <li>egress</li> </ul> |  The preferred policy control in relation to where the policy will be applied  |
| policy_control_preference  |   no  | enforced  | <ul><li>enforced</li> <li>unenforced</li></ul> |  The preferred policy control  |
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
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs, i.e. Get or Post |
| bd_name  |   yes  |  | <ul></ul> |  Name of the bridge domain  |
| tenant_name | yes | | <ul></ul> | Name of the Tenant the bridge domain will be a part of |
| vrf_name | yes | | <ul></ul> | Name of the context the bridge domain will be associated to |
| descr  |   no  |  | <ul></ul> |  description of bridge domain  |
| arp_flooding | no | yes | <ul><li>yes</li> <li>no</li></ul> | Enable or Disable ARP flooding |
| l2_unknown_unicast | no | proxy | <ul><li>flood</li> <li>proxy</li></ul> | L2 Unknown Unicast |
| l3_unknown_multicast | no | flood | <ul><li>opt-flood</li><li>flood</li></ul> | L3 Unknown Multicast |
| multi_dest | no | bd-flood | <ul> <li>bd-flood</li><li>drop</li><li>encap-flood</li> </ul> | Multi Destination Flooding |
| l3_out | yes | | <ul></ul> | L3 out association with the Bridge Domain |
| gateway_ip | yes | | <ul></ul> | IP address of the gateway |
| subnet_mask |  yes  |  | <ul></ul> |  subnet mask value  |
| scope | no | private | <ul></ul> | Scope of  the subnet | 
| dhcp_name | yes | | <ul></ul> | Name  of the DHCP Relay Label |
| dhcp_scope | no | infra | <ul><li> tenant <li> <li> infra </li> </ul> | Scope of the DHCP Relay label |


 
#### Examples

```

aci_bridge_domain:
     action: "{{ action }}"
     tenant_name: "{{ tenant_name }}" 
     bd_name: "{{ bd_name }}" 
     vrf_name: "{{ vrf_name }}"
     arp_flooding: "{{ arp_flooding }}"
     l2_unknown_unicast: "{{ l2_unknown_unicast }}"
     l3_unknown_multicast: "{{ l3_unknown_multicast }}"
     multi_dest: "{{ multi_dest }}" 
     l3_out: "{{ l3_out }}"
     gateway_ip: "{{ gateway_ip }}"
     subnet_mask: "{{ subnet_mask }}"
     scope: "{{ scope }}"
     dhcp_name: "{{ dhcp_name }}"
     dhcp_scope: "{{ dhcp_scope }}"
     host: "{{ inventory_hostname }}"
     username: "{{ username }}"
     password: "{{ password }}"
     protocol: "{{ protocol }}"

```


#### Notes

- Tenant and context must exist prior to using this module

- One subnet can be added per task (per module call)

---


## aci_contract
Manages initial contracts (does not include contract subjs)

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Manages contract resource

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li> </ul> | Http verbs, i.e. Get or Post |
| contract_name  |   yes  |  | <ul></ul> |  Name of the contract  |
| tenant_name  |   yes  |  | <ul></ul> |  name of tenant this contract will be part of  |
| priority |   no  | unspecified | <ul> <li>unspecified</li>  <li>level1</li>  <li>level2</li>  <li>level3</li> </ul> |  priority (qosclass) of contract  |
| target | no | unspecified | <ul></ul> |  Contract Target | 
| scope  |   no  | context  | <ul> <li>application-profile</li>  <li>context</li>  <li>global</li>  <li>tenant</li> </ul> |  scope of contract  |
| descr  |   no  |  | <ul></ul> |  description of contract  |

 
#### Examples

```
 aci_contract:
       action: "{{ action }}"
       contract_name: "{{ contract_name }}"
       tenant_name: "{{ tenant_name }}"
       priority: "{{ priority }}"
       scope: "{{ scope }}"
       target: "{{ target }}"
       descr: "{{ descr }}"
       host: "{{ inventory_hostname }}"
       username: "{{ user }}"
       password: "{{ pass }}"
       protocol: "{{ protocol }}"
```


#### Notes

- Tenant must exist prior to using this module

---


## aci_contract_subjects
Manages initial contracts subjects 

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Manages contract subjects

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol to use  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li> </ul> | Http verbs, i.e. Get or Post |
| subject_name | yes | | <ul></ul> | Contract Subject name |
| contract_name  |   yes  |  | <ul></ul> |  Name of the contract which will contain the subject  |
| tenant_name  |   yes  |  | <ul></ul> |  name of tenant this contract  will be part of  |
| priority |   no  | unspecified | <ul> <li>unspecified</li>  <li>level1</li>  <li>level2</li>  <li>level3</li> </ul> |  priority (qosclass) of contract subject |
| reverse_filter | no | yes | <ul><li>yes</li> <li>no</li> </ul> | Enable or Disable Reverse Filter |
| target | no | unspecified | <ul></ul> |  Contract subject Target | 
| filter_name | yes | | <ul></ul> | name of the filter chain |
| directive  |   no  | none  | <ul> <li>log</li>  <li>none</li> |  Filter chain directive can be none and/or log |
| descr  |   no  |  | <ul></ul> |  description of contract subject |
 
#### Examples

```
 aci_contract_subjects:
       action: "{{ action }}"
       subject_name: "{{ subject_name }}"
       contract_name: "{{ contract_name }}"
       tenant_name: "{{ tenant_name }}"
       priority: "{{ priority }}"
       reverse_filter: "{{ reverse_filter }}"
       filter_name: "{{ filter_name }}"
       directive: "{{ directive }}"   
       target: "{{ target }}"
       descr: "{{ descr }}"
       host: "{{ inventory_hostname }}"
       username: "{{ user }}"
       password: "{{ pass }}"
       protocol: "{{ protocol }}"

```


#### Notes

- Tenant and contract must exist prior to using this module

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
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  |   yes  |  | <ul></ul> |  Name of tenant  |
| descr  |   no  |  | <ul></ul> |  description of tenant  |

 
#### Examples

```
 aci_tenant:
       action: "{{ action }}"
       tenant_name: "{{ tenant_name }}"
       descr: "{{ descr }}"
       host: "{{ inventory_hostname }}"
       username: "{{ user }}"
       password: "{{ pass }}"
       protocol: "{{ protocol }}"

```

---

## aci_anp
Manage application network profile in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Application Network profiles 

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  |   yes  |  | <ul></ul> |  Name of tenant the Application profile will be a part of |
| app_profile_name | yes | | <ul></ul> | Name of the Application profile |
| descr  |   no  |  | <ul></ul> |  description of applciation profile  |

 
#### Examples

```
  aci_anp:
       action: "{{ action }}"
       app_profile_name: "{{ app_profile_name }}"
       tenant_name: "{{ tenant_name }}"
       descr: "{{ descr }}"
       host: "{{ inventory_hostname }}"
       username: "{{ user }}"
       password: "{{ pass }}"
       protocol: "{{ protocol }}"

```
#### Notes

- Tenant must exist prior to using this module

---

## aci_epg
Manage end point groups in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage end point groups

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  |   yes  |  | <ul></ul> |  Name of tenant the Application profile will be a part of |
| app_profile_name | yes | | <ul></ul> | Name of the Application profile the EPG will be a part of |
| epg_name | yes | | <ul></ul> | Name of the end point group |
| descr  |   no  |  | <ul></ul> |  description of end point group  |
| bd_name | yes | | <ul></ul> | Bridge Domain the EPG is being associated with |
| priority | no | unspecified | <ul> <li>unspecified</li>  <li>level1</li>  <li>level2</li>  <li>level3</li> </ul> |  priority (qosclass) of epg  |
| intra_epg_isolation | no | unenforced | <ul><li>enforced</li> <li>unenforced</li> | Intra EPG isolation |
| contract_type | no | | <ul><li>provider</li> <li>consumer</li> <li>both</li> | the type of contract being attached to the epg |
| contract_name_provider | no | | <ul></ul>  | Name of the provider contract |
| priority_provider | no | unspecified | <ul> <li>unspecified</li>  <li>level1</li>  <li>level2</li>  <li>level3</li> </ul> |  priority (qosclass) of provider contract  |
| contract_name_consumer | no | | <ul></ul>  | Name of the consumer contract |
| priority_consumer | no | unspecified | <ul> <li>unspecified</li>  <li>level1</li>  <li>level2</li>  <li>level3</li> </ul> |  priority (qosclass) of consumer contract  |


#### Examples

```
   aci_epg:
       action: "{{ action }}"
       epg_name: ""{{ epg_name }}"
       app_profile_name: "{{ app_profile_name }}"
       tenant_name: "{{ tenant_name }}"
       bd_name: "{{ bd_name }}"
       priority: "{{ priority }}"
       contract_type: "{{ contract_type }}"
       contract_name_provider: "{{ contract_name_provider }}"
       contract_name_consumer: "{{ contract_name_consumer }}"
       priority_provider: "{{ priority_provider }}"
       priority_consumer: "{{ priority_consumer }}"
       intra_epg_isolation: "{{ intra_epg_isolation }}"
       descr: "{{ descr }}"
       host: "{{ inventory_hostname }}"
       username: "{{ user }}"
       password: "{{ pass }}"
       protocol: "{{ protocol }}"


```
#### Notes

- Tenant, Application Profile and Bridge Domain must exist prior to using this module
- Contract name and priority for Provider will only need to be provided if the contract type is provider/both 
- Contract name and priority for Consumer will only need to be provided if the contract type is consumer/both
- Not entering the Contract type will create a EPG with BD associated without assigning contracts

---

## aci_epr
Manage end point retention policy 

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage end point retention policy

#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  |   yes  |  | <ul></ul> |  Name of tenant the policy will be a part of |
| epr_name | yes | | <ul></ul> | Name of the End point retention policy |
| descr  |   no  |  | <ul></ul> |  description of EPR |
| bounce_age | no | 630 | <ul></ul> | Bounce Entry Aging Interval in seconds |
| hold_interval | no | 300 | <ul></ul> | hold interval in seconds |
| local_ep_interval | no | 900 | <ul></ul> | Local end point aging interval in seconds |
| remote_ep_interval | no | 300 | <ul></ul> | Remote end point aging interval in seconds |
| move_frequency | no | 256 | <ul></ul> | Move Frequency per second |

 
#### Examples

```
 aci_epr:
        action: "{{ action }}"
        tenant_name: "{{ tenant_name }}"
        epr_name: "{{ epr_name }}"
        bounce_age: "{{ bounce_age }}"
        hold_interval: "{{ hold_interval }}"
        local_ep_interval: "{{ local_ep_interval }}"
        remote_ep_interval: "{{ remote_ep_interval }}"
        move_frequency: "{{ move_frequency }}"
        descr: "{{ descr }}"
        host: "{{ inventory_hostname }}"
        username: "{{ username }}" 
        password: "{{ password }}"
        protocol: "{{ protocol }}"

```
#### Notes

- Tenant must exist prior to using this module

---

## aci_fiber_channel_policy
Manage fiber channel policy in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage fiber channel policy
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| fc_policy  |   yes  |  | <ul></ul> |  Name of fiber channel policy|
| port_mode | no | f | <ul><li>f</li><li>np</li> </ul> | Port Mode |
| descr  |   no  |  | <ul></ul> |  description of fiber channel policy |

 
#### Examples

```
   aci_fiber_channel_policy:
         action: "{{ action }}"
         fc_policy: "{{ fc_policy }}"
         port_mode: "{{ port_mode }}" 
         descr: "{{ descr }}" 
         host: "{{ inventory_hostname }}"
         username: "{{ username }}"
         password: "{{ password }}"
         protocol: "{{ protocol }}"

```
---

## aci_l2_interface_policy
Manage L2 Interface Policy in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage L2 interface Policy
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| l2_policy  |   yes  |  | <ul></ul> |  Name of L2 interface policy|
| vlan_scope | no | gloabl | <ul><li>global</li><li>portlocal</li> </ul> | Scope of VLAN |
| descr  |   no  |  | <ul></ul> |  description of L2 interface policy |

 
#### Examples

```
   aci_l2_interface_policy: 
        action: "{{ action }}"
        l2_policy: "{{ l2_policy }}"
        vlan_scope: "{{ vlan_policy }}"
        descr: "{{ descr }}"
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
	protocol: "{{ protocol }}"

```
---
## aci_lldp_interface_policy
Manage LLDP Interface Policy in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage LLDP interface policy
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| lldp_policy  |   yes  |  | <ul></ul> |  Name of LLDP interface policy|
| receive_state | no | enabled | <ul><li>enabled</li><li>disabled</li> </ul> | Receive State |
| transmit_state | no | enabled | <ul><li>enabled</li><li>disabled</li> </ul> | Transmit State |
| descr  |   no  |  | <ul></ul> |  description of LLDP interface policy |

 
#### Examples

```
    aci_lldp_interface_policy: 
        action: "{{ action }}"
        lldp_policy: "{{ lldp_policy }}"
        receive_state: "{{ receive_state }}"
        transmit_state: "{{ transmit_state }}"
        descr: "{{ descr }}" 
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
       	protocol: "{{ protocol }}"

```
---

## aci_login_domain
Manage Login Domain for an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Login Domain
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| login_domain  |   yes  |  | <ul></ul> |  Name of Login Domain|
| descr  |   no  |  | <ul></ul> |  description of login domain |

 
#### Examples

```
   aci_login_domain:
        action: "{{ action }}"
        login_domain: "{{ login_domain }}"
        descr: "{{ descr }}"
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        protocol: "{{ protocol }}"

```
---

## aci_monitoring_policy
Manage monitoring policy in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Monitoring policy
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  |   yes  |  | <ul></ul> |  Name of tenant , the monitoring policy will be a part of |
| monitoring_policy | yes |  | <ul></ul> | Name of the monitoring policy | 
| descr  |   no  |  | <ul></ul> |  description of Monitoring policy |

 
#### Examples

```
  aci_monitoring_policy:
        action: "{{ action }}"
        tenant_name: "{{ tenant_name }}"
	monitoring_policy: "{{ monitoring_policy }}"
        descr: "{{ descr }}"
        host= "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
       	protocol: "{{ protocol }}"


```
#### NOTES

- Tenant must exist prior to using this module

---

## aci_mcp_interface
Manage MCP Interface policy in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage MCP Interface Policy
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| mcp_interface  |   yes  |  | <ul></ul> |  Name of MCP interface policy|
| descr  |   no  |  | <ul></ul> |  description of MCP Interface policy |
| admin_state | no | enabled | <ul><li>enabled</li> <li>disabled</li></ul> | Enable or Disable admin state | 
 
#### Examples

```
  aci_mcp_interface:
        action: "{{ action }}" 
        mcp_interface: "{{ mcp_interface }}"
        admin_state: "{{ admin_state }}"
        descr: "{{ descr }}
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
	protocol:"{{ protocol }}"

```

---

## aci_port_channel_interface
Manage Port Channel Interface in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Port channel interface
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| port_channel  |   yes  |  | <ul></ul> |  Name of the port channel interface |
| max_link | no | 16 | <ul></ul> | Maximum number of links [1-16] | 
| min_link | no | 1 | <ul></ul> | Mininum number of links [1-16] |
| mode | no | off | <ul><li>off</li> <li>mac-pin</li> <li>active</li> <li>passive</li> <li>mac-pin-nicload</li></ul> | Mode of the port channel |
| descr  |   no  |  | <ul></ul> |  description of Port channel interface |

 
#### Examples

```
  aci_port_channel_interface:
        action: "{{ action }}"
        port_channel: "{{ port_channel }}"
        max_link: "{{ max_link }}"
        min_link: "{{ min_link }}"
        mode: "{{ mode }}"
        descr: "{{ descr }}"
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
	protocol: "{{ protocol }}"


```
---

## aci_port_security
Manage Port Security in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Port Security
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| port_security  |   yes  |  | <ul></ul> |  Name of the port security|
| max_end_points | no | 0 | <ul></ul> | Maximum number of end points allowed [0-12000] | 
| descr  |   no  |  | <ul></ul> |  description of Port Security |

 
#### Examples

```
  aci_port_security:
        action: "{{ action }}"
        port_security: "{{ port_security }}"
        max_end_points: "{{ max_end_points }}"
        descr: "{{ descr }}"
        host: "{{ inventory_hostname }}"
        username: "{{ username }}" 
        password: "{{ password }}"
	protocol: "{{ protocol }}"


```
---

## aci_route_tag_policy
Manage Route Tag Policy in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Route Tag policy
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  | yes |  | <ul></ul> |  Name of the tenant, the RTP will be a part of |
| rtp_name | yes|  | <ul></ul> | Name of the Route Tag Policy  | 
| tag | no | 4294967295 | <ul></ul> | Tag for Route Tag Policy |
| descr  |   no  |  | <ul></ul> |  description of Route Tag Policy |

#### Examples

```
  aci_route_tag_policy:
         action: "{{ action }}" 
         tenant_name: "{{ tenant_name }}"
         rtp_name: "{{ rtp_name }}" 
         tag: "{{ tag }}"
	 descr: "{{ descr }}" 
	 host: "{{ inventory_hostname }}" 
	 username: "{{ username }}"
	 password: "{{ password }}"
	 protocol: "{{ protocol }}"

```
#### NOTES
- Tenant must exist before using this module

---

## aci_span_dst_group
Manage SPAN Destination Group in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage SPAN Destination Group
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  | yes |  | <ul></ul> |  Name of the tenant, the SPAN destination group will be a part of |
| dst_group | yes|  | <ul></ul> | Name of the SPAN Destination Group  | 
| descr  |   no  |  | <ul></ul> |  description of SPAN Destination Group |

#### Examples

```
  aci_span_dst_group: 
        action:"{{ action }}" 
        tenant_name:"{{ tenant_name }}" 
       	dst_group:"{{ dst_group }}" 
 	descr:"{{ descr }}" 
	host:"{{ inventory_hostname }}" 
	username:"{{ username }}"
       	password:"{{ password }}"
	protocol: "{{ protocol }}"

```
#### NOTES
- Tenant must exist before using this module

---

## aci_span_src_group
Manage SPAN Source Group in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage SPAN Source Group
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  | yes |  | <ul></ul> |  Name of the tenant, the SPAN source group will be a part of |
| src_group | yes |  | <ul></ul> | Name of the SPAN Source Group |
| dst_group | yes|  | <ul></ul> | Name of the SPAN Destination Group  | 
| admin_state | no | enabled | <ul><li>enabled</li> <li>disabled</li></ul> | Enable or Disable admin state |
| descr  |   no  |  | <ul></ul> |  description of SPAN Source Group |

#### Examples

```
  aci_span_src_group: 
	action:"{{ action }}" 	
	tenant_name:"{{ tenant_name }}" 
     	src_group:"{{ src_group }}" 
	dst_group:"{{ dst_group }}" 
	admin_state:"{{ admin_state }}" 
	descr:"{{ descr }}" 
	host:"{{ inventory_hostname }}" 
	username:"{{ username }}" 
	password:"{{ password }}"
     	protocol: "{{ protocol }}"

```
#### NOTES
- Tenant and SPAN destination group must exist before using this module

---

## aci_taboo_contracts
Manage Taboo Contracts in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Taboo Contracts
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  | yes |  | <ul></ul> |  Name of the tenant, the Taboo Contract will be a part of |
| taboo_contract | yes |  | <ul></ul> | Name of the Taboo Contract |
| descr  |   no  |  | <ul></ul> |  description of Taboo Contract |

#### Examples

```
  aci_taboo_contracts: 
     	action:"{{ action }}" 
        tenant_name:"{{ tenant_name }}" 
	taboo_contract:"{{ taboo_contract }}" 
     	descr:"{{ descr }}" 
     	host:"{{ inventory_hostname }}" 
     	username:"{{ username }}" 
	password:"{{ password }}"
     	protocol: "{{ protocol }}"

```
#### NOTES
- Tenant  must exist before using this module

---
## aci_action_rule_profile
Manage Action Rule Profile in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Action Rule Profile
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  | yes |  | <ul></ul> |  Name of the tenant, the action rule profile will be a part of |
| action_rule_name | yes |  | <ul></ul> | Name of the Action Rule Profile |
| descr  |   no  |  | <ul></ul> |  description of Action Rule Profile |

#### Examples

```
  aci_action_rule_profile:
         action: "{{ action }}"
         tenant_name: "{{ tenant_name }}" 
         action_rule_name: "{{ action_rule_name }}"
         descr: "{{ descr }}"  
         host: "{{ inventory_hostname }}"
         username: "{{ username }}" 
         password: "{{ password }}"
	 protocol: "{{ protocol }}"

```
#### NOTES
- Tenant  must exist before using this module

---
## aci_aep
Manage Attachable Entity Profile in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Attachable Entity Profile
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| aep_name | yes |  | <ul></ul> | Name of the Attachable Entity Profile |
| descr  |   no  |  | <ul></ul> |  description of Attachable Entity Profile |

#### Examples

```
    aci_aep:
         action: "{{ action }}"  
         aep_name: "{{ aep_name }}" 
         descr: "{{ descr }}" 
         host: "{{ inventory_hostname }}"
         username: "{{ username }}"
         password: "{{ password }}"
         protocol: "{{ protocol }}"
```
---

## aci_epg_domain_binding
Manage Physical domain binding to EPGs in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Physical domain binding to EPGs
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  | yes |  | <ul></ul> | Name of the tenant, the EPG is a part of |
| app_profile_name | yes | <ul></ul> | Name of the Application profile that contains the EPG |
| epg_name | yes |  | <ul></ul> | Name of the EPG to which the Physical Domain will be associated |
| encap | yes | | <ul></ul> | VLAN Encapsulation |
| domain | no | phys | <ul><li> phys </li></ul> | Domain type  |
| domain_profile | yes | | <ul></ul> | Name of the Physical domain profile |
| immediacy | no | immediate | <ul><li>immediate</li> <li>on-demand</li></ul> | Immediacy |

#### Examples

```
    aci_epg_domain_binding: 
        action: "{{ action }}"
	tenant_name: "{{ tenant_name }}"
	app_profile_name: "{{ app_profile_name }}"
       	epg_name: "{{ epg_name }}"
       	encap: 1
       	domain: "{{ domain }}"
       	domain_profile: "{{ domain_profile }}"
       	immediacy: "{{ immediacy }}" 
       	host: "{{ inventory_hostname }}"
	username: "{{ user }}"
       	password: "{{ pass }}"
	protocol: "{{ protocol }}"

```
#### NOTES
- Tenant , Application Profile and EPG must exist before using this module

---

## aci_epg_domain_binding
Manage Physical domain binding to EPGs in an ACI fabric

  * Synopsis
  * Options
  * Examples

#### Synopsis
 Offers ability to manage Physical domain binding to EPGs
#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   yes  |  admin  | <ul></ul> |  Username used to login to the switch  |
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |
| protocol  |   no  |  https  | <ul> <li>http</li>  <li>https</li> </ul> |  Dictates connection protocol  |
| host  |   yes  |  | <ul></ul> |  IP Address or hostname of APIC resolvable by Ansible control host  |
| action | yes | | <ul><li>Post</li> <li>Get</li></ul> | Http verbs i.e. Get or Post |
| tenant_name  | yes |  | <ul></ul> | Name of the tenant, the EPG is a part of |
| app_profile_name | yes | <ul></ul> | Name of the Application profile that contains the EPG |
| epg_name | yes |  | <ul></ul> | Name of the EPG to which the VMM Domain will be associated |
| domain_profile | yes | | <ul></ul> | Name of the Physical domain profile |
| deploy_immediacy | no | on-demand | <ul><li>immediate</li> <li>on-demand</li></ul> | Deploy Immediacy |
| resolution_immediacy | no | immediate | <ul><li>immediate</li> <li>on-demand</li> <li>pre-provision</li></ul> | Resolution Immediacy |
| netflow | no | disabled | <ul><li>enabled</li> <li>disbaled</li></ul> | NetFlow Preference|


#### Examples

```
    aci_dynamic_vmm_binding:
           action: "{{ action }}"
           app_profile_name: "{{ app_profile_name }}"
           tenant_name: "{{ tenant_name }}"
           epg_name: "{{ epg_name }}"
           domain_profile: "{{ domain_profile }}"
           deploy_immediacy: "{{ deploy_immediacy }}"
	   resolution_immediacy: "{{ resolution_immediacy }}"
	   netflow: "{{ netflow }}"
           host: "{{ inventory_hostname }}"
           username: "{{ user }}"
           password: "{{ pass }}"
	   protocol: "{{ protocol }}"

```
#### NOTES
- Tenant , Application Profile and EPG must exist before using this module

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
| password  |   yes  |    | <ul></ul> |  Password used to login to the switch  |


 
#### Examples

```

# add a tenant
- aci_rest: 
    action: post
    uri: /api/mo/uni.xml 
    config_file: /home/cisco/ansible/aci/configs/aci_config.xml
    host: "{{ inventory_hostname }}"
    username: "{{ user }}"
    password: "{{ pass }}"

# get tenants
- aci_rest: 
     action: get
     uri: /api/node/class/fvTenant.json 
     host: "{{ inventory_hostname }}"
     username: "{{ user }}" 
     password: "{{ pass }}"

# configure contracts
- aci_rest:
    action: post 
    uri: /api/mo/uni.xml 
    config_file: /home/cisco/ansible/aci/configs/contract_config.xml 
    host: "{{ inventory_hostname }}"
    username: "{{ user }}"
    password: "{{ pass }}"


```


#### Notes

- Tenant must be exist prior to using this module


---
Created by Network to Code, LLC
For:
2015
