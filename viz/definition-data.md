# Definiation of Data
--------
[TOC]

Abstract:
>This post is the definiation of data-mbbo.json.

Now Browser is interactive with service mbbo by data-mbbo.json, getting dict data to render the near-optima of mbbo for vm-consolidation.


## Data definiation

```
data = {
  'vms_num': int-num,
  'pms_num': int-num,
  'vms': [[v,n],...,[c,k]],
  'pms': [[a,b],...,[0,0],...],
  'state': [[q,w,e],[a],[],[d],...],
  'plan': [[f,g],[h,j],...,[k,l]],
  'HSI-cost': [[0,0,0],[0,0,0]]
  'parameters': [rp_u,rm_u,related_coefficient,diff_factor,p_mutation,generation],
  'efficiency': [algorithm_time,nums-unused-pm,nums-mig-vms]
}
```
`data['vms_num']` : the nums of all vms

`data['pms_num']` : the nums of all served pms, thinking as the `vms_num`.

`data['vms']` : to record [cpu,mem] of every vm

`data['pms']` : to record the used [cpu,mem] of pm-i, [0,0] if pm is empty.

`data['state']` : to record the index [vm-a,vm-b,...] of all vms hosted on pm-i, [] if pm is empty.

`data['plan']` : to record the migrate-list [pm-source,pm-destination] of vm-i.

`data['HSI-cost']` : to record the 3 hsi-cost [power,load-index,mig-time] of initial chrom and near-optima chrom respectively.

`data['parameters']` : to record parameters of MBBO algorithm.

`data['efficiency']` : simple calculation about algorithm_time, nums of unused pms, nums of migration vms.

## parameters

- rp_u

- rm_u

- related_coefficient

- diff_factor

- p_mutation

- generation

## efficiency

- algorithm_time

- nums-unused-pm

- nums-mig-vms
